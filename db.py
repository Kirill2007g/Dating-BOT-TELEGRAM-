import sqlite3
import random
from datetime import date, timedelta

conn = sqlite3.connect("dating.db")
cursor = conn.cursor()

DAILY_LIMIT = 500

# Canonical city names (Ukrainian/Russian variants → stored Russian name)
_CITY_NORMALIZE: dict[str, str] = {
    "київ": "Киев",          "киев": "Киев",
    "харків": "Харьков",     "харьков": "Харьков",
    "одеса": "Одесса",       "одесса": "Одесса",
    "дніпро": "Днепр",       "днепр": "Днепр",
    "дніпропетровськ": "Днепр", "днепропетровск": "Днепр",
    "запоріжжя": "Запорожье", "запорожье": "Запорожье",
    "львів": "Львов",        "львов": "Львов",
    "кривий ріг": "Кривой Рог", "кривой рог": "Кривой Рог",
    "миколаїв": "Николаев",  "николаев": "Николаев",
    "вінниця": "Винница",    "винница": "Винница",
    "полтава": "Полтава",
    "чернігів": "Чернигов",  "чернигов": "Чернигов",
    "черкаси": "Черкассы",   "черкассы": "Черкассы",
    "суми": "Сумы",          "сумы": "Сумы",
    "хмельницький": "Хмельницкий", "хмельницкий": "Хмельницкий",
    "житомир": "Житомир",
    "рівне": "Ровно",        "ровно": "Ровно",
    "тернопіль": "Тернополь", "тернополь": "Тернополь",
    "ужгород": "Ужгород",
    "херсон": "Херсон",
    "івано-франківськ": "Ивано-Франковск",
    "ивано-франковск": "Ивано-Франковск",
    "питер": "Санкт-Петербург",
    "спб": "Санкт-Петербург",
    "санкт-петербург": "Санкт-Петербург",
}


def normalize_city(city: str) -> str:
    key = city.lower().strip()
    return _CITY_NORMALIZE.get(key, city.strip().title())


def init_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS profiles (
        telegram_id    INTEGER PRIMARY KEY,
        username       TEXT,
        name           TEXT,
        age            INTEGER,
        city           TEXT,
        gender         TEXT,
        looking_for    TEXT,
        description    TEXT,
        active         INTEGER DEFAULT 1,
        language       TEXT DEFAULT 'ru',
        premium_until  TEXT DEFAULT NULL,
        daily_views    INTEGER DEFAULT 0,
        last_view_date TEXT DEFAULT NULL
    )""")
    # Миграция: добавляем колонки если таблица уже существовала без них
    for col, definition in [
        ("language",       "TEXT DEFAULT 'ru'"),
        ("premium_until",  "TEXT DEFAULT NULL"),
        ("daily_views",    "INTEGER DEFAULT 0"),
        ("last_view_date", "TEXT DEFAULT NULL"),
    ]:
        try:
            cursor.execute(f"ALTER TABLE profiles ADD COLUMN {col} {definition}")
        except Exception:
            pass

    # Отдельная таблица для медиа (до 3 файлов на профиль)
    cursor.execute("""CREATE TABLE IF NOT EXISTS media (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        profile_id  INTEGER,
        file_id     TEXT,
        media_type  TEXT,
        position    INTEGER,
        FOREIGN KEY (profile_id) REFERENCES profiles(telegram_id)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS likes (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        from_user INTEGER,
        to_user   INTEGER,
        action    TEXT
    )""")
    conn.commit()


# ─── Профиль ────────────────────────────────────────────────────────────────

def add_profile(telegram_id: int, username: str, name: str, age: int, city: str,
                gender: str, looking_for: str, description: str) -> None:
    existing = cursor.execute(
        "SELECT language, premium_until FROM profiles WHERE telegram_id = ?", (telegram_id,)
    ).fetchone()
    lang = existing[0] if existing else "ru"
    premium_until = existing[1] if existing else None
    cursor.execute(
        """INSERT OR REPLACE INTO profiles
        (telegram_id, username, name, age, city, gender, looking_for, description, language, premium_until)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (telegram_id, username, name, age, normalize_city(city), gender, looking_for, description,
         lang, premium_until)
    )
    conn.commit()


def get_profile(telegram_id: int) -> tuple | None:
    cursor.execute("SELECT * FROM profiles WHERE telegram_id = ?", (telegram_id,))
    return cursor.fetchone()


def delete_profile(telegram_id: int) -> bool:
    cursor.execute("DELETE FROM profiles WHERE telegram_id = ?", (telegram_id,))
    clear_media(telegram_id)
    conn.commit()
    return cursor.rowcount > 0


def deactivate_profile(telegram_id: int) -> None:
    cursor.execute("UPDATE profiles SET active = 0 WHERE telegram_id = ?", (telegram_id,))
    conn.commit()


def activate_profile(telegram_id: int) -> None:
    cursor.execute("UPDATE profiles SET active = 1 WHERE telegram_id = ?", (telegram_id,))
    conn.commit()


def update_description(telegram_id: int, description: str) -> None:
    cursor.execute(
        "UPDATE profiles SET description = ? WHERE telegram_id = ?",
        (description, telegram_id)
    )
    conn.commit()


def update_language(telegram_id: int, language: str) -> None:
    cursor.execute(
        "UPDATE profiles SET language = ? WHERE telegram_id = ?",
        (language, telegram_id)
    )
    conn.commit()


def update_username(telegram_id: int, username: str) -> None:
    cursor.execute(
        "UPDATE profiles SET username = ? WHERE telegram_id = ?",
        (username, telegram_id)
    )
    conn.commit()


# ─── Медиа ──────────────────────────────────────────────────────────────────

def add_media(profile_id: int, file_id: str, media_type: str) -> bool:
    cursor.execute("SELECT COUNT(*) FROM media WHERE profile_id = ?", (profile_id,))
    count = cursor.fetchone()[0]
    if count >= 3:
        return False
    cursor.execute(
        "INSERT INTO media (profile_id, file_id, media_type, position) VALUES (?, ?, ?, ?)",
        (profile_id, file_id, media_type, count + 1)
    )
    conn.commit()
    return True


def clear_media(profile_id: int) -> None:
    cursor.execute("DELETE FROM media WHERE profile_id = ?", (profile_id,))
    conn.commit()


def get_media(profile_id: int) -> list:
    cursor.execute(
        "SELECT file_id, media_type FROM media WHERE profile_id = ? ORDER BY position",
        (profile_id,)
    )
    return cursor.fetchall()


def update_media(profile_id: int, media_list: list) -> None:
    clear_media(profile_id)
    for i, (file_id, media_type) in enumerate(media_list):
        cursor.execute(
            "INSERT INTO media (profile_id, file_id, media_type, position) VALUES (?, ?, ?, ?)",
            (profile_id, file_id, media_type, i + 1)
        )
    conn.commit()


# ─── Лайки / матчи ──────────────────────────────────────────────────────────

def add_like(from_user: int, to_user: int, action: str) -> None:
    cursor.execute(
        "INSERT INTO likes (from_user, to_user, action) VALUES (?, ?, ?)",
        (from_user, to_user, action)
    )
    conn.commit()


def check_match(user1: int, user2: int) -> bool:
    """Проверяет, лайкнул ли user1 пользователя user2."""
    cursor.execute(
        "SELECT 1 FROM likes WHERE from_user = ? AND to_user = ? AND action = 'like'",
        (user1, user2)
    )
    return cursor.fetchone() is not None


def get_who_liked_me(telegram_id: int) -> list:
    """Возвращает профили тех, кто лайкнул меня и я ещё не ответил."""
    cursor.execute("""
        SELECT * FROM profiles
        WHERE telegram_id IN (
            SELECT from_user FROM likes
            WHERE to_user = ? AND action = 'like'
        )
        AND telegram_id NOT IN (
            SELECT to_user FROM likes
            WHERE from_user = ?
        )
        AND active = 1
    """, (telegram_id, telegram_id))
    return cursor.fetchall()


# ─── Подбор анкет ────────────────────────────────────────────────────────────

def get_next_profile(telegram_id: int) -> tuple | None:
    my = get_profile(telegram_id)
    if not my:
        return None

    # Индексы: 0=tg_id, 1=username, 2=name, 3=age, 4=city,
    #           5=gender, 6=looking_for, 7=desc, 8=active, 9=language
    my_age        = my[3]
    my_city       = my[4]
    my_looking_for = my[6]

    gender_clause = "" if my_looking_for == "все" else "AND gender = ?"
    gender_params = () if my_looking_for == "все" else (my_looking_for,)

    def query(age_min: int, age_max: int) -> tuple | None:
        sql = f"""
            SELECT * FROM profiles
            WHERE telegram_id != ?
            AND active = 1
            AND LOWER(city) = LOWER(?)
            AND age BETWEEN ? AND ?
            {gender_clause}
            AND telegram_id NOT IN (
                SELECT to_user FROM likes WHERE from_user = ?
            )
            ORDER BY CASE WHEN premium_until IS NOT NULL AND premium_until >= DATE('now') THEN 0 ELSE 1 END, RANDOM()
            LIMIT 1
        """
        cursor.execute(sql, (telegram_id, my_city, age_min, age_max) + gender_params + (telegram_id,))
        return cursor.fetchone()

    # 90% — показываем точный возраст, 10% — сразу пробуем ±1
    if random.random() < 0.9:
        result = query(my_age, my_age)
        if result:
            return result

    # Расширяем диапазон по 1 году, максимум ±4
    for delta in range(1, 5):
        result = query(my_age - delta, my_age + delta)
        if result:
            return result

    return None


# ─── Язык ────────────────────────────────────────────────────────────────────

def get_lang(telegram_id: int) -> str:
    cursor.execute("SELECT language FROM profiles WHERE telegram_id = ?", (telegram_id,))
    row = cursor.fetchone()
    return row[0] if row and row[0] else "ru"


# ─── Премиум ─────────────────────────────────────────────────────────────────

def activate_premium(telegram_id: int, days: int) -> None:
    cursor.execute("SELECT premium_until FROM profiles WHERE telegram_id = ?", (telegram_id,))
    row = cursor.fetchone()
    today = date.today()
    if row and row[0] and row[0] >= today.isoformat():
        base = date.fromisoformat(row[0])
    else:
        base = today
    new_until = (base + timedelta(days=days)).isoformat()
    cursor.execute(
        "UPDATE profiles SET premium_until = ? WHERE telegram_id = ?",
        (new_until, telegram_id)
    )
    conn.commit()


def check_premium(telegram_id: int) -> bool:
    cursor.execute("SELECT premium_until FROM profiles WHERE telegram_id = ?", (telegram_id,))
    row = cursor.fetchone()
    return bool(row and row[0] and row[0] >= date.today().isoformat())


def delete_like(from_user: int, to_user: int) -> None:
    cursor.execute(
        "DELETE FROM likes WHERE from_user = ? AND to_user = ? AND action = 'dislike'",
        (from_user, to_user),
    )
    conn.commit()


def get_all_active_users() -> list[tuple]:
    cursor.execute("SELECT telegram_id, language FROM profiles WHERE active = 1")
    return cursor.fetchall()


def check_and_increment_views(telegram_id: int) -> bool:
    """Returns True if the user may view one more profile (increments counter).
    Premium users always return True. Non-premium users are capped at DAILY_LIMIT."""
    today = date.today().isoformat()
    row = cursor.execute(
        "SELECT daily_views, last_view_date, premium_until FROM profiles WHERE telegram_id = ?",
        (telegram_id,),
    ).fetchone()
    if not row:
        return False
    daily_views, last_view_date, premium_until = row
    if premium_until and premium_until >= today:
        return True
    if last_view_date != today:
        daily_views = 0
    if daily_views >= DAILY_LIMIT:
        return False
    cursor.execute(
        "UPDATE profiles SET daily_views = ?, last_view_date = ? WHERE telegram_id = ?",
        (daily_views + 1, today, telegram_id),
    )
    conn.commit()
    return True

STRINGS: dict[str, dict[str, str]] = {
    "ru": {
        "welcome":           "Я помогу найти тебе пару или просто друзей.\nМожно я задам пару вопросов?",
        "welcome_back":      "С возвращением! Вот твоя анкета:",
        "menu_prompt":       "Смотри анкеты или измени свою 👇",
        "ask_age":           "Сколько тебе лет?",
        "ask_gender":        "Теперь определимся с полом",
        "ask_looking_for":   "Кто тебе интересен?",
        "ask_city":          "Из какого ты города?",
        "ask_name":          "Как мне тебя называть?",
        "ask_description":   "Расскажи о себе и кого хочешь найти, чем предлагаешь заняться.\nЭто поможет лучше подобрать тебе компанию.\n\nМожно пропустить 👇",
        "ask_photo":         "Теперь отправь фото, видео или запиши кружочек.\nМожно до 3 штук 👇",
        "profile_preview":   "Вот так выглядит твоя анкета:",
        "confirm_prompt":    "Всё верно?",
        "profile_saved":     "Анкета сохранена! 🎉",
        "refill_start":      "Начнём заново! Сколько тебе лет?",
        "no_profile":        "У тебя нет анкеты",
        "liked_one":         "Тебя лайкнул(а) {who}! Посмотришь?",
        "liked_many":        "Тебя лайкнули {count} раз! Посмотришь?",
        "no_profiles":       "Анкеты закончились 😴",
        "match":             "Супер! Надеюсь, хорошо проведёте время 🙌\nНачинай общаться 👉 {link}",
        "liked_notif_one":   "Тебя лайкнул(а) {who}!",
        "liked_notif_many":  "Тебя лайкнули уже {count} раз!",
        "notif_msg":         "\n\nСообщение: {msg}",
        "envelope_prompt":   "Напиши сообщение для {name}.\nОтправится вместе с лайком 💌",
        "envelope_text_only": "Напиши текстовое сообщение",
        "stop_viewing":      "Смотри анкеты или измени свою 👇",
        "settings_prompt":   "Дополнительные настройки:",
        "choose_language":   "Выбери язык интерфейса:",
        "language_saved":    "Язык изменён на: {lang} ✅",
        "photo_updated":     "Фото/видео обновлено! ✅",
        "text_updated":      "Текст анкеты обновлён! ✅",
        "report_sent":       "Жалоба отправлена. Мы рассмотрим её в ближайшее время.",
        "skip_liked":        "Хорошо, возвращаемся в меню",
        "enter_age_number":  "Введи возраст числом",
        "age_range":         "Возраст от 13 до 99",
        "choose_button":     "Выбери кнопку",
        "enter_city":        "Введи название города",
        "enter_name":        "Имя минимум 2 символа",
        "enter_text":        "Напиши текстом или нажми Пропустить",
        "name_too_long":      "Имя слишком длинное (максимум 50 символов)",
        "text_too_long":     "Максимум 500 символов",
        "send_media":        "Отправь фото, видео или кружочек",
        "send_at_least_one": "Сначала отправь хотя бы одно фото, видео или кружочек",
        "max_media":         "Максимум 3 файла. Нажми Готово ✅",
        "media_added":       "Принято! Можно добавить ещё {n} или нажми Готово",
        "enter_new_text":    "Напиши новый текст анкеты (до 999 символов):",
        "enter_new_photo":   "Отправь новое фото, видео или кружочек.\nМожно до 3 штук 👇",
        "premium_coming":    "⭐ Премиум скоро будет доступен!",
        "premium_menu": (
            "Активируй Premium и будь в топе ✨\n\n"
            "Выделяйся среди других:\n"
            "📈 Больше показов анкеты\n"
            "🚀 Больше лайков в день\n"
            "👀 Твои лайки видят первыми\n"
            "⭐️ Твой профиль выше других\n\n"
            "Выбери срок Premium:"
        ),
        "premium_activated":  "✅ Premium активирован на {days} дней!\nТвой профиль теперь в топе.",
        "premium_already":    "⭐ У тебя уже есть Premium до {until}!\nМожно продлить — новые дни прибавятся к текущим.\n\nВыбери срок:",
        "premium_terms":      "\n\n_Оплачивая Premium, ты принимаешь [условия покупки](http://pt.leomatchbot.com/)._",
        "daily_limit":        "На сегодня ты исчерпал лимит просмотра анкет (500).\nХочешь смотреть дальше — купи Премиум или жди завтра ⏳",
        "btn_browse":        "Смотреть анкеты",
        "btn_my_profile":    "Моя анкета",
        "btn_refill":        "Заполнить заново",
        "btn_change_photo":  "Изменить фото/видео",
        "btn_change_text":   "Изменить текст",
        "btn_settings":      "Доп настройки",
        "btn_premium":       "⭐ Активируй Премиум",
        "btn_male":          "Я парень",
        "btn_female":        "Я девушка",
        "btn_guys":          "Парни",
        "btn_girls":         "Девушки",
        "btn_anyone":        "Все равно",
        "btn_skip":          "Пропустить",
        "btn_done":          "Готово ✅",
        "btn_yes":           "Да",
        "btn_edit":          "Изменить анкету",
        "btn_change_lang":   "Изменить язык",
        "btn_back":          "Назад",
        "btn_2d":            "2 дня • ⭐ 150",
        "btn_10d":           "10 дней • ⭐ 350",
        "btn_30d":           "30 дней • ⭐ 500",
        "btn_90d":           "90 дней • ⭐ 1000",
        "gender_male_word":  "парень",
        "gender_female_word": "девушка",
    },
    "uk": {
        "welcome":           "Я допоможу знайти тобі пару або просто друзів.\nМожна я задам пару питань?",
        "welcome_back":      "З поверненням! Ось твоя анкета:",
        "menu_prompt":       "Дивись анкети або зміни свою 👇",
        "ask_age":           "Скільки тобі років?",
        "ask_gender":        "Тепер визначимось зі статтю",
        "ask_looking_for":   "Хто тебе цікавить?",
        "ask_city":          "З якого ти міста?",
        "ask_name":          "Як мені тебе називати?",
        "ask_description":   "Розкажи про себе і кого хочеш знайти, що пропонуєш.\nЦе допоможе краще підібрати тобі компанію.\n\nМожна пропустити 👇",
        "ask_photo":         "Тепер надішли фото, відео або запиши кружечок.\nМожна до 3 штук 👇",
        "profile_preview":   "Ось так виглядає твоя анкета:",
        "confirm_prompt":    "Все вірно?",
        "profile_saved":     "Анкету збережено! 🎉",
        "refill_start":      "Почнемо знову! Скільки тобі років?",
        "no_profile":        "У тебе немає анкети",
        "liked_one":         "Тебе лайкнув(ла) {who}! Подивишся?",
        "liked_many":        "Тебе лайкнули {count} разів! Подивишся?",
        "no_profiles":       "Анкети закінчились 😴",
        "match":             "Супер! Сподіваюсь, гарно проведете час 🙌\nПочинай спілкуватися 👉 {link}",
        "liked_notif_one":   "Тебе лайкнув(ла) {who}!",
        "liked_notif_many":  "Тебе лайкнули вже {count} разів!",
        "notif_msg":         "\n\nПовідомлення: {msg}",
        "envelope_prompt":   "Напиши повідомлення для {name}.\nВідправиться разом з лайком 💌",
        "envelope_text_only": "Напиши текстове повідомлення",
        "stop_viewing":      "Дивись анкети або зміни свою 👇",
        "settings_prompt":   "Додаткові налаштування:",
        "choose_language":   "Обери мову інтерфейсу:",
        "language_saved":    "Мову змінено на: {lang} ✅",
        "photo_updated":     "Фото/відео оновлено! ✅",
        "text_updated":      "Текст анкети оновлено! ✅",
        "report_sent":       "Скаргу надіслано. Ми розглянемо її найближчим часом.",
        "skip_liked":        "Добре, повертаємось у меню",
        "enter_age_number":  "Введи вік числом",
        "age_range":         "Вік від 13 до 99",
        "choose_button":     "Обери кнопку",
        "enter_city":        "Введи назву міста",
        "enter_name":        "Ім'я мінімум 2 символи",
        "enter_text":        "Напиши текстом або натисни Пропустити",
        "name_too_long":      "Ім'я задовге (максимум 50 символів)",
        "text_too_long":     "Максимум 500 символів",
        "send_media":        "Надішли фото, відео або кружечок",
        "send_at_least_one": "Спочатку надішли хоча б одне фото, відео або кружечок",
        "max_media":         "Максимум 3 файли. Натисни Готово ✅",
        "media_added":       "Прийнято! Можна додати ще {n} або натисни Готово",
        "enter_new_text":    "Напиши новий текст анкети (до 999 символів):",
        "enter_new_photo":   "Надішли нове фото, відео або кружечок.\nМожна до 3 штук 👇",
        "premium_coming":    "⭐ Преміум незабаром буде доступний!",
        "premium_menu": (
            "Активуй Premium і будь у топі ✨\n\n"
            "Виділяйся серед інших:\n"
            "📈 Більше показів анкети\n"
            "🚀 Більше лайків на день\n"
            "👀 Твої лайки бачать першими\n"
            "⭐️ Твоя анкета вище за інших\n\n"
            "Обери термін Premium:"
        ),
        "premium_activated":  "✅ Premium активовано на {days} днів!\nТвій профіль тепер у топі.",
        "premium_already":    "⭐ У тебе вже є Premium до {until}!\nМожна продовжити — нові дні додадуться до поточних.\n\nОбери термін:",
        "premium_terms":      "\n\n_Оплачуючи Premium, ти приймаєш [умови покупки](http://pt.leomatchbot.com/)._",
        "daily_limit":        "На сьогодні ти вичерпав ліміт перегляду анкет (500).\nХочеш дивитись далі — купи Преміум або чекай завтра ⏳",
        "btn_browse":        "Дивитись анкети",
        "btn_my_profile":    "Моя анкета",
        "btn_refill":        "Заповнити знову",
        "btn_change_photo":  "Змінити фото/відео",
        "btn_change_text":   "Змінити текст",
        "btn_settings":      "Доп налаштування",
        "btn_premium":       "⭐ Активуй Преміум",
        "btn_male":          "Я хлопець",
        "btn_female":        "Я дівчина",
        "btn_guys":          "Хлопці",
        "btn_girls":         "Дівчата",
        "btn_anyone":        "Все одно",
        "btn_skip":          "Пропустити",
        "btn_done":          "Готово ✅",
        "btn_yes":           "Так",
        "btn_edit":          "Змінити анкету",
        "btn_change_lang":   "Змінити мову",
        "btn_back":          "Назад",
        "btn_2d":            "2 дні • ⭐ 150",
        "btn_10d":           "10 днів • ⭐ 350",
        "btn_30d":           "30 днів • ⭐ 500",
        "btn_90d":           "90 днів • ⭐ 1000",
        "gender_male_word":  "хлопець",
        "gender_female_word": "дівчина",
    },
    "en": {
        "welcome":           "I'll help you find a partner or just friends.\nMay I ask a couple of questions?",
        "welcome_back":      "Welcome back! Here's your profile:",
        "menu_prompt":       "Browse profiles or update yours 👇",
        "ask_age":           "How old are you?",
        "ask_gender":        "Let's figure out your gender",
        "ask_looking_for":   "Who are you interested in?",
        "ask_city":          "What city are you from?",
        "ask_name":          "What should I call you?",
        "ask_description":   "Tell me about yourself and who you're looking for.\nThis will help find better matches.\n\nYou can skip 👇",
        "ask_photo":         "Now send a photo, video or record a circle.\nUp to 3 files 👇",
        "profile_preview":   "Here's how your profile looks:",
        "confirm_prompt":    "Is everything correct?",
        "profile_saved":     "Profile saved! 🎉",
        "refill_start":      "Let's start over! How old are you?",
        "no_profile":        "You don't have a profile",
        "liked_one":         "A {who} liked you! Want to see?",
        "liked_many":        "You've been liked {count} times! Want to see?",
        "no_profiles":       "No more profiles 😴",
        "match":             "Awesome! Hope you have a great time 🙌\nStart chatting 👉 {link}",
        "liked_notif_one":   "A {who} liked you!",
        "liked_notif_many":  "You've been liked {count} times!",
        "notif_msg":         "\n\nMessage: {msg}",
        "envelope_prompt":   "Write a message for {name}.\nIt will be sent with your like 💌",
        "envelope_text_only": "Please write a text message",
        "stop_viewing":      "Browse profiles or update yours 👇",
        "settings_prompt":   "Additional settings:",
        "choose_language":   "Choose interface language:",
        "language_saved":    "Language changed to: {lang} ✅",
        "photo_updated":     "Photo/video updated! ✅",
        "text_updated":      "Profile text updated! ✅",
        "report_sent":       "Report sent. We'll review it shortly.",
        "skip_liked":        "OK, going back to menu",
        "enter_age_number":  "Please enter your age as a number",
        "age_range":         "Age must be between 13 and 99",
        "choose_button":     "Please choose a button",
        "enter_city":        "Please enter your city name",
        "enter_name":        "Name must be at least 2 characters",
        "enter_text":        "Write some text or press Skip",
        "name_too_long":      "Name is too long (50 characters max)",
        "text_too_long":     "Maximum 500 characters",
        "send_media":        "Send a photo, video or circle",
        "send_at_least_one": "Please send at least one photo, video or circle first",
        "max_media":         "Maximum 3 files. Press Done ✅",
        "media_added":       "Got it! You can add {n} more or press Done",
        "enter_new_text":    "Write new profile text (up to 999 chars):",
        "enter_new_photo":   "Send new photo, video or circle.\nUp to 3 files 👇",
        "premium_coming":    "⭐ Premium coming soon!",
        "premium_menu": (
            "Activate Premium and be on top ✨\n\n"
            "Stand out from others:\n"
            "📈 More profile views\n"
            "🚀 More daily likes\n"
            "👀 Your likes are seen first\n"
            "⭐️ Your profile ranks above others\n\n"
            "Choose Premium duration:"
        ),
        "premium_activated":  "✅ Premium activated for {days} days!\nYour profile is now on top.",
        "premium_already":    "⭐ You already have Premium until {until}!\nYou can extend it — new days add to your current plan.\n\nChoose duration:",
        "premium_terms":      "\n\n_By purchasing Premium, you accept the [terms of purchase](http://pt.leomatchbot.com/)._",
        "daily_limit":        "You've reached today's profile viewing limit (500).\nGet Premium to continue or wait until tomorrow ⏳",
        "btn_browse":        "Browse profiles",
        "btn_my_profile":    "My profile",
        "btn_refill":        "Refill profile",
        "btn_change_photo":  "Change photo/video",
        "btn_change_text":   "Change text",
        "btn_settings":      "Settings",
        "btn_premium":       "⭐ Activate Premium",
        "btn_male":          "I'm a boy",
        "btn_female":        "I'm a girl",
        "btn_guys":          "Guys",
        "btn_girls":         "Girls",
        "btn_anyone":        "Doesn't matter",
        "btn_skip":          "Skip",
        "btn_done":          "Done ✅",
        "btn_yes":           "Yes",
        "btn_edit":          "Edit profile",
        "btn_change_lang":   "Change language",
        "btn_back":          "Back",
        "btn_2d":            "2 days • ⭐ 150",
        "btn_10d":           "10 days • ⭐ 350",
        "btn_30d":           "30 days • ⭐ 500",
        "btn_90d":           "90 days • ⭐ 1000",
        "gender_male_word":  "guy",
        "gender_female_word": "girl",
    },
}


def t(key: str, lang: str) -> str:
    return STRINGS.get(lang, STRINGS["ru"]).get(key, STRINGS["ru"].get(key, key))


def _all(key: str) -> set[str]:
    return {STRINGS[l][key] for l in STRINGS}


# Множества всех вариантов кнопок для фильтров
ALL_BROWSE        = _all("btn_browse")
ALL_MY_PROFILE    = _all("btn_my_profile")
ALL_REFILL        = _all("btn_refill")
ALL_CHANGE_PHOTO  = _all("btn_change_photo")
ALL_CHANGE_TEXT   = _all("btn_change_text")
ALL_SETTINGS      = _all("btn_settings")
ALL_PREMIUM       = _all("btn_premium")
ALL_MALE          = _all("btn_male")
ALL_FEMALE        = _all("btn_female")
ALL_GUYS          = _all("btn_guys")
ALL_GIRLS         = _all("btn_girls")
ALL_ANYONE        = _all("btn_anyone")
ALL_SKIP          = _all("btn_skip")
ALL_DONE          = _all("btn_done")
ALL_YES           = _all("btn_yes")
ALL_EDIT          = _all("btn_edit")
ALL_CHANGE_LANG   = _all("btn_change_lang")
ALL_BACK          = _all("btn_back")
ALL_2D            = _all("btn_2d")
ALL_10D           = _all("btn_10d")
ALL_30D           = _all("btn_30d")
ALL_90D           = _all("btn_90d")
ALL_PREMIUM_DURATIONS = ALL_2D | ALL_10D | ALL_30D | ALL_90D

# Маппинг любого варианта кнопки → внутреннее значение
GENDER_MAP    = {v: "мужской" for v in ALL_MALE}   | {v: "женский" for v in ALL_FEMALE}
LOOKING_MAP   = {v: "мужской" for v in ALL_GUYS}   | {v: "женский" for v in ALL_GIRLS} | {v: "все" for v in ALL_ANYONE}

# Маппинг кнопок длительности → (дни, звёзды)
DURATION_MAP  = {v: (2, 150)   for v in ALL_2D}   | \
                {v: (10, 350)  for v in ALL_10D}  | \
                {v: (30, 500)  for v in ALL_30D}  | \
                {v: (90, 1000) for v in ALL_90D}

# Кнопки смены языка всегда на своём языке, не переводятся
LANGUAGE_BUTTONS = {"Українська": "uk", "Русский": "ru", "English": "en"}

SAFETY_TIPS: dict[str, list[str]] = {
    "ru": [
        "⚠️ Осторожно! Не отправляй деньги незнакомцам — ни под каким предлогом. Мошенники часто придумывают убедительные истории.",
        "🔒 Никогда не отправляй интимные фото или видео людям, с которыми познакомился онлайн. Это может использоваться против тебя.",
        "📍 Не сообщай домашний адрес малознакомым людям. Первые встречи — только в публичных местах.",
        "🚨 Если кто-то давит, угрожает или требует деньги — это мошенник. Жми «Пожаловаться» и блокируй без раздумий.",
        "💬 Будь осторожен: если человек слишком быстро признаётся в любви или просит перейти в другой мессенджер — скорее всего, это развод.",
    ],
    "uk": [
        "⚠️ Обережно! Не надсилай гроші незнайомцям — ні під яким приводом. Шахраї часто вигадують переконливі історії.",
        "🔒 Ніколи не надсилай інтимні фото чи відео людям, з якими познайомився онлайн. Це може бути використано проти тебе.",
        "📍 Не повідомляй домашню адресу малознайомим людям. Перші зустрічі — лише в публічних місцях.",
        "🚨 Якщо хтось тисне, погрожує або вимагає гроші — це шахрай. Натискай «Поскаржитись» і блокуй без роздумів.",
        "💬 Будь обережний: якщо людина дуже швидко зізнається в коханні або просить перейти в інший месенджер — швидше за все, це розвод.",
    ],
    "en": [
        "⚠️ Warning! Never send money to strangers online — no matter their story. Scammers are very convincing.",
        "🔒 Never send intimate photos or videos to people you've just met online. It can be used against you.",
        "📍 Don't share your home address with people you barely know. First meetings should always be in public places.",
        "🚨 If someone pressures you, makes threats, or asks for money — that's a scammer. Report and block immediately.",
        "💬 Be careful: if someone confesses love very quickly or asks you to move to another app — it's likely a scam.",
    ],
}

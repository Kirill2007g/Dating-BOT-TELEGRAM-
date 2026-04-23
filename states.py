from aiogram.fsm.state import State, StatesGroup


class StartRegistration(StatesGroup):
    age = State()
    gender = State()
    looking_for = State()
    city = State()
    name = State()
    description = State()
    photo = State()
    confirm = State()


class ProfileMenu(StatesGroup):
    new_photo = State()
    new_description = State()
    settings = State()
    language = State()


class Viewing(StatesGroup):
    viewing = State()
    liked_me = State()
    sending_message = State()


class Premium(StatesGroup):
    choosing = State()

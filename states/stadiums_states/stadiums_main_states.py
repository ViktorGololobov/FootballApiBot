from telebot.handler_backends import State, StatesGroup


class StadiumStates(StatesGroup):
    all_stadiums = State()
    one_stadium = State()

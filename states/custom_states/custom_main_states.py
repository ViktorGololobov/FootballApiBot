from telebot.handler_backends import State, StatesGroup


class CustomStatMainState(StatesGroup):
    """ Класс основных состояний пользователя в рамках команды custom_champ. """

    goals = State()
    wins = State()
    draws = State()
    loses = State()
    points = State()


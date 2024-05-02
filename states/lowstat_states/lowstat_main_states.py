from telebot.handler_backends import State, StatesGroup


class LowStatMainState(StatesGroup):
    """ Класс основных состояний пользователя в рамках команды lowstat_champ. """

    goals = State()
    wins = State()
    draws = State()
    loses = State()
    points = State()


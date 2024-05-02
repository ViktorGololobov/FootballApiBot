from telebot.handler_backends import State, StatesGroup


class HighStatMainState(StatesGroup):
    """ Класс основных состояний пользователя в рамках команды highstat_champ. """

    goals = State()
    wins = State()
    draws = State()
    loses = State()
    points = State()


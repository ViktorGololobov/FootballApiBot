from telebot.handler_backends import State, StatesGroup


class HighWinsStat(StatesGroup):
    """ Класс состояний пользователя в рамках команды highstat_champ по победам. """

    all_wins = State()
    home_wins = State()
    away_wins = State()

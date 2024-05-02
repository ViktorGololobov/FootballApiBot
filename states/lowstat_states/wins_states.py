from telebot.handler_backends import State, StatesGroup


class LowWinsStat(StatesGroup):
    """ Класс состояний пользователя в рамках команды lowstat_champ по победам. """

    all_wins = State()
    home_wins = State()
    away_wins = State()

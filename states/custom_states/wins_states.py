from telebot.handler_backends import State, StatesGroup


class CustomWinsStat(StatesGroup):
    """ Класс состояний пользователя в рамках команды custom_champ по победам. """

    all_wins = State()
    home_wins = State()
    away_wins = State()

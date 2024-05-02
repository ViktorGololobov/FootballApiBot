from telebot.handler_backends import State, StatesGroup


class LowLosesStat(StatesGroup):
    """ Класс состояний пользователя в рамках команды lowstat_champ по поражениям. """

    all_loses = State()
    home_loses = State()
    away_loses = State()

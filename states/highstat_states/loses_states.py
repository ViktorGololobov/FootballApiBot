from telebot.handler_backends import State, StatesGroup


class HighLosesStat(StatesGroup):
    """ Класс состояний пользователя в рамках команды highstat_champ по поражениям. """

    all_loses = State()
    home_loses = State()
    away_loses = State()

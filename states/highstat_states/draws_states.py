from telebot.handler_backends import State, StatesGroup


class HighDrawsStat(StatesGroup):
    """ Класс состояний пользователя в рамках команды highstat_champ по ничьим. """

    all_draws = State()
    home_draws = State()
    away_draws = State()

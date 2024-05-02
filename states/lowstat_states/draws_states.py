from telebot.handler_backends import State, StatesGroup


class LowDrawsStat(StatesGroup):
    """ Класс состояний пользователя в рамках команды lowstat_champ по ничьим. """

    all_draws = State()
    home_draws = State()
    away_draws = State()

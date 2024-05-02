from telebot.handler_backends import State, StatesGroup


class CustomDrawsStat(StatesGroup):
    """ Класс состояний пользователя в рамках команды custom_champ по ничьим. """

    all_draws = State()
    home_draws = State()
    away_draws = State()

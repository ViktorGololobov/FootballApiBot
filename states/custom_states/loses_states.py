from telebot.handler_backends import State, StatesGroup


class CustomLosesStat(StatesGroup):
    """ Класс состояний пользователя в рамках команды custom_champ по поражениям. """

    all_loses = State()
    home_loses = State()
    away_loses = State()

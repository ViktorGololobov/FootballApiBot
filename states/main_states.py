from telebot.handler_backends import State, StatesGroup


class UserMainCommandInfo(StatesGroup):
    """ Класс основных состояний пользователя, согласно командам бота. """

    lowstat = State()
    highstat = State()
    custom = State()
    stadiums = State()
    all_champ_statistics = State()
    history = State()

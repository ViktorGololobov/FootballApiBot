from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    """ Состояния запросов. """
    new_task = State()

from telebot.handler_backends import State, StatesGroup


class CustomStatGoals(StatesGroup):
    """ Класс состояний пользователя в рамках команды custom_champ по голам. """

    all_goals = State()
    home_goals = State()
    away_goals = State()


class CustomStatGoalsForAgainst(StatesGroup):
    """ Класс состояний пользователя по забитым и пропущенным голам. """

    goals_for = State()
    goals_against = State()

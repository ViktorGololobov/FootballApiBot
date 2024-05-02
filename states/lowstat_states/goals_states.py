from telebot.handler_backends import State, StatesGroup


class LowStatGoals(StatesGroup):
    """ Класс состояний пользователя в рамках команды lowstat_champ по голам. """

    all_goals = State()
    home_goals = State()
    away_goals = State()


class LowStatGoalsForAgainst(StatesGroup):
    """ Класс состояний пользователя по забитым и пропущенным голам. """

    goals_for = State()
    goals_against = State()

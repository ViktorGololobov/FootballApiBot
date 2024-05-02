from loader import bot
from telebot.types import CallbackQuery
from states.highstat_states.goals_states import HighStatGoals, HighStatGoalsForAgainst
from api.football_api import api_request
from keyboards.inline.highstat_buttons.main_buttons import all_home_away_buttons_gen
from states.highstat_states.highstat_main_states import HighStatMainState
from collections.abc import Iterable
from typing import List, Dict


method_endswith = '/v3/standings'

params: Dict[str, int] = {
    'league': 140,
    'season': 2023
}

method_type = 'GET'

result_list: List[str] = ['all', 'home', 'away']
for_against: List[str] = ['for', 'against']


@bot.callback_query_handler(func=lambda call: True, state=HighStatGoals.all_goals)
def goals_show(call: CallbackQuery) -> None:
    """
    Хэндлер для запуска процесса отображения информации на экран пользователя по всем голам. Декоратор ловит
    состояние пользователя state и запускает функцию goals_show, которая в свою очередь запускает функцию goals_print
    для получения и отправки информации о голах пользователю.

    :param call: обратный вызов кнопки
    """

    global method_endswith
    global params
    global method_type

    if call.data == 'goals_for':
        bot.set_state(call.message.chat.id, HighStatGoalsForAgainst.goals_for, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех забито голов:', call.message.chat.id, call.message.message_id
        )
        goals_for = goals_stat(result_list[0], for_against[0], method_endswith, params, method_type)
        goals_print(goals_for, call)
    elif call.data == 'goals_against':
        bot.set_state(call.message.chat.id, HighStatGoalsForAgainst.goals_against, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех пропущено голов:', call.message.chat.id, call.message.message_id
        )
        goals_against = goals_stat(result_list[0], for_against[1], method_endswith, params, method_type)
        goals_print(goals_against, call)
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, HighStatMainState.goals, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в предыдущее меню. Вам нужны голы дома, на выезде или общее количество? ',
            call.message.chat.id, call.message.message_id, reply_markup=all_home_away_buttons_gen()
        )


@bot.callback_query_handler(func=lambda call: True, state=HighStatGoals.home_goals)
def goals_show(call: CallbackQuery) -> None:
    """
    Хэндлер для запуска процесса отображения информации на экран пользователя по голам дома. Декоратор ловит
    состояние пользователя state и запускает функцию goals_show, которая в свою очередь запускает функцию goals_print
    для получения и отправки информации о голах пользователю.

    :param call: обратный вызов кнопки
    """

    global method_endswith
    global params
    global method_type

    if call.data == 'goals_for':
        bot.set_state(call.message.chat.id, HighStatGoalsForAgainst.goals_for, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех забито голов дома:', call.message.chat.id, call.message.message_id
        )
        goals_for = goals_stat(result_list[1], for_against[0], method_endswith, params, method_type)
        goals_print(goals_for, call)

    elif call.data == 'goals_against':
        bot.set_state(call.message.chat.id, HighStatGoalsForAgainst.goals_against, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех пропущено голов дома:', call.message.chat.id, call.message.message_id
        )
        goals_against = goals_stat(result_list[1], for_against[1], method_endswith, params, method_type)
        goals_print(goals_against, call)
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, HighStatMainState.goals, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в предыдущее меню. Вам нужны голы дома, на выезде или общее количество? ',
            call.message.chat.id, call.message.message_id, reply_markup=all_home_away_buttons_gen()
        )


@bot.callback_query_handler(func=lambda call: True, state=HighStatGoals.away_goals)
def goals_show(call: CallbackQuery) -> None:
    """
    Хэндлер для запуска процесса отображения информации на экран пользователя по голам на выезде. Декоратор
    ловит состояние пользователя state и запускает функцию goals_show, которая в свою очередь запускает функцию
    goals_print для получения и отправки информации о голах пользователю.

    :param call: обратный вызов кнопки
    """

    global method_endswith
    global params
    global method_type

    if call.data == 'goals_for':
        bot.set_state(call.message.chat.id, HighStatGoalsForAgainst.goals_for, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех забито голов на выезде:', call.message.chat.id, call.message.message_id
        )
        goals_for = goals_stat(result_list[2], for_against[0], method_endswith, params, method_type)
        goals_print(goals_for, call)
    elif call.data == 'goals_against':
        bot.set_state(call.message.chat.id, HighStatGoalsForAgainst.goals_against, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех пропущено голов на выезде:', call.message.chat.id, call.message.message_id
        )
        goals_against = goals_stat(result_list[2], for_against[1], method_endswith, params, method_type)
        goals_print(goals_against, call)
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, HighStatMainState.goals, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в предыдущее меню. Вам нужны голы дома, на выезде или общее количество? ',
            call.message.chat.id, call.message.message_id, reply_markup=all_home_away_buttons_gen()
        )


def goals_stat(result: str, goals_param: str, api_endswith: str, parameters: Dict, api_method_type: str) -> \
        Iterable[str]:
    """
    Функция-генератор для получения количества голов. На вход получает параметр, где нужно смотреть голы (все, дома или
    на выезде) и возвращает их.

    :param result: параметр для поиска голов дома, на выезде или всего
    :param goals_param: параметр для поиска голов по забитым или пропущеннным
    :param api_endswith: запрос
    :param parameters: параметры запроса
    :param api_method_type: тип запроса
    :return: key, value
    :rtype: Iterable[str]
    """

    response = api_request(api_endswith, parameters, api_method_type)
    team_name = response['response'][0]['league']['standings'][0]
    goals = 0
    team_dict = dict()

    for counter in range(20):
        for point in team_name[counter][result]:
            if point == 'goals' and counter == 0:
                goals = team_name[counter][result][point][goals_param]
                team = team_name[counter]['team']['name']
                team_dict[team] = goals
                continue

            if point == 'goals' and goals <= team_name[counter][result][point][goals_param]:
                goals = team_name[counter][result][point][goals_param]
                team = team_name[counter]['team']['name']
                team_dict[team] = goals

    maximum = max(team_dict.values())

    for key, value in team_dict.items():
        if maximum == value:
            yield f'Команда: {key}\n'\
                  f'Голы: {value}'


def goals_print(goals_data: Iterable[str], call: CallbackQuery) -> None:
    """
    Функция для отправки сообщений пользователю с информацией о голах.

    :param goals_data: данные о голах (команда и количество голов)
    :param call: обратный вызов кнопки
    """

    for goal in goals_data:
        bot.send_message(call.message.chat.id, goal)

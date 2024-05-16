from loader import bot
from telebot.types import CallbackQuery
from states.highstat_states.goals_states import HighStatGoals, HighStatGoalsForAgainst
from api.football_api import api_request
from keyboards.inline.highstat_buttons.main_buttons import all_home_away_buttons_gen
from states.highstat_states.highstat_main_states import HighStatMainState
from handlers.custom_handlers.print_info import print_info
from collections.abc import Iterable
from typing import List
from api.api_params import methods_endswith_list, params_dict
from database.new_enquiry import add_new_enquiry

command = '/highstat_champ'

method_endswith = methods_endswith_list[0]
params = params_dict['standings_and_all_stadiums']
result_list: List[str] = ['all', 'home', 'away']
for_against: List[str] = ['for', 'against']


@bot.callback_query_handler(func=lambda call: True, state=HighStatGoals.all_goals)
def goals_call(call: CallbackQuery) -> None:
    """
    Хэндлер для запуска процесса отображения информации на экран пользователя по всем голам. Декоратор ловит
    состояние пользователя state и запускает функцию goals_call, которая в свою очередь запускает функцию goals_print
    для получения и отправки информации о голах пользователю.

    :param call: обратный вызов кнопки
    """

    global command

    if call.data == 'goals_for':
        bot.set_state(call.message.chat.id, HighStatGoalsForAgainst.goals_for, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех забито голов:', call.message.chat.id, call.message.message_id
        )
        goals_for = goals_stat(result_list[0], for_against[0])
        add_new_enquiry(call.message, command)
        print_info(goals_for, call.message)
    elif call.data == 'goals_against':
        bot.set_state(call.message.chat.id, HighStatGoalsForAgainst.goals_against, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех пропущено голов:', call.message.chat.id, call.message.message_id
        )
        goals_against = goals_stat(result_list[0], for_against[1])
        add_new_enquiry(call.message, command)
        print_info(goals_against, call.message)
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, HighStatMainState.goals, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в предыдущее меню. Вам нужны голы дома, на выезде или общее количество? ',
            call.message.chat.id, call.message.message_id, reply_markup=all_home_away_buttons_gen()
        )


@bot.callback_query_handler(func=lambda call: True, state=HighStatGoals.home_goals)
def goals_call(call: CallbackQuery) -> None:
    """
    Хэндлер для запуска процесса отображения информации на экран пользователя по голам дома. Декоратор ловит
    состояние пользователя state и запускает функцию goals_call, которая в свою очередь запускает функцию goals_print
    для получения и отправки информации о голах пользователю.

    :param call: обратный вызов кнопки
    """

    global command

    if call.data == 'goals_for':
        bot.set_state(call.message.chat.id, HighStatGoalsForAgainst.goals_for, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех забито голов дома:', call.message.chat.id, call.message.message_id
        )
        goals_for = goals_stat(result_list[1], for_against[0])
        add_new_enquiry(call.message, command)
        print_info(goals_for, call.message)

    elif call.data == 'goals_against':
        bot.set_state(call.message.chat.id, HighStatGoalsForAgainst.goals_against, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех пропущено голов дома:', call.message.chat.id, call.message.message_id
        )
        goals_against = goals_stat(result_list[1], for_against[1])
        add_new_enquiry(call.message, command)
        print_info(goals_against, call.message)
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, HighStatMainState.goals, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в предыдущее меню. Вам нужны голы дома, на выезде или общее количество? ',
            call.message.chat.id, call.message.message_id, reply_markup=all_home_away_buttons_gen()
        )


@bot.callback_query_handler(func=lambda call: True, state=HighStatGoals.away_goals)
def goals_call(call: CallbackQuery) -> None:
    """
    Хэндлер для запуска процесса отображения информации на экран пользователя по голам на выезде. Декоратор
    ловит состояние пользователя state и запускает функцию goals_call, которая в свою очередь запускает функцию
    goals_print для получения и отправки информации о голах пользователю.

    :param call: обратный вызов кнопки
    """

    global command

    if call.data == 'goals_for':
        bot.set_state(call.message.chat.id, HighStatGoalsForAgainst.goals_for, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех забито голов на выезде:', call.message.chat.id, call.message.message_id
        )
        goals_for = goals_stat(result_list[2], for_against[0])
        add_new_enquiry(call.message, command)
        print_info(goals_for, call.message)
    elif call.data == 'goals_against':
        bot.set_state(call.message.chat.id, HighStatGoalsForAgainst.goals_against, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех пропущено голов на выезде:', call.message.chat.id, call.message.message_id
        )
        goals_against = goals_stat(result_list[2], for_against[1])
        add_new_enquiry(call.message, command)
        print_info(goals_against, call.message)
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, HighStatMainState.goals, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в предыдущее меню. Вам нужны голы дома, на выезде или общее количество? ',
            call.message.chat.id, call.message.message_id, reply_markup=all_home_away_buttons_gen()
        )


def goals_stat(result: str, goals_param: str) -> Iterable[str]:
    """
    Функция-генератор для получения количества голов. На вход получает параметр, где нужно смотреть голы (все, дома или
    на выезде) и возвращает их.

    :param result: параметр для поиска голов дома, на выезде или всего
    :param goals_param: параметр для поиска голов по забитым или пропущеннным
    :return: key, value
    :rtype: Iterable[str]
    """

    global method_endswith
    global params

    response = api_request(method_endswith, params)
    team_name = response['response'][0]['league']['standings'][0]
    goals = 0
    team_dict = dict()
    teams = 20

    for counter in range(teams):
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

from loader import bot
from telebot.types import CallbackQuery
from api.football_api import api_request
from states.lowstat_states.lowstat_main_states import LowStatMainState
from states.lowstat_states.wins_states import LowWinsStat
from states.main_states import UserMainCommandInfo
from keyboards.inline.lowstat_buttons.main_buttons import button_generator_for_back
from handlers.custom_handlers.print_info import print_info
from collections.abc import Iterable
from typing import List
from api.api_params import methods_endswith_list, params_dict
from database.new_enquiry import add_new_enquiry


command = '/lowstat_champ'

method_endswith = methods_endswith_list[0]
params = params_dict['standings_and_all_stadiums']
result_list: List[str] = ['all', 'home', 'away']


@bot.callback_query_handler(func=lambda call: True, state=LowStatMainState.wins)
def wins_call(call: CallbackQuery) -> None:
    """
    Хэндлер для запуска процесса отображения информации на экран пользователя. Декоратор ловит состояние
    пользователя state и запускает функцию wins_call, которая в свою очередь запускает функцию wins_print для
    получения и отправки информации о победах пользователю.

    :param call: обратный вызов кнопки
    """

    global command

    if call.data == 'all_info':
        bot.set_state(call.message.chat.id, LowWinsStat.all_wins, call.message.chat.id)
        bot.edit_message_text(
            f'Меньше всех побед:', call.message.chat.id, call.message.message_id
        )
        wins_info = wins_stat(result_list[0])
        add_new_enquiry(call.message, command)
        print_info(wins_info, call.message)
    elif call.data == 'home':
        bot.set_state(call.message.chat.id, LowWinsStat.home_wins, call.message.chat.id)
        bot.edit_message_text(
            f'Меньше всех побед дома:', call.message.chat.id, call.message.message_id
        )
        wins_info = wins_stat(result_list[1])
        add_new_enquiry(call.message, command)
        print_info(wins_info, call.message)
    elif call.data == 'away':
        bot.set_state(call.message.chat.id, LowWinsStat.away_wins, call.message.chat.id)
        bot.edit_message_text(
            f'Меньше всех побед на выезде:', call.message.chat.id, call.message.message_id
        )
        wins_info = wins_stat(result_list[2])
        add_new_enquiry(call.message, command)
        print_info(wins_info, call.message)
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, UserMainCommandInfo.lowstat, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в главное меню. Какой показатель интересует? ', call.message.chat.id,
            call.message.message_id, reply_markup=button_generator_for_back()
        )


def wins_stat(result: str) -> Iterable[str]:
    """
    Функция-генератор для получения количества побед. На вход получает параметр, где нужно смотреть победы (все, дома или
    на выезде) и возвращает их.

    :param result: параметр для поиска побед
    :return: key, value
    :rtype: Iterable[str]
    """

    global method_endswith
    global params

    response = api_request(method_endswith, params)
    team_name = response['response'][0]['league']['standings'][0]
    wins = 0
    team_dict = dict()
    teams = 20

    for counter in range(teams):
        for point in team_name[counter][result]:
            if point == 'win' and counter == 0:
                wins = team_name[counter][result][point]
                team = team_name[counter]['team']['name']
                team_dict[team] = wins
                continue

            if point == 'win' and wins >= team_name[counter][result][point]:
                wins = team_name[counter][result][point]
                team = team_name[counter]['team']['name']
                team_dict[team] = wins

    minimum = min(team_dict.values())

    for key, value in team_dict.items():
        if minimum == value:
            yield f'Команда: {key}\n' \
                  f'Победы: {value}'

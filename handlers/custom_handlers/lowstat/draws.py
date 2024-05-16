from loader import bot
from telebot.types import CallbackQuery
from api.football_api import api_request
from states.lowstat_states.lowstat_main_states import LowStatMainState
from states.lowstat_states.draws_states import LowDrawsStat
from states.main_states import UserMainCommandInfo
from keyboards.inline.lowstat_buttons.main_buttons import button_generator_for_back
from handlers.custom_handlers.print_info import print_info
from api.api_params import methods_endswith_list, params_dict
from collections.abc import Iterable
from typing import List
from database.new_enquiry import add_new_enquiry


command = '/lowstat_champ'

method_endswith = methods_endswith_list[0]
params = params_dict['standings_and_all_stadiums']
result_list: List[str] = ['all', 'home', 'away']


@bot.callback_query_handler(func=lambda call: True, state=LowStatMainState.draws)
def draws_call(call: CallbackQuery) -> None:
    """
    Хэндлер для запуска процесса отображения информации на экран пользователя. Декоратор ловит состояние
    пользователя state и запускает функцию draws_call, которая в свою очередь запускает функцию draws_print для
    получения и отправки информации о ничьих пользователю.

    :param call: обратный вызов кнопки
    """

    global result_list
    global command

    if call.data == 'all_info':
        bot.set_state(call.message.chat.id, LowDrawsStat.all_draws, call.message.chat.id)
        bot.edit_message_text(
            f'Меньше всех ничьих:', call.message.chat.id, call.message.message_id
        )
        draws_info = draws_stat(result_list[0])
        add_new_enquiry(call.message, command)
        print_info(draws_info, call.message)
    elif call.data == 'home':
        bot.set_state(call.message.chat.id, LowDrawsStat.home_draws, call.message.chat.id)
        bot.edit_message_text(
            f'Меньше всех ничьих дома:', call.message.chat.id, call.message.message_id
        )
        draws_info = draws_stat(result_list[1])
        add_new_enquiry(call.message, command)
        print_info(draws_info, call.message)
    elif call.data == 'away':
        bot.set_state(call.message.chat.id, LowDrawsStat.away_draws, call.message.chat.id)
        bot.edit_message_text(
            f'Меньше всех ничьих на выезде:', call.message.chat.id, call.message.message_id
        )
        draws_info = draws_stat(result_list[2])
        add_new_enquiry(call.message, command)
        print_info(draws_info, call.message)
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, UserMainCommandInfo.lowstat, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в главное меню. Какой показатель интересует? ', call.message.chat.id,
            call.message.message_id, reply_markup=button_generator_for_back()
        )


def draws_stat(result: str) -> Iterable[str]:
    """
    Функция-генератор для получения количества ничьих. На вход получает параметр, где нужно смотреть ничьи (все, дома
    или на выезде) и возвращает их.

    :param result: параметр для поиска ничьих
    :return: key, value
    :rtype: Iterable[str]
    """

    global method_endswith
    global params

    response = api_request(method_endswith, params)
    team_name = response['response'][0]['league']['standings'][0]
    draws = 0
    team_dict = dict()
    teams = 20

    for counter in range(teams):
        for point in team_name[counter][result]:
            if point == 'draw' and counter == 0:
                draws = team_name[counter][result][point]
                team = team_name[counter]['team']['name']
                team_dict[team] = draws
                continue

            if point == 'draw' and draws >= team_name[counter][result][point]:
                draws = team_name[counter][result][point]
                team = team_name[counter]['team']['name']
                team_dict[team] = draws

    minimum = min(team_dict.values())

    for key, value in team_dict.items():
        if minimum == value:
            yield f'Команда: {key}\n'\
                  f'Ничьи: {value}'

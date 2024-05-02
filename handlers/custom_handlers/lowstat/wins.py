from loader import bot
from telebot.types import CallbackQuery
from api.football_api import api_request
from states.lowstat_states.lowstat_main_states import LowStatMainState
from states.lowstat_states.wins_states import LowWinsStat
from states.main_states import UserMainCommandInfo
from keyboards.inline.lowstat_buttons.main_buttons import button_generator_for_back
from collections.abc import Iterable
from typing import Dict, List

method_endswith = '/v3/standings'

params: Dict[str, int] = {
    'league': 140,
    'season': 2023
}

method_type = 'GET'

result_list: List[str] = ['all', 'home', 'away']


@bot.callback_query_handler(func=lambda call: True, state=LowStatMainState.wins)
def wins_call(call: CallbackQuery) -> None:
    """
    Хэндлер для запуска процесса отображения информации на экран пользователя. Декоратор ловит состояние
    пользователя state и запускает функцию wins_call, которая в свою очередь запускает функцию wins_print для
    получения и отправки информации о победах пользователю.

    :param call: обратный вызов кнопки
    """

    global method_endswith
    global params
    global method_type

    if call.data == 'all_info':
        bot.set_state(call.message.chat.id, LowWinsStat.all_wins, call.message.chat.id)
        bot.edit_message_text(
            f'Меньше всех побед:', call.message.chat.id, call.message.message_id
        )
        wins_info = wins_stat(result_list[0], method_endswith, params, method_type)
        wins_print(wins_info, call)
    elif call.data == 'home':
        bot.set_state(call.message.chat.id, LowWinsStat.home_wins, call.message.chat.id)
        bot.edit_message_text(
            f'Меньше всех побед дома:', call.message.chat.id, call.message.message_id
        )
        wins_info = wins_stat(result_list[1], method_endswith, params, method_type)
        wins_print(wins_info, call)
    elif call.data == 'away':
        bot.set_state(call.message.chat.id, LowWinsStat.away_wins, call.message.chat.id)
        bot.edit_message_text(
            f'Меньше всех побед на выезде:', call.message.chat.id, call.message.message_id
        )
        wins_info = wins_stat(result_list[2], method_endswith, params, method_type)
        wins_print(wins_info, call)
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, UserMainCommandInfo.lowstat, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в главное меню. Какой показатель интересует? ', call.message.chat.id,
            call.message.message_id, reply_markup=button_generator_for_back()
        )


def wins_stat(result: str, api_endswith: str, parameters: Dict, api_method_type: str) -> Iterable[str]:
    """
    Функция-генератор для получения количества побед. На вход получает параметр, где нужно смотреть победы (все, дома или
    на выезде) и возвращает их.

    :param result: параметр для поиска побед
    :param api_endswith: запрос
    :param parameters: параметры запроса
    :param api_method_type: тип запроса
    :return: key, value
    :rtype: Iterable[str]
    """

    response = api_request(api_endswith, parameters, api_method_type)
    team_name = response['response'][0]['league']['standings'][0]
    wins = 0
    team_dict = dict()

    for counter in range(20):
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


def wins_print(wins_data: Iterable[str], call: CallbackQuery) -> None:
    """
    Функция для отправки сообщений пользователю с информацией о победах.

    :param wins_data: данные о победах (команда и количество побед)
    :param call: обратный вызов кнопки
    """

    for win in wins_data:
        bot.send_message(call.message.chat.id, win)


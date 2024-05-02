from loader import bot
from telebot.types import CallbackQuery
from api.football_api import api_request
from states.highstat_states.highstat_main_states import HighStatMainState
from states.highstat_states.loses_states import HighLosesStat
from states.main_states import UserMainCommandInfo
from keyboards.inline.highstat_buttons.main_buttons import button_generator_for_back
from collections.abc import Iterable
from typing import List, Dict


method_endswith = '/v3/standings'

params: Dict[str, int] = {
    'league': 140,
    'season': 2023
}

method_type = 'GET'

result_list: List[str] = ['all', 'home', 'away']


@bot.callback_query_handler(func=lambda call: True, state=HighStatMainState.loses)
def loses_call(call: CallbackQuery) -> None:
    """
    Хэндлер для запуска процесса отображения информации на экран пользователя. Декоратор ловит состояние
    пользователя state и запускает функцию loses_call, которая в свою очередь запускает функцию loses_print для
    получения и отправки информации о поражениях пользователю.

    :param call: обратный вызов кнопки
    """

    global method_endswith
    global params
    global method_type

    if call.data == 'all_info':
        bot.set_state(call.message.chat.id, HighLosesStat.all_loses, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех поражений:', call.message.chat.id, call.message.message_id
        )
        loses_info = loses_stat(result_list[0], method_endswith, params, method_type)
        loses_print(loses_info, call)
    elif call.data == 'home':
        bot.set_state(call.message.chat.id, HighLosesStat.home_loses, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех поражений дома:', call.message.chat.id, call.message.message_id
        )
        loses_info = loses_stat(result_list[1], method_endswith, params, method_type)
        loses_print(loses_info, call)
    elif call.data == 'away':
        bot.set_state(call.message.chat.id, HighLosesStat.away_loses, call.message.chat.id)
        bot.edit_message_text(
            f'Больше всех поражений на выезде:', call.message.chat.id, call.message.message_id
        )
        loses_info = loses_stat(result_list[2], method_endswith, params, method_type)
        loses_print(loses_info, call)
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, UserMainCommandInfo.highstat, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в главное меню. Какой показатель интересует? ', call.message.chat.id,
            call.message.message_id, reply_markup=button_generator_for_back()
        )


def loses_stat(result: str, api_endswith: str, parameters: Dict, api_method_type: str) -> Iterable[str]:
    """
    Функция-генератор для получения количества поражений. На вход получает параметр, где нужно смотреть поражения (все,
    дома или на выезде) и возвращает их.

    :param result: параметр для поиска поражений
    :param api_endswith: запрос
    :param parameters: параметры запроса
    :param api_method_type: тип запроса
    :return: key, value
    :rtype: Iterable[str]
    """

    response = api_request(api_endswith, parameters, api_method_type)
    team_name = response['response'][0]['league']['standings'][0]
    loses = 0
    team_dict = dict()

    for counter in range(20):
        for point in team_name[counter][result]:
            if point == 'lose' and counter == 0:
                loses = team_name[counter][result][point]
                team = team_name[counter]['team']['name']
                team_dict[team] = loses
                continue

            if point == 'lose' and loses <= team_name[counter][result][point]:
                loses = team_name[counter][result][point]
                team = team_name[counter]['team']['name']
                team_dict[team] = loses

    maximum = max(team_dict.values())

    for key, value in team_dict.items():
        if maximum == value:
            yield f'Команда: {key}\n'\
                  f'Поражения: {value}'


def loses_print(loses_data: Iterable[str], call: CallbackQuery) -> None:
    """
    Функция для отправки сообщений пользователю с информацией о поражениях.

    :param loses_data: данные о поражениях (команда и количество поражений)
    :param call: обратный вызов кнопки
    """

    for lose in loses_data:
        bot.send_message(call.message.chat.id, lose)

from loader import bot
from telebot.types import CallbackQuery, Message
from api.football_api import api_request
from collections.abc import Iterable
from handlers.custom_handlers.custom.data_check import points_data_check
from typing import Dict, List


method_endswith = '/v3/standings'

params: Dict[str, int] = {
    'league': 140,
    'season': 2023
}

method_type = 'GET'


def points_show(call: CallbackQuery) -> None:
    """
    Функция для запуска процесса отображения информации на экран пользователя. Запускается функция points_print
    для получения и отправки информации об очках пользователю.

    :param call: обратный вызов кнопки
    :param api_endswith: запрос
    :param parameters: параметры запроса
    :param api_method_type: тип запроса
    """

    global method_endswith
    global params
    global method_type

    bot.edit_message_text(
        f'Введите диапазон из двух чисел через пробел для поиска по очкам команд:', call.message.chat.id,
        call.message.message_id
    )
    bot.register_next_step_handler(
        call.message, points_data_check, points_stat, points_print, method_endswith, params, method_type
    )


def points_stat(data_list: List, api_endswith: str, parameters: Dict, api_method_type: str) -> Iterable[str]:
    """
    Функция-генератор для получения количества очков.

    :param data_list: список с цифрами для диапазона
    :param api_endswith: запрос
    :param parameters: параметры запроса
    :param api_method_type: тип запроса
    :return: team, points
    :rtype: Iterable[str]
    """

    response = api_request(api_endswith, parameters, api_method_type)
    team_name = response['response'][0]['league']['standings'][0]
    is_one_in_range = False

    for counter in range(20):
        for point in team_name[counter]:

            if point == 'points' and int(data_list[0]) <= team_name[counter][point] <= int(data_list[1]):
                is_one_in_range = True
                points = team_name[counter][point]
                team = team_name[counter]['team']['name']
                yield f'Команда: {team}\n' \
                      f'Очки: {points}'

    if not is_one_in_range:
        yield f'Команд по заданному диапазону не найдено.'


def points_print(points_data: Iterable[str], call: Message) -> None:
    """
    Функция для отправки сообщений пользователю с информацией об очках.

    :param points_data: данные о поражениях (команда и количество поражений)
    :param call: обратный вызов кнопки
    """

    for points in points_data:
        bot.send_message(call.chat.id, points)


from loader import bot
from telebot.types import CallbackQuery
from api.football_api import api_request
from collections.abc import Iterable
from typing import Dict

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
    """

    global method_endswith
    global params
    global method_type

    bot.edit_message_text(
        f'Наибольшее количество очков:', call.message.chat.id, call.message.message_id
    )
    points_info = points_stat(method_endswith, params, method_type)
    points_print(points_info, call)


def points_stat(api_endswith: str, parameters: Dict, api_method_type: str) -> Iterable[str]:
    """
    Функция-генератор для получения количества очков.

    :param api_endswith: запрос
    :param parameters: параметры запроса
    :param api_method_type: тип запроса
    :return: key, value
    :rtype: Iterable[str]
    """

    response = api_request(api_endswith, parameters, api_method_type)
    team_name = response['response'][0]['league']['standings'][0]
    points = 0
    team_dict = dict()

    for counter in range(20):
        for point in team_name[counter]:
            if point == 'points' and counter == 0:
                points = team_name[counter][point]
                team = team_name[counter]['team']['name']
                team_dict[team] = points
                continue

            if point == 'points' and points <= team_name[counter][point]:
                points = team_name[counter][point]
                team = team_name[counter]['team']['name']
                team_dict[team] = points

    maximum = max(team_dict.values())

    for key, value in team_dict.items():
        if maximum == value:
            yield f'Команда: {key}\n'\
                  f'Очки: {value}'


def points_print(points_data: Iterable[str], call: CallbackQuery) -> None:
    """
    Функция для отправки сообщений пользователю с информацией об очках.

    :param points_data: данные о поражениях (команда и количество поражений)
    :param call: обратный вызов кнопки
    """

    for points in points_data:
        bot.send_message(call.message.chat.id, points)


from loader import bot
from telebot.types import CallbackQuery, Message
from api.football_api import api_request
from collections.abc import Iterable
from handlers.custom_handlers.custom.data_check import points_data_check
from handlers.custom_handlers.print_info import print_info
from typing import List
from api.api_params import methods_endswith_list, params_dict


method_endswith = methods_endswith_list[0]
params = params_dict['standings_and_all_stadiums']


def points_call(call: CallbackQuery) -> None:
    """
    Функция для запуска процесса отображения информации на экран пользователя. Запускается функция points_print
    для получения и отправки информации об очках пользователю.

    :param call: обратный вызов кнопки
    """

    bot.edit_message_text(
        f'Введите диапазон из двух чисел через пробел для поиска по очкам команд:', call.message.chat.id,
        call.message.message_id
    )
    bot.register_next_step_handler(call.message, points_data_check, points_stat, print_info)


def points_stat(data_list: List) -> Iterable[str]:
    """
    Функция-генератор для получения количества очков.

    :param data_list: список с цифрами для диапазона
    :return: team, points
    :rtype: Iterable[str]
    """

    global method_endswith
    global params

    response = api_request(method_endswith, params)
    team_name = response['response'][0]['league']['standings'][0]
    is_one_in_range = False
    teams = 20

    for counter in range(teams):
        for point in team_name[counter]:

            if point == 'points' and int(data_list[0]) <= team_name[counter][point] <= int(data_list[1]):
                is_one_in_range = True
                points = team_name[counter][point]
                team = team_name[counter]['team']['name']
                yield f'Команда: {team}\n' \
                      f'Очки: {points}'

    if not is_one_in_range:
        yield f'Команд по заданному диапазону не найдено.'

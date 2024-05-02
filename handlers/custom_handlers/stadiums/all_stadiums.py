from loader import bot
from telebot.types import CallbackQuery, Message
from api.football_api import api_request
from collections.abc import Iterable
from typing import Dict

method_endswith = '/v3/teams'

params: Dict[str, int] = {
    'league': 140,
    'season': 2023
}

method_type = 'GET'


def stadium_show(call: CallbackQuery) -> None:
    """
    Функция для запуска процесса отображения информации на экран пользователя. Запускается функция stadium_print
    для получения и отправки информации о командах, их стадионах и городах пользователю.

    :param call: обратный вызов кнопки
    """

    bot.edit_message_text(f'Команды, их города и стадионы:', call.message.chat.id, call.message.message_id)

    stadium_info = stadium_gen()
    stadium_print(stadium_info, call)


def stadium_gen() -> Iterable[str]:
    """
    Функция-генератор для получения команд, их городов и стадионов.

    :return: team, city_list
    :rtype: Iterable[str]
    """

    response = api_request(method_endswith, params, method_type)
    teams_n_stadiums_dict = dict()

    for counter in range(20):
        team_name = response['response'][counter]['team']['name']
        stadium_name = response['response'][counter]['venue']['name']
        city = response['response'][counter]['venue']['city']
        teams_n_stadiums_dict[team_name] = [city, stadium_name]

    for team, city_list in sorted(teams_n_stadiums_dict.items()):
        yield f'Команда: {team}\n' \
              f'Город: {city_list[0]}\n' \
              f'Стадион: {city_list[1]}'


def stadium_print(stadium_data: Iterable[str], call: CallbackQuery):
    """
    Функция для вывода информации о командах, стадионах и городах на экран пользователю.

    :param stadium_data: строка с командой, ее городом и стадионом
    :param call: обратный вызов кнопки
    """

    for stadium in stadium_data:
        bot.send_message(call.message.chat.id, stadium)




from loader import bot
from telebot.types import CallbackQuery
from api.football_api import api_request
from collections.abc import Iterable
from typing import List
from handlers.custom_handlers.print_info import print_info
from api.api_params import methods_endswith_list, params_dict
from database.new_enquiry import add_new_enquiry


command = '/stadiums'

method_endswith = methods_endswith_list[1]
params = params_dict['standings_and_all_stadiums']
result_list: List[str] = ['all', 'home', 'away']


def stadium_call(call: CallbackQuery) -> None:
    """
    Функция для запуска процесса отображения информации на экран пользователя. Запускается функция stadium_print
    для получения и отправки информации о командах, их стадионах и городах пользователю.

    :param call: обратный вызов кнопки
    """

    global command

    bot.edit_message_text(f'Команды, их города и стадионы:', call.message.chat.id, call.message.message_id)

    stadium_info = stadium_gen()
    add_new_enquiry(call.message, command)
    print_info(stadium_info, call.message)


def stadium_gen() -> Iterable[str]:
    """
    Функция-генератор для получения команд, их городов и стадионов.

    :return: team, city_list
    :rtype: Iterable[str]
    """
    global method_endswith
    global params

    response = api_request(method_endswith, params)
    teams_n_stadiums_dict = dict()
    teams = 20

    for counter in range(teams):
        team_name = response['response'][counter]['team']['name']
        stadium_name = response['response'][counter]['venue']['name']
        city = response['response'][counter]['venue']['city']
        teams_n_stadiums_dict[team_name] = [city, stadium_name]

    for team, city_list in sorted(teams_n_stadiums_dict.items()):
        yield f'Команда: {team}\n' \
              f'Город: {city_list[0]}\n' \
              f'Стадион: {city_list[1]}'

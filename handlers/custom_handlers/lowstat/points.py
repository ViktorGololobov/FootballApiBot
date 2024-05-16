from loader import bot
from telebot.types import CallbackQuery
from api.football_api import api_request
from collections.abc import Iterable
from handlers.custom_handlers.print_info import print_info
from api.api_params import methods_endswith_list, params_dict
from database.new_enquiry import add_new_enquiry


command = '/lowstat_champ'

method_endswith = methods_endswith_list[0]
params = params_dict['standings_and_all_stadiums']


def points_call(call: CallbackQuery) -> None:
    """
    Функция для запуска процесса отображения информации на экран пользователя. Запускается функция points_print
    для получения и отправки информации об очках пользователю.

    :param call: обратный вызов кнопки
    """

    global command

    bot.edit_message_text(
        f'Наименьшее количество очков:', call.message.chat.id, call.message.message_id
    )
    points_info = points_stat()
    add_new_enquiry(call.message, command)
    print_info(points_info, call.message)


def points_stat() -> Iterable[str]:
    """
    Функция-генератор для получения количества очков.

    :return: key, value
    :rtype: Iterable[str]
    """

    global method_endswith
    global params

    response = api_request(method_endswith, params)
    team_name = response['response'][0]['league']['standings'][0]
    points = 0
    team_dict = dict()
    teams = 20

    for counter in range(teams):
        for point in team_name[counter]:
            if point == 'points' and counter == 0:
                points = team_name[counter][point]
                team = team_name[counter]['team']['name']
                team_dict[team] = points
                continue

            if point == 'points' and points >= team_name[counter][point]:
                points = team_name[counter][point]
                team = team_name[counter]['team']['name']
                team_dict[team] = points

    minimum = min(team_dict.values())

    for key, value in team_dict.items():
        if minimum == value:
            yield f'Команда: {key}\n'\
                  f'Очки: {value}'

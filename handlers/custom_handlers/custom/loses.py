from loader import bot
from telebot.types import CallbackQuery, Message
from api.football_api import api_request
from states.custom_states.custom_main_states import CustomStatMainState
from states.custom_states.loses_states import CustomLosesStat
from states.main_states import UserMainCommandInfo
from keyboards.inline.custom_buttons.main_buttons import button_generator_for_back
from operator import itemgetter
from handlers.custom_handlers.print_info import print_info
from handlers.custom_handlers.custom.data_check import win_lose_draw_data_check
from collections.abc import Iterable
from typing import List
from api.api_params import methods_endswith_list, params_dict


method_endswith = methods_endswith_list[0]
params = params_dict['standings_and_all_stadiums']
points_list: List[str] = ['all', 'home', 'away']


@bot.callback_query_handler(func=lambda call: True, state=CustomStatMainState.loses)
def loses_call(call: CallbackQuery) -> None:
    """
    Хэндлер для запуска процесса отображения информации на экран пользователя. Декоратор ловит состояние
    пользователя state и передает функции data_check, loses_stat, loses_print и строчный параметр points_list в
    callback-функцию для проверки корректности ввода пользователем, его обработки и вывода результата в бота.

    :param call: обратный вызов кнопки
    """

    if call.data == 'all_info':
        bot.set_state(call.message.chat.id, CustomLosesStat.all_loses, call.message.chat.id)
        bot.edit_message_text(
            f'Введите диапазон из двух чисел через пробел для поиска по всем поражениям команд:', call.message.chat.id,
            call.message.message_id
        )
        bot.register_next_step_handler(call.message, win_lose_draw_data_check, loses_stat, print_info, points_list[0])
    elif call.data == 'home':
        bot.set_state(call.message.chat.id, CustomLosesStat.home_loses, call.message.chat.id)
        bot.edit_message_text(
            f'Введите диапазон из двух чисел через пробел для поиска по всем домашним поражениям команд:',
            call.message.chat.id, call.message.message_id
        )
        bot.register_next_step_handler(call.message, win_lose_draw_data_check, loses_stat, print_info, points_list[1])
    elif call.data == 'away':
        bot.set_state(call.message.chat.id, CustomLosesStat.away_loses, call.message.chat.id)
        bot.edit_message_text(
            f'Введите диапазон из двух чисел через пробел для поиска по всем гостевым поражениям команд:',
            call.message.chat.id, call.message.message_id
        )
        bot.register_next_step_handler(call.message, win_lose_draw_data_check, loses_stat, print_info, points_list[2])
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, UserMainCommandInfo.custom, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в главное меню. Какой показатель интересует? ', call.message.chat.id,
            call.message.message_id, reply_markup=button_generator_for_back()
        )


def loses_stat(result: str, data_list: List) -> Iterable[str]:
    """
    Функция-генератор для получения количества поражений. На вход получает параметр, где нужно смотреть поражения (все,
    дома или на выезде), список с диапазоном и возвращает команды и результат.

    :param result: параметр для поиска побед
    :param data_list: список с цифрами для диапазона
    :return: key, value
    :rtype: Iterable[str]
    """

    global method_endswith
    global params

    response = api_request(method_endswith, params)
    team_name = response['response'][0]['league']['standings'][0]
    team_dict = dict()
    teams = 20

    for counter in range(teams):
        for point in team_name[counter][result]:

            if point == 'lose' and int(data_list[0]) <= team_name[counter][result][point] <= int(data_list[1]):
                wins = team_name[counter][result][point]
                team = team_name[counter]['team']['name']
                team_dict[team] = wins

    team_list = sorted(team_dict.items(), key=itemgetter(1))
    team_dict = dict(team_list)

    for key, value in reversed(team_dict.items()):
        yield f'Команда: {key}\n' \
              f'Поражения: {value}'

    if len(team_dict) == 0:
        yield f'Команд по заданному диапазону не найдено.'

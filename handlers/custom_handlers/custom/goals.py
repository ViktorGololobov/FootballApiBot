from loader import bot
from telebot.types import CallbackQuery, Message
from states.custom_states.goals_states import CustomStatGoals, CustomStatGoalsForAgainst
from api.football_api import api_request
from keyboards.inline.custom_buttons.main_buttons import all_home_away_buttons_gen
from states.custom_states.custom_main_states import CustomStatMainState
from handlers.custom_handlers.custom.data_check import goal_data_check
from handlers.custom_handlers.print_info import print_info
from operator import itemgetter
from collections.abc import Iterable
from typing import List
from api.api_params import methods_endswith_list, params_dict


method_endswith = methods_endswith_list[0]
params = params_dict['standings_and_all_stadiums']
points_list: List[str] = ['all', 'home', 'away']
for_against: List[str] = ['for', 'against']


@bot.callback_query_handler(func=lambda call: True, state=CustomStatGoals.all_goals)
def goals_call(call: CallbackQuery) -> None:
    """
    Хэндлер для запуска процесса отображения информации на экран пользователя по всем голам. Декоратор ловит
    состояние пользователя state и передает функции goal_data_check, goals_stat, goals_print и строчные параметры
    points_list и for_against в callback-функцию для проверки корректности ввода пользователем, его обработки и
    вывода результата в бота.

    :param call: обратный вызов кнопки
    """

    if call.data == 'goals_for':
        bot.set_state(call.message.chat.id, CustomStatGoalsForAgainst.goals_for, call.message.chat.id)
        bot.edit_message_text(
            f'Введите диапазон через пробел для поиска по всем забитым голам команд:', call.message.chat.id,
            call.message.message_id
        )
        bot.register_next_step_handler(
            call.message, goal_data_check, goals_stat, print_info, points_list[0], for_against[0]
        )
    elif call.data == 'goals_against':
        bot.set_state(call.message.chat.id, CustomStatGoalsForAgainst.goals_against, call.message.chat.id)
        bot.edit_message_text(
            f'Введите диапазон через пробел для поиска по всем пропущенным голам команд:', call.message.chat.id,
            call.message.message_id
        )
        bot.register_next_step_handler(
            call.message, goal_data_check, goals_stat, print_info, points_list[0], for_against[1]
        )
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, CustomStatMainState.goals, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в предыдущее меню. Вам нужны голы дома, на выезде или общее количество? ',
            call.message.chat.id, call.message.message_id, reply_markup=all_home_away_buttons_gen()
        )


@bot.callback_query_handler(func=lambda call: True, state=CustomStatGoals.home_goals)
def goals_call(call: CallbackQuery) -> None:
    """
    Хэндлер для запуска процесса отображения информации на экран пользователя по всем голам. Декоратор ловит
    состояние пользователя state и передает функции goal_data_check, goals_stat, goals_print и строчные параметры
    points_list и for_against в callback-функцию для проверки корректности ввода пользователем, его обработки и
    вывода результата в бота.

    :param call: обратный вызов кнопки
    """

    if call.data == 'goals_for':
        bot.set_state(call.message.chat.id, CustomStatGoalsForAgainst.goals_for, call.message.chat.id)
        bot.edit_message_text(
            f'Введите диапазон через пробел для поиска по домашним забитым голам команд:', call.message.chat.id,
            call.message.message_id
        )
        bot.register_next_step_handler(
            call.message, goal_data_check, goals_stat, print_info, points_list[1], for_against[0]
        )
    elif call.data == 'goals_against':
        bot.set_state(call.message.chat.id, CustomStatGoalsForAgainst.goals_against, call.message.chat.id)
        bot.edit_message_text(
            f'Введите диапазон через пробел для поиска по домашним пропущенным голам команд:', call.message.chat.id,
            call.message.message_id
        )
        bot.register_next_step_handler(
            call.message, goal_data_check, goals_stat, print_info, points_list[1], for_against[1]
        )
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, CustomStatMainState.goals, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в предыдущее меню. Вам нужны голы дома, на выезде или общее количество? ',
            call.message.chat.id, call.message.message_id, reply_markup=all_home_away_buttons_gen()
        )


@bot.callback_query_handler(func=lambda call: True, state=CustomStatGoals.away_goals)
def goals_call(call: CallbackQuery) -> None:
    """
    Хэндлер для запуска процесса отображения информации на экран пользователя по всем голам. Декоратор ловит
    состояние пользователя state и передает функции goal_data_check, goals_stat, goals_print и строчные параметры
    points_list и for_against в callback-функцию для проверки корректности ввода пользователем, его обработки и
    вывода результата в бота.

    :param call: обратный вызов кнопки
    """

    if call.data == 'goals_for':
        bot.set_state(call.message.chat.id, CustomStatGoalsForAgainst.goals_for, call.message.chat.id)
        bot.edit_message_text(
            f'Введите диапазон через пробел для поиска по гостевым забитым голам команд:', call.message.chat.id,
            call.message.message_id
        )
        bot.register_next_step_handler(
            call.message, goal_data_check, goals_stat, print_info, points_list[2], for_against[0]
        )
    elif call.data == 'goals_against':
        bot.set_state(call.message.chat.id, CustomStatGoalsForAgainst.goals_against, call.message.chat.id)
        bot.edit_message_text(
            f'Введите диапазон через пробел для поиска по гостевым пропущенным голам команд:', call.message.chat.id,
            call.message.message_id
        )
        bot.register_next_step_handler(
            call.message, goal_data_check, goals_stat, print_info, points_list[2], for_against[1]
        )
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, CustomStatMainState.goals, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в предыдущее меню. Вам нужны голы дома, на выезде или общее количество? ',
            call.message.chat.id, call.message.message_id, reply_markup=all_home_away_buttons_gen()
        )


def goals_stat(result: str, goals_param: str, data_list: str) -> Iterable[str]:
    """
    Функция-генератор для получения количества голов. На вход получает параметр, где нужно смотреть голы (все, дома или
    на выезде), параметр по забитым или пропущенным голам и список с диапазоном и возвращает команды и результат.

    :param result: параметр для поиска побед
    :param goals_param: параметр для поиска голов по забитым или пропущеннным
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

            if point == 'goals' and \
                    int(data_list[0]) <= team_name[counter][result][point][goals_param] <= int(data_list[1]):
                goals = team_name[counter][result][point][goals_param]
                team = team_name[counter]['team']['name']
                team_dict[team] = goals

    team_list = sorted(team_dict.items(), key=itemgetter(1))
    team_dict = dict(team_list)

    for key, value in reversed(team_dict.items()):
        yield f'Команда: {key}\n' \
              f'Голы: {value}'

    if len(team_dict) == 0:
        yield f'Команд по заданному диапазону не найдено.'

from loader import bot
from telebot.types import Message
from typing import Callable, Dict


def win_lose_draw_data_check(
        message: Message, stat_func: Callable, print_func: Callable, point: str, api_endswith: str, parameters: Dict,
        api_method_type: str
) -> None:
    """
    Функция для проверки корректности ввода диапазона пользователем. На вход получает сообщение от пользователя,
    две функции и параметр для поиска, который нужно передать в следующую функцию.

    :param message: сообщение от пользователя
    :param stat_func: функция для получения искомого количества побед, ничьих или поражений
    :param print_func: функция для вывода информации пользователю
    :param point: параметр для передачи в следующую функцию
    :param api_endswith: запрос
    :param parameters: параметры запроса
    :param api_method_type: тип запроса
    """

    data_list = message.text.split(' ')
    count = 0
    for data in data_list:
        if data.isdigit():
            count += 1

    if count < len(data_list):
        bot.send_message(message.chat.id, f'Неверный формат ввода. Введите два числа через пробел:')
        bot.register_next_step_handler(
            message, win_lose_draw_data_check, stat_func, print_func,  point, api_endswith, parameters, api_method_type
        )
    elif count < 2:
        bot.send_message(message.chat.id, f'Неверный формат ввода, введено одно число. Введите два числа через пробел:')
        bot.register_next_step_handler(
            message, win_lose_draw_data_check, stat_func, print_func, point, api_endswith, parameters, api_method_type
        )
    elif count > 2:
        bot.send_message(message.chat.id, f'Неверный формат ввода, введено больше двух чисел. '
                                          f'Введите два числа через пробел:')
        bot.register_next_step_handler(
            message, win_lose_draw_data_check, stat_func, print_func, point, api_endswith, parameters, api_method_type
        )
    elif int(data_list[0]) > int(data_list[1]):
        bot.send_message(message.chat.id, f'Первое число больше второго, должно быть наоборот. '
                                          f'Введите два числа через пробел повторно:')
        bot.register_next_step_handler(
            message, win_lose_draw_data_check, stat_func, print_func, point, api_endswith, parameters, api_method_type
        )
    else:
        func_info = stat_func(point, data_list, api_endswith, parameters, api_method_type)
        print_func(func_info, message)


def goal_data_check(
        message: Message, stat_func: Callable, print_func: Callable, point: str, for_against_goals: str,
        api_endswith: str, parameters: Dict, api_method_type: str
) -> None:
    """
    Функция для проверки корректности ввода диапазона пользователем. На вход получает сообщение от пользователя,
    две функции и параметр для поиска, который нужно передать в следующую функцию.

    :param message: сообщение от пользователя
    :param stat_func: функция для получения искомого количества голов
    :param print_func: функция для вывода информации пользователю
    :param point: параметр для поиска среди всех голов, дома или на выезде. Передается в функцию stat_func
    :param for_against_goals: параметр для поиска по забитым или пропущенным. Передается в функцию print_func
    :param api_endswith: запрос
    :param parameters: параметры запроса
    :param api_method_type: тип запроса
    """

    data_list = message.text.split(' ')
    count = 0
    for data in data_list:
        if data.isdigit():
            count += 1

    if count < len(data_list):
        bot.send_message(message.chat.id, f'Неверный формат ввода. Введите два числа через пробел:')
        bot.register_next_step_handler(
            message, goal_data_check, stat_func, print_func, point, for_against_goals, api_endswith, parameters,
            api_method_type
        )
    elif count < 2:
        bot.send_message(message.chat.id, f'Неверный формат ввода, введено одно число. Введите два числа через пробел:')
        bot.register_next_step_handler(
            message, goal_data_check, stat_func, print_func, point, for_against_goals, api_endswith, parameters,
            api_method_type
        )
    elif count > 2:
        bot.send_message(message.chat.id, f'Неверный формат ввода, введено больше двух чисел. '
                                          f'Введите два числа через пробел:')
        bot.register_next_step_handler(
            message, goal_data_check, stat_func, print_func, point, for_against_goals, api_endswith, parameters,
            api_method_type
        )
    elif int(data_list[0]) > int(data_list[1]):
        bot.send_message(message.chat.id, f'Первое число больше второго, должно быть наоборот. '
                                          f'Введите два числа через пробел повторно:')
        bot.register_next_step_handler(
            message, goal_data_check, stat_func, print_func, point, for_against_goals, api_endswith, parameters,
            api_method_type
        )
    else:
        goals_info = stat_func(point, for_against_goals, data_list, api_endswith, parameters, api_method_type)
        print_func(goals_info, message)


def points_data_check(
        message: Message, stat_func: Callable, print_func: Callable, api_endswith: str, parameters: Dict,
        api_method_type: str
) -> None:
    """
    Функция для проверки корректности ввода диапазона пользователем. На вход получает сообщение от пользователя и
    две функции, которые вызываются в случае, если все в порядке.

    :param message: сообщение от пользователя
    :param stat_func: функция для получения искомого количества очков
    :param print_func: функция для вывода информации пользователю
    :param api_endswith: запрос
    :param parameters: параметры запроса
    :param api_method_type: тип запроса
    """

    data_list = message.text.split(' ')
    count = 0
    for data in data_list:
        if data.isdigit():
            count += 1

    if count < len(data_list):
        bot.send_message(message.chat.id, f'Неверный формат ввода. Введите два числа через пробел:')
        bot.register_next_step_handler(
            message, points_data_check, stat_func, print_func, api_endswith, parameters, api_method_type
        )
    elif count < 2:
        bot.send_message(message.chat.id, f'Неверный формат ввода, введено одно число. Введите два числа через пробел:')
        bot.register_next_step_handler(
            message, points_data_check, stat_func, print_func, api_endswith, parameters, api_method_type
        )
    elif count > 2:
        bot.send_message(message.chat.id, f'Неверный формат ввода, введено больше двух чисел. '
                                          f'Введите два числа через пробел:')
        bot.register_next_step_handler(
            message, points_data_check, stat_func, print_func, api_endswith, parameters, api_method_type
        )
    elif int(data_list[0]) > int(data_list[1]):
        bot.send_message(message.chat.id, f'Первое число больше второго, должно быть наоборот. '
                                          f'Введите два числа через пробел повторно:')
        bot.register_next_step_handler(
            message, points_data_check, stat_func, print_func, api_endswith, parameters, api_method_type)
    else:
        points_info = stat_func(data_list, api_endswith, parameters, api_method_type)
        print_func(points_info, message)

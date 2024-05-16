from loader import bot
from telebot.types import Message
from typing import Callable
from database.new_enquiry import add_new_enquiry

command = '/custom_champ'


def win_lose_draw_data_check(
        message: Message,
        stat_func: Callable,
        print_func: Callable,
        point: str,
) -> None:
    """
    Функция для проверки корректности ввода диапазона пользователем. На вход получает сообщение от пользователя,
    две функции и параметр для поиска, который нужно передать в следующую функцию.

    :param message: сообщение от пользователя
    :param stat_func: функция для получения искомого количества побед, ничьих или поражений
    :param print_func: функция для вывода информации пользователю
    :param point: параметр для передачи в следующую функцию
    """

    global command

    data_list = message.text.split(' ')
    count = 0

    for data in data_list:
        if data.isdigit():
            count += 1

    try:
        data_1 = int(data_list[0])
        data_2 = int(data_list[1])
    except (TypeError, ValueError):
        bot.send_message(message.chat.id, f'В введенной строке нет двух отдельных целых чисел. '
                                          f'Введите два целых числа через пробел повторно:')
        bot.register_next_step_handler(message, win_lose_draw_data_check, stat_func, print_func, point)
    except IndexError:
        bot.send_message(message.chat.id, f'Неверный формат ввода, введено одно число. '
                                          f'Введите два числа через пробел:')
        bot.register_next_step_handler(message, win_lose_draw_data_check, stat_func, print_func, point)
    else:
        if data_1 < 0 or data_2 < 0:
            bot.send_message(message.chat.id, f'Одно или оба числа отрицательны. Числа должны быть положительными. '
                                              f'Введите два целых числа через пробел повторно:')
            bot.register_next_step_handler(message, win_lose_draw_data_check, stat_func, print_func, point)
        elif count > 2:
            bot.send_message(message.chat.id, f'Неверный формат ввода, введено больше двух чисел. '
                                              f'Введите два числа через пробел:')
            bot.register_next_step_handler(message, win_lose_draw_data_check, stat_func, print_func, point)
        elif data_1 > data_2:
            bot.send_message(message.chat.id, f'Первое число больше второго, должно быть наоборот. '
                                              f'Введите два числа через пробел повторно:')
            bot.register_next_step_handler(message, win_lose_draw_data_check, stat_func, print_func, point)
        else:
            func_info = stat_func(point, data_list)
            add_new_enquiry(message, command)
            print_func(func_info, message)


def goal_data_check(
        message: Message,
        stat_func: Callable,
        print_func: Callable,
        point: str,
        for_against_goals: str
) -> None:
    """
    Функция для проверки корректности ввода диапазона пользователем. На вход получает сообщение от пользователя,
    две функции и параметр для поиска, который нужно передать в следующую функцию.

    :param message: сообщение от пользователя
    :param stat_func: функция для получения искомого количества голов
    :param print_func: функция для вывода информации пользователю
    :param point: параметр для поиска среди всех голов, дома или на выезде. Передается в функцию stat_func
    :param for_against_goals: параметр для поиска по забитым или пропущенным. Передается в функцию print_func
    """

    global command

    data_list = message.text.split(' ')
    count = 0

    for data in data_list:
        if data.isdigit():
            count += 1

    try:
        data_1 = int(data_list[0])
        data_2 = int(data_list[1])
    except (TypeError, ValueError):
        bot.send_message(message.chat.id, f'В введенной строке нет двух отдельных целых чисел. '
                                          f'Введите два целых числа через пробел повторно:')
        bot.register_next_step_handler(message, goal_data_check, stat_func, print_func, point, for_against_goals)
    except IndexError:
        bot.send_message(message.chat.id, f'Неверный формат ввода, введено одно число. '
                                          f'Введите два числа через пробел:')
        bot.register_next_step_handler(message, goal_data_check, stat_func, print_func, point, for_against_goals)
    else:
        if data_1 < 0 or data_2 < 0:
            bot.send_message(message.chat.id, f'Одно или оба числа отрицательны. Числа должны быть положительными. '
                                              f'Введите два целых числа через пробел повторно:')
            bot.register_next_step_handler(message, goal_data_check, stat_func, print_func, point, for_against_goals)
        elif count > 2:
            bot.send_message(message.chat.id, f'Неверный формат ввода, введено больше двух чисел. '
                                              f'Введите два числа через пробел:')
            bot.register_next_step_handler(message, goal_data_check, stat_func, print_func, point, for_against_goals)
        elif data_1 > data_2:
            bot.send_message(message.chat.id, f'Первое число больше второго, должно быть наоборот. '
                                              f'Введите два числа через пробел повторно:')
            bot.register_next_step_handler(message, goal_data_check, stat_func, print_func, point, for_against_goals)
        else:
            goals_info = stat_func(point, for_against_goals, data_list)
            add_new_enquiry(message, command)
            print_func(goals_info, message)


def points_data_check(
        message: Message,
        stat_func: Callable,
        print_func: Callable
) -> None:
    """
    Функция для проверки корректности ввода диапазона пользователем. На вход получает сообщение от пользователя и
    две функции, которые вызываются в случае, если все в порядке.

    :param message: сообщение от пользователя
    :param stat_func: функция для получения искомого количества очков
    :param print_func: функция для вывода информации пользователю
    """

    global command

    data_list = message.text.split(' ')
    count = 0

    for data in data_list:
        if data.isdigit():
            count += 1

    try:
        data_1 = int(data_list[0])
        data_2 = int(data_list[1])
    except (TypeError, ValueError):
        bot.send_message(message.chat.id, f'В введенной строке нет двух отдельных целых чисел. '
                                          f'Введите два целых числа через пробел повторно:')
        bot.register_next_step_handler(message, points_data_check, stat_func, print_func)
    except IndexError:
        bot.send_message(message.chat.id, f'Неверный формат ввода, введено одно число. '
                                          f'Введите два числа через пробел:')
        bot.register_next_step_handler(message, points_data_check, stat_func, print_func)
    else:
        if data_1 < 0 or data_2 < 0:
            bot.send_message(message.chat.id, f'Одно или оба числа отрицательны. Числа должны быть положительными. '
                                              f'Введите два целых числа через пробел повторно:')
            bot.register_next_step_handler(message, points_data_check, stat_func, print_func)
        elif count > 2:
            bot.send_message(message.chat.id, f'Неверный формат ввода, введено больше двух чисел. '
                                              f'Введите два числа через пробел:')
            bot.register_next_step_handler(message, points_data_check, stat_func, print_func)
        elif data_1 > data_2:
            bot.send_message(message.chat.id, f'Первое число больше второго, должно быть наоборот. '
                                              f'Введите два числа через пробел повторно:')
            bot.register_next_step_handler(message, points_data_check, stat_func, print_func)
        else:
            points_info = stat_func(data_list)
            add_new_enquiry(message, command)
            print_func(points_info, message)

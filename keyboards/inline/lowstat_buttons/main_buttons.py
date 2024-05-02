from telebot import types
from loader import bot
from telebot.types import Message
from states.main_states import UserMainCommandInfo


@bot.message_handler(commands=['lowstat_champ'])
def button_generator(message: Message) -> None:
    """
    Хэндлер для обработки команды lowstat_champ. Создает кнопки, и выводит панель сообщением пользователю.

    :param message: команда lowstat_champ
    """

    bot.set_state(message.from_user.id, UserMainCommandInfo.lowstat, message.chat.id)
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    goals = types.InlineKeyboardButton(text='Голы', callback_data='goals')
    wins = types.InlineKeyboardButton(text='Победы', callback_data='wins')
    draws = types.InlineKeyboardButton(text='Ничьи', callback_data='draws')
    loses = types.InlineKeyboardButton(text='Поражения', callback_data='loses')
    points = types.InlineKeyboardButton(text='Очки', callback_data='points')
    keyboard.add(goals, wins, draws, loses, points)
    bot.send_message(message.from_user.id, f'Какой показатель интересует?', reply_markup=keyboard)


def button_generator_for_back() -> types:
    """
    Вспомогательная функция для создания кнопок при нажатии на кнопку "Назад".

    :return: keyboard
    :rtype: types
    """

    keyboard = types.InlineKeyboardMarkup(row_width=3)
    goals = types.InlineKeyboardButton(text='Голы', callback_data='goals')
    wins = types.InlineKeyboardButton(text='Победы', callback_data='wins')
    draws = types.InlineKeyboardButton(text='Ничьи', callback_data='draws')
    loses = types.InlineKeyboardButton(text='Поражения', callback_data='loses')
    points = types.InlineKeyboardButton(text='Очки', callback_data='points')
    keyboard.add(goals, wins, draws, loses, points)
    return keyboard


def all_home_away_buttons_gen() -> types:
    """
    Функция для создания кнопок "Все", "Дома", "На выезде", "Назад".

    :return: keyboard
    :rtype: types
    """

    keyboard = types.InlineKeyboardMarkup(row_width=3)
    all_info = types.InlineKeyboardButton(text='Все', callback_data='all_info')
    home = types.InlineKeyboardButton(text='Дома', callback_data='home')
    away = types.InlineKeyboardButton(text='На выезде', callback_data='away')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(all_info, home, away, back)
    return keyboard


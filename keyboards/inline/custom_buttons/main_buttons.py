from telebot import types
from loader import bot
from telebot.types import Message
from states.main_states import UserMainCommandInfo


@bot.message_handler(commands=['custom_champ'])
def button_generator(message: Message) -> None:
    """
    Хэндлер для обработки команды custom_champ. Создает кнопки, и выводит панель сообщением пользователю.

    :param message: команда custom_champ
    """

    bot.set_state(message.from_user.id, UserMainCommandInfo.custom, message.chat.id)
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    goals = types.InlineKeyboardButton(text='\U000026BD Голы', callback_data='goals')
    wins = types.InlineKeyboardButton(text='\U0001F3C6 Победы', callback_data='wins')
    draws = types.InlineKeyboardButton(text='\U0001F91D Ничьи', callback_data='draws')
    loses = types.InlineKeyboardButton(text='\U0001F614 Поражения', callback_data='loses')
    points = types.InlineKeyboardButton(text='\U0001F522 Очки', callback_data='points')
    keyboard.add(goals, wins, draws, loses, points)
    bot.send_message(message.from_user.id, f'Какой показатель интересует?', reply_markup=keyboard)


def button_generator_for_back() -> types:
    """
    Вспомогательная функция для создания кнопок при нажатии на кнопку "Назад".

    :return: keyboard
    :rtype: types
    """

    keyboard = types.InlineKeyboardMarkup(row_width=3)
    goals = types.InlineKeyboardButton(text='\U000026BD Голы', callback_data='goals')
    wins = types.InlineKeyboardButton(text='\U0001F3C6 Победы', callback_data='wins')
    draws = types.InlineKeyboardButton(text='\U0001F91D Ничьи', callback_data='draws')
    loses = types.InlineKeyboardButton(text='\U0001F614 Поражения', callback_data='loses')
    points = types.InlineKeyboardButton(text='\U0001F522 Очки', callback_data='points')
    keyboard.add(goals, wins, draws, loses, points)
    return keyboard


def all_home_away_buttons_gen() -> types:
    """
    Функция для создания кнопок "Все", "Дома", "На выезде", "Назад".

    :return: keyboard
    :rtype: types
    """

    keyboard = types.InlineKeyboardMarkup(row_width=3)
    all_info = types.InlineKeyboardButton(text='\U0001F4CA Все', callback_data='all_info')
    home = types.InlineKeyboardButton(text='\U0001F3E0 Дома', callback_data='home')
    away = types.InlineKeyboardButton(text='\U00002708 На выезде', callback_data='away')
    back = types.InlineKeyboardButton(text='\U0001F519 Назад', callback_data='back')
    keyboard.add(all_info, home, away, back)
    return keyboard


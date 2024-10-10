from telebot import types


def for_against_buttons_gen() -> types:
    """
    Функция для создания кнопок по забитым и пропущенным голам.

    :return: for_against_keyboard
    :rtype: types
    """

    for_against_keyboard = types.InlineKeyboardMarkup(row_width=2)
    goals_for = types.InlineKeyboardButton(text='\U00002705 Забито', callback_data='goals_for')
    goals_against = types.InlineKeyboardButton(text='\U0000274C Пропущено', callback_data='goals_against')
    back = types.InlineKeyboardButton(text='\U0001F519 Назад', callback_data='back')
    for_against_keyboard.add(goals_for, goals_against, back)
    return for_against_keyboard

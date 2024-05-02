from loader import bot
from states.main_states import UserMainCommandInfo
from telebot import types
from telebot.types import Message


@bot.message_handler(commands=['stadiums'])
def button_generator(message: Message) -> None:
    """
    Хэндлер для обработки команды stadiums. Создает кнопки, и выводит панель сообщением пользователю.

    :param message: команда stadiums
    """

    bot.set_state(message.from_user.id, UserMainCommandInfo.stadiums, message.chat.id)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    all_stadiums = types.InlineKeyboardButton(text='Все стадионы', callback_data='all_stadiums')
    one_stadium = types.InlineKeyboardButton(text='Один стадион', callback_data='one_stadium')
    keyboard.add(all_stadiums, one_stadium)
    bot.send_message(message.from_user.id, f'Нужна информация по всем стадионам или по одному?', reply_markup=keyboard)


def button_generator_for_back() -> types:
    """
    Хэндлер для обработки команды stadiums. Создает кнопки, и выводит панель сообщением пользователю.

    :param message: команда stadiums
    """

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    all_stadiums = types.InlineKeyboardButton(text='Все стадионы', callback_data='all_stadiums')
    one_stadium = types.InlineKeyboardButton(text='Один стадион', callback_data='one_stadium')
    keyboard.add(all_stadiums, one_stadium)
    return keyboard

from loader import bot
from states.main_states import UserMainCommandInfo
from telebot import types
from telebot.types import Message


@bot.message_handler(commands=['team_statistics'])
def button_generator(message: Message) -> None:
    """
    Хэндлер для обработки команды team_statistics. Создает кнопки, и выводит панель сообщением пользователю.

    :param message: команда stadiums
    """

    bot.set_state(message.from_user.id, UserMainCommandInfo.team_statistics, message.chat.id)

    keyboard = types.InlineKeyboardMarkup(row_width=2)

    alaves = types.InlineKeyboardButton(text='Алавес', callback_data='alaves')
    almeria = types.InlineKeyboardButton(text='Алмерия', callback_data='almeria')
    athletic = types.InlineKeyboardButton(text='Атлетик Бильбао', callback_data='athletic club')
    atletico = types.InlineKeyboardButton(text='Атлетико Мадрид', callback_data='atletico madrid')
    barcelona = types.InlineKeyboardButton(text='Барселона', callback_data='barcelona')
    cadiz = types.InlineKeyboardButton(text='Кадис', callback_data='cadiz')
    celta = types.InlineKeyboardButton(text='Сельта', callback_data='celta vigo')
    getafe = types.InlineKeyboardButton(text='Хетафе', callback_data='getafe')
    girona = types.InlineKeyboardButton(text='Жирона', callback_data='girona')
    granada = types.InlineKeyboardButton(text='Гранада', callback_data='granada cf')
    las_palmas = types.InlineKeyboardButton(text='Лас Пальмас', callback_data='las palmas')
    mallorca = types.InlineKeyboardButton(text='Мальорка', callback_data='mallorca')
    osasuna = types.InlineKeyboardButton(text='Осасуна', callback_data='osasuna')
    rayo_vallecano = types.InlineKeyboardButton(text='Райо Вальекано', callback_data='rayo vallecano')
    real_betis = types.InlineKeyboardButton(text='Реал Бетис', callback_data='real betis')
    real_madrid = types.InlineKeyboardButton(text='Реал Мадрид', callback_data='real madrid')
    real_sociedad = types.InlineKeyboardButton(text='Реал Сосьедад', callback_data='real sociedad')
    sevilla = types.InlineKeyboardButton(text='Севилья', callback_data='sevilla')
    valencia = types.InlineKeyboardButton(text='Валенсия', callback_data='valencia')
    villareal = types.InlineKeyboardButton(text='Вильярреал', callback_data='villarreal')

    keyboard.add(
        alaves, almeria, athletic, atletico, barcelona, cadiz, celta, getafe, girona, granada, las_palmas, mallorca,
        osasuna, rayo_vallecano, real_betis, real_madrid, real_sociedad, sevilla, valencia, villareal
    )
    bot.send_message(message.from_user.id, f'По какой команде нужна статистика?', reply_markup=keyboard)

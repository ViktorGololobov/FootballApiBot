from telebot.types import Message
from datetime import datetime
from database.models import DATE_FORMAT, Users
from peewee import IntegrityError
from loader import bot
from database.models import DB_PATH


@bot.message_handler(state='*', commands=["start"])
def handle_start(message: Message):
    user_id = message.chat.id
    username = message.chat.username
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    message_text = message.text
    date = datetime.strftime(datetime.now(), DATE_FORMAT)

    try:
        with DB_PATH:
            Users.create(
                user_id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                message_text=message_text,
                date=date
            )
        bot.send_message(message.from_user.id, 'Добро пожаловать!\n'
                                               'Это бот для получения статистики по чемпионату Испании по футболу.\n'
                                               'Информация выдается по высшей лиге текущего сезона.\n'
                                               'Для информации о командах бота введите /help или воспользуйтесь '
                                               'меню слева от строки для ввода сообщения.')
    except IntegrityError:
        bot.send_message(message.from_user.id, f'Здравствуйте, {first_name}!\n'
                                               f'Если нужна информация о командах бота, введите /help.\n'
                                               f'Если знаете нужную команду, то можете ввести ее или воспользоваться '
                                               f'меню слева от строки для ввода сообщения.')

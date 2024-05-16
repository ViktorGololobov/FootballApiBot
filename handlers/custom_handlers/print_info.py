from loader import bot
from typing import Iterable
from telebot.types import Message


def print_info(data_info: Iterable[str], call: Message) -> None:
    """
    Функция для отправки сообщений пользователю с информацией о запрошенных данных.

    :param data_info: команда и запрашиваемый параметр
    :param call: обратный вызов кнопки
    """

    for data in data_info:
        bot.send_message(call.chat.id, data)
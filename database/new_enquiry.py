from loader import bot
from telebot.types import Message
from datetime import datetime
from database.models import Users, Task, DATE_FORMAT
from states.history_states.main_states import UserState


def add_new_enquiry(message: Message, input_command: str) -> None:
    """
    Функция для добавления запроса пользователя в БД.

    :param message: сообщение
    :param input_command: команда пользователя
    """

    user_id = message.chat.id
    due_date = datetime.strftime(datetime.now(), DATE_FORMAT)
    command = input_command

    if Users.get_or_none(Users.user_id == user_id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    bot.set_state(message.chat.id, UserState.new_task)
    with bot.retrieve_data(message.chat.id) as data:
        data["new_task"] = {"user_id": user_id}
        data["new_task"]["due_date"] = due_date
        data['new_task']['message_text'] = command

    new_task = Task(**data["new_task"])
    new_task.save()
    bot.delete_state(message.chat.id)

from loader import bot
from database.models import Users, Task
from telebot.types import Message
from typing import List


@bot.message_handler(state='*', commands=["history"])
def handle_tasks(message: Message) -> None:
    user_id = message.from_user.id
    user = Users.get_or_none(Users.user_id == user_id)
    if user is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    tasks: List[Task] = user.tasks.order_by(-Task.due_date, -Task.task_id).limit(10)

    result = []
    result.extend(map(str, reversed(tasks)))

    if not result:
        bot.send_message(message.from_user.id, "У вас ещё нет запросов.")
        return

    bot.send_message(message.from_user.id, "\n".join(result))

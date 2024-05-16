from telebot.types import Message
from loader import bot


@bot.message_handler(state=None)
def bot_echo(message: Message):
    """ Эхо хендлер, куда летят текстовые сообщения без указанного состояния. """
    bot.reply_to(message, f"Я вас не понимаю. \n"
                          f"Для того, чтобы начать, введите команду /start или, если вам нужна помощь, введите /help.")

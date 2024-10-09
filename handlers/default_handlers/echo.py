from telebot.types import Message
from loader import bot


greetings_list = [
    'привет', 'добрый день', 'добрый вечер', 'доброе утро', 'здравствуйте', 'здравствуй', 'приветствую', 'здрасьте',
    'доброго дня', 'доброго вечера', 'доброго утра'
]


@bot.message_handler(state=None)
def bot_echo(message: Message):
    """ Эхо хендлер, куда летят текстовые сообщения без указанного состояния. """

    global greetings_list

    for greeting in greetings_list:
        if greeting in message.text.lower():
            bot.reply_to(
                message,
                'Привет! Для того, чтобы начать, введите команду /start или, если вам нужна помощь, введите /help.'
            )
            break
    else:
        bot.reply_to(
            message,
            "Я вас не понимаю. \n"
            "Для того, чтобы начать, введите команду /start или, если вам нужна помощь, введите /help."
        )

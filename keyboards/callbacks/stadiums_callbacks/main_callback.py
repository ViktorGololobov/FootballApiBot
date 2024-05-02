from loader import bot
from telebot.types import CallbackQuery
from keyboards.inline.stadiums_buttons.one_stadium import one_stadium_buttons
from states.stadiums_states.stadiums_main_states import StadiumStates
from states.main_states import UserMainCommandInfo
from handlers.custom_handlers.stadiums.all_stadiums import stadium_show


@bot.callback_query_handler(func=lambda call: True, state=UserMainCommandInfo.stadiums)
def stadiums_callback(call: CallbackQuery) -> None:
    """
    Хэндлер для обработки вызовов кнопок команды stadiums.

    :param call: обратный вызов кнопки
    """

    if call.message:
        if call.data == 'all_stadiums':
            bot.set_state(call.message.chat.id, StadiumStates.all_stadiums, call.message.chat.id)
            stadium_show(call)
        elif call.data == 'one_stadium':
            bot.set_state(call.message.chat.id, StadiumStates.one_stadium, call.message.chat.id)
            bot.edit_message_text(
                f'Выберите команду: ', call.message.chat.id, call.message.message_id,
                reply_markup=one_stadium_buttons()
            )


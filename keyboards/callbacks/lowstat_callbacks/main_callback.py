from telebot.types import CallbackQuery
from loader import bot
from keyboards.inline.lowstat_buttons.main_buttons import all_home_away_buttons_gen
from states.lowstat_states.lowstat_main_states import LowStatMainState
from states.main_states import UserMainCommandInfo
from handlers.custom_handlers.lowstat.points import points_call


@bot.callback_query_handler(func=lambda call: True, state=UserMainCommandInfo.lowstat)
def lowstat_callback(call: CallbackQuery) -> None:
    """
    Хэндлер для обработки вызовов кнопок.

    :param call: обратный вызов кнопки
    """

    if call.message:
        if call.data == 'goals':
            bot.set_state(call.message.chat.id, LowStatMainState.goals, call.message.chat.id)
            bot.edit_message_text(
                f'У меня есть информация по голам дома, на выезде и общем количестве. Что интересует?',
                call.message.chat.id, call.message.message_id, reply_markup=all_home_away_buttons_gen()
            )
        elif call.data == 'wins':
            bot.set_state(call.message.chat.id, LowStatMainState.wins, call.message.chat.id)
            bot.edit_message_text(
                f'У меня есть информация по победам дома, на выезде и общем количестве. Что интересует?',
                call.message.chat.id, call.message.message_id, reply_markup=all_home_away_buttons_gen()
            )
        elif call.data == 'draws':
            bot.set_state(call.message.chat.id, LowStatMainState.draws, call.message.chat.id)
            bot.edit_message_text(
                f'У меня есть информация по ничьим дома, на выезде и общем количестве. Что интересует?',
                call.message.chat.id, call.message.message_id, reply_markup=all_home_away_buttons_gen()
            )
        elif call.data == 'loses':
            bot.set_state(call.message.chat.id, LowStatMainState.loses, call.message.chat.id)
            bot.edit_message_text(
                f'У меня есть информация по поражениям дома, на выезде и общем количестве. Что интересует?',
                call.message.chat.id, call.message.message_id, reply_markup=all_home_away_buttons_gen()
            )
        elif call.data == 'points':
            bot.set_state(call.message.chat.id, LowStatMainState.points, call.message.chat.id)
            points_call(call)


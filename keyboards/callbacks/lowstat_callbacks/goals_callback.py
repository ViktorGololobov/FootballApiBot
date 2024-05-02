from loader import bot
from states.lowstat_states.goals_states import LowStatGoals
from states.lowstat_states.lowstat_main_states import LowStatMainState
from states.main_states import UserMainCommandInfo
from telebot.types import CallbackQuery
from keyboards.inline.lowstat_buttons.goals_buttons import for_against_buttons_gen
from keyboards.inline.lowstat_buttons.main_buttons import button_generator_for_back


@bot.callback_query_handler(func=lambda call: True, state=LowStatMainState.goals)
def goals_callback(call: CallbackQuery) -> None:
    """
    Хэндлер для обработки вызовов кнопок по голам.

    :param call: обратный вызов кнопки
    """

    if call.data == 'all_info':
        bot.set_state(call.message.chat.id, LowStatGoals.all_goals, call.message.chat.id)
        bot.edit_message_text(
            f'Нужна информация по забитым или пропущенным?', call.message.chat.id,
            call.message.message_id, reply_markup=for_against_buttons_gen()
        )
    elif call.data == 'home':
        bot.set_state(call.message.chat.id, LowStatGoals.home_goals, call.message.chat.id)
        bot.edit_message_text(
            f'Нужна информация по забитым или пропущенным?', call.message.chat.id,
            call.message.message_id, reply_markup=for_against_buttons_gen()
        )
    elif call.data == 'away':
        bot.set_state(call.message.chat.id, LowStatGoals.away_goals, call.message.chat.id)
        bot.edit_message_text(
            f'Нужна информация по забитым или пропущенным?', call.message.chat.id,
            call.message.message_id, reply_markup=for_against_buttons_gen()
        )
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, UserMainCommandInfo.lowstat, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в главное меню. Какой показатель интересует? ', call.message.chat.id,
            call.message.message_id, reply_markup=button_generator_for_back()
        )

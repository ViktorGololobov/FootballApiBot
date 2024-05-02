from loader import bot
from states.highstat_states.goals_states import HighStatGoals
from states.highstat_states.highstat_main_states import HighStatMainState
from states.main_states import UserMainCommandInfo
from telebot.types import CallbackQuery
from keyboards.inline.highstat_buttons.goals_buttons import for_against_buttons_gen
from keyboards.inline.highstat_buttons.main_buttons import button_generator_for_back


@bot.callback_query_handler(func=lambda call: True, state=HighStatMainState.goals)
def goals_callback(call: CallbackQuery) -> None:
    """
    Хэндлер для обработки вызовов кнопок по голам.

    :param call: обратный вызов кнопки
    """

    if call.data == 'all_info':
        bot.set_state(call.message.chat.id, HighStatGoals.all_goals, call.message.chat.id)
        bot.edit_message_text(
            f'Нужна информация по забитым или пропущенным?', call.message.chat.id,
            call.message.message_id, reply_markup=for_against_buttons_gen()
        )
    elif call.data == 'home':
        bot.set_state(call.message.chat.id, HighStatGoals.home_goals, call.message.chat.id)
        bot.edit_message_text(
            f'Нужна информация по забитым или пропущенным?', call.message.chat.id,
            call.message.message_id, reply_markup=for_against_buttons_gen()
        )
    elif call.data == 'away':
        bot.set_state(call.message.chat.id, HighStatGoals.away_goals, call.message.chat.id)
        bot.edit_message_text(
            f'Нужна информация по забитым или пропущенным?', call.message.chat.id,
            call.message.message_id, reply_markup=for_against_buttons_gen()
        )
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, UserMainCommandInfo.highstat, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в главное меню. Какой показатель интересует? ', call.message.chat.id,
            call.message.message_id, reply_markup=button_generator_for_back()
        )

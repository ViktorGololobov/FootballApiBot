from loader import bot
from telebot.types import CallbackQuery
from api.football_api import api_request
from states.stadiums_states.stadiums_main_states import StadiumStates
from states.stadiums_states.one_stadium_states import OneStadiumStates
from states.main_states import UserMainCommandInfo
from keyboards.inline.stadiums_buttons.main_buttons import button_generator_for_back
from typing import List
from api.api_params import methods_endswith_list, params_dict
from database.new_enquiry import add_new_enquiry


command = '/stadiums'

method_endswith = methods_endswith_list[1]
params = params_dict['standings_and_all_stadiums']

team_list: List[str] = [
    'alaves', 'almeria', 'athletic club', 'atletico madrid', 'barcelona', 'cadiz', 'celta vigo', 'getafe', 'girona',
    'granada cf', 'las palmas', 'mallorca', 'osasuna', 'rayo vallecano', 'real betis', 'real madrid', 'real sociedad',
    'sevilla', 'valencia', 'villarreal'
]


@bot.callback_query_handler(func=lambda call: True, state=StadiumStates.one_stadium)
def stadium_call(call: CallbackQuery) -> None:
    """
    Функция для запуска процесса отображения информации на экран пользователя. Запускается функция stadium_gen
    для получения и отправки информации о командах, их стадионах и городах пользователю.

    :param call: обратный вызов кнопки
    """

    global team_list
    global command

    if call.data in team_list:
        bot.set_state(call.message.chat.id, OneStadiumStates.alaves, call.message.chat.id)
        params['name'] = call.data.title()
        bot.edit_message_text(f'Команда, ее город и стадион:', call.message.chat.id, call.message.message_id)
        add_new_enquiry(call.message, command)
        stadium_gen(call)
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, UserMainCommandInfo.stadiums, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в предыдущее меню. Нужна информация по всем стадионам или по одному?', call.message.chat.id,
            call.message.message_id, reply_markup=button_generator_for_back()
        )


def stadium_gen(call: CallbackQuery) -> None:
    """
    Функция для получения команд, их городов и стадионов.

    :param call: обратный вызов кнопки
    """

    global method_endswith
    global params

    response = api_request(method_endswith, params)

    team_name = response['response'][0]['team']['name']
    stadium_name = response['response'][0]['venue']['name']
    city = response['response'][0]['venue']['city']
    bot.send_message(call.message.chat.id, f'\U0001F465 Команда: {team_name}\n'
                                           f'\U0001F3D9 Город: {city}\n'
                                           f'\U0001F3DF Стадион: {stadium_name}')

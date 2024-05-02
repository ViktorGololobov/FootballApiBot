from loader import bot
from telebot.types import CallbackQuery
from api.football_api import api_request
from states.stadiums_states.stadiums_main_states import StadiumStates
from states.stadiums_states.one_stadium_states import OneStadiumStates
from states.main_states import UserMainCommandInfo
from keyboards.inline.stadiums_buttons.main_buttons import button_generator_for_back
from typing import Dict, Any


method_endswith = '/v3/teams'

params: Dict[str, Any] = {
    'league': 140,
    'season': 2023,
    'name': ''
}

method_type = 'GET'
team_list = [
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

    global method_endswith
    global params
    global method_type

    if call.data in team_list:
        bot.set_state(call.message.chat.id, OneStadiumStates.alaves, call.message.chat.id)
        params['name'] = call.data.title()
        bot.edit_message_text(f'Информация по выбранной команде:', call.message.chat.id, call.message.message_id)
        stadium_gen(call, method_endswith, params, method_type)
    elif call.data == 'back':
        bot.set_state(call.message.chat.id, UserMainCommandInfo.stadiums, call.message.chat.id)
        bot.edit_message_text(
            f'Вы вернулись в предыдущее меню. Нужна информация по всем стадионам или по одному?', call.message.chat.id,
            call.message.message_id, reply_markup=button_generator_for_back()
        )


def stadium_gen(call: CallbackQuery, api_endswith: str, parameters: Dict, api_method_type: str) -> None:
    """ Функция для получения команд, их городов и стадионов. """

    response = api_request(api_endswith, parameters, api_method_type)

    team_name = response['response'][0]['team']['name']
    stadium_name = response['response'][0]['venue']['name']
    city = response['response'][0]['venue']['city']
    bot.send_message(call.message.chat.id, f'Команда: {team_name}\nГород: {city}\nСтадион: {stadium_name}')

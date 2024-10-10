from loader import bot
from api.api_params import methods_endswith_list, params_dict
from api.football_api import api_request
from telebot.types import CallbackQuery
from states.main_states import UserMainCommandInfo
from typing import Dict
from database.new_enquiry import add_new_enquiry


command = '/team_statistics'

method_endswith = methods_endswith_list[2]
params = params_dict['teams_statistics']

team_dict: Dict[str, int] = {
    'Barcelona': 529,
    'Atletico Madrid': 530,
    'Athletic Club': 531,
    'Valencia': 532,
    'Villarreal': 533,
    'Las Palmas': 534,
    'Sevilla': 536,
    'Celta Vigo': 538,
    'Real Madrid': 541,
    'Alaves': 542,
    'Real Betis': 543,
    'Getafe': 546,
    'Girona': 547,
    'Real Sociedad': 548,
    'Granada CF': 715,
    'Almeria': 723,
    'Cadiz': 724,
    'Osasuna': 727,
    'Rayo Vallecano': 728,
    'Mallorca': 798
}


@bot.callback_query_handler(func=lambda call: True, state=UserMainCommandInfo.team_statistics)
def team_call(call: CallbackQuery) -> None:
    """
    Callback-хэндлер для реагирования на нажатие кнопки по команде team_statistics

    :param call: обратный вызов кнопки
    """

    global command
    global team_dict

    if call.data.title() in team_dict:
        params['team'] = team_dict[call.data.title()]
        add_new_enquiry(call.message, command)
        team_info_print(call, params)


def card_search(cards: Dict, count=0) -> int:
    """
    Рекурсионная функция для подсчета желтых и красных карт у команды.

    :param cards: словарь с данными для подсчета карт
    :param count: счетчик для подсчета карт
    :return: count
    :rtype: int
    """

    if cards == '106-120':
        return 0

    for key in cards:
        if isinstance(cards[key], dict):
            count += card_search(cards[key])

        if key == 'total':
            if cards[key] is not None:
                return cards[key]
    return count


def team_info_print(call: CallbackQuery, parameters) -> None:
    """
    Функция для получения и отправки пользователю информации о конкретной команде: название, лига, форма,
    количество игр, побед, поражений, ничьих, забитых и пропущенных голов, желтых и красных карточек.

    :param call: название команды
    :param parameters: параметры запроса
    """

    global method_endswith

    response = api_request(method_endswith, parameters)

    team_name = response['response']['team']['name']
    team_league = response['response']['league']['name']
    team_form = response['response']['form']
    team_games = response['response']['fixtures']['played']['total']
    team_wins = response['response']['fixtures']['wins']['total']
    team_draws = response['response']['fixtures']['draws']['total']
    team_loses = response['response']['fixtures']['loses']['total']
    team_goals_for = response['response']['goals']['for']['total']['total']
    team_goals_against = response['response']['goals']['against']['total']['total']
    yellow = response['response']['cards']['yellow']
    yel_cards = card_search(yellow)
    red = response['response']['cards']['red']
    red_cards = card_search(red)
    bot.edit_message_text(
        f'Информация о выбранной команде:\n'
        f'\U0001F465 Команда: {team_name}\n'
        f'\U0001F310 Лига: {team_league}\n'
        f'\U0001F4C8 Форма: {team_form}\n'
        f'\U0001F4C5 Сыграно игр: {team_games}\n'
        f'\U0001F3C6 Победы: {team_wins}\n'
        f'\U0001F91D Ничьи: {team_draws}\n'
        f'\U0001F614 Поражения: {team_loses}\n'
        f'\U000026BD Мячей забито: {team_goals_for}\n'
        f'\U0001F945 Мячей пропущено: {team_goals_against}\n'
        f'\U0001F7E8 Желтые карточки: {yel_cards}\n'
        f'\U0001F7E5 Красные карточки: {red_cards}',
        call.message.chat.id, call.message.message_id
    )

import requests
from config_data import config
from typing import Dict


headers: Dict = {
    "X-RapidAPI-Key": config.RAPID_API_KEY,
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

url_api = 'https://api-football-v1.p.rapidapi.com'


def api_request(method_endswith: str, params: Dict) -> Dict:
    """
    Функция для получения данных от API через функцию get_request.

    :param method_endswith: API запрос. Может меняться в зависимости от запроса
    :param params: параметры запроса
    :return: get_request
    :rtype: dict
    """

    global url_api

    url = f"{url_api}{method_endswith}"

    return get_request(
            url=url,
            params=params
        )


def get_request(url: str, params: Dict) -> Dict:
    """
    Функция для получения отклика API.

    :param url: ссылка на API
    :param params: параметры для API
    :return: response
    :rtype: dict
    """

    try:
        response = requests.get(
            url=url,
            headers=headers,
            params=params,
            timeout=10
        )
        if response.status_code == requests.codes.ok:
            return response.json()
    except NameError as exc:
        print(exc)


def get_request_for_season(url):
    """ Функция получения отклика от API для получения года сезона. """

    response = requests.get(
        url=url,
        headers=headers
    )
    if response.status_code == requests.codes.ok:
        return response.json()

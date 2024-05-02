import requests
from config_data import config


headers = {
    "X-RapidAPI-Key": config.RAPID_API_KEY,
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

url_api = 'https://api-football-v1.p.rapidapi.com'


def api_request(method_endswith, params, method_type) -> dict:
    """
    Функция для получения данных от API через функцию get_request.

    :param method_endswith: API запрос. Может меняться в зависимости от запроса
    :param params: параметры запроса
    :param method_type: метод/тип запроса. Может быть GET или POST
    :return: get_request
    :rtype: dict
    """

    url = f"{url_api}{method_endswith}"

    if method_type == 'GET':
        return get_request(
            url=url,
            params=params
        )


def get_request(url, params) -> dict:
    """
    Функция для получения отклика API.

    :param url: ссылка на API
    :param params: параметры для API
    :return: response
    :rtype: dict
    """

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=10
        )
        if response.status_code == requests.codes.ok:
            return response.json()
    except NameError as exc:
        print(exc)



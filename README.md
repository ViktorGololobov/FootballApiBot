# Telegram-API-FootballBot 
Телеграм-бот по футболу, выводящий по запросу информацию по чемпионату Испании.

## Описание
Телеграм-бот, который выводит информацию по первому дивизиону чемпионата Испании по футболу или команде, участвующую в нем. У бота есть 7 команд: /lowstat_champ, /highstat_champ, /custom_champ, /help, /stadiums, /team_statistics и /history с кнопками Наименьший показатель чемпионата, Наибольший показатель чемпионата, Информация по показателю в указанном диапазоне, Помощь, Стадионы команд, Статистика команды и История запросов соответственно. Как команды и кнопки работают:
- /lowstat_champ (кнопка Наименьший показатель чемпионата): запрашивает у пользователя, какие данные он хочет получить (голы, победы, ничьи, поражения и очки) и выводит наименьшее значение;
- /highstat_champ (кнопка Наибольший показатель чемпионата): запрашивает у пользователя, какие данные он хочет получить (голы, победы, ничьи, поражения и очки) и выводит наибольшее значение;
- /custom_champ (кнопка Информация по показателю в указанном диапазоне): запрашивает у пользователя, какие данные он хочет получить (голы, победы, ничьи, поражения и очки), затем пользователь вводит диапазон и команда выводит значения в заданном диапазоне;
- /stadiums (кнопка Стадионы команд): запрашивает у пользователя, хочет ли он посмотреть стадионы всех команд или какой-либо конкретной и выдает список стадионов всех команд чемпионата или одной в зависимости от его выбора; 
- /team_statistics (кнопка Статистика команды): запрашивает у пользователя, какую статистику он хочет увидеть (таблицу чемпионата, забитые/пропущенные голы, сейвы и т.д.). В рамках команды бот будет выдавать список всех команд по порядку по местам в таблице чемпионата и нужное значение;
- /history (кнопка История запросов): выводит пользователю его последние 10 запросов;
- /help (кнопка Помощь): выводит информацию по командам бота.

## API и эндпоинты
Используемый API: 

`https://rapidapi.com/api-sports/api/api-football` - регистрация не нужна, достаточно регистрации на rapidapi.com.

Эндпоинты:

`/v3/standings` - GET запрос, выдающий информацию по турнирной таблице конкретного чемпионата.


`/v3/teams/statistics` - GET запрос, выдающий подробную информацию по статистике одной команды: голы дома/на выезде, статистика получения карточек, сухих игр, схемы игры в сезоне и тд


`/v3/teams` - GET запрос, выдающий информацию по всем командам.


## Этапы разработки:

1. Создание виртуального окружения
2. Создание и реализация директории config_data для хранения секретных данных
	- Создание и реализация модуля config
3. Создание и реализация директории keyboards для кнопок
4. Создание и реализация модуля lowstat_champ
5. Создание и реализация модуля highstat_champ
6. Создание и реализация модуля custom_champ
7. Создание и реализация модуля team_statistics
8. Создание и реализация модуля stadiums
9. Создание и реализация модуля help
10. Создание и реализация модуля main, в котором будет осуществляться основной запуск бота
11. Создание и реализация директории database для хранения запросов пользователей.
	- Создание и реализация модуля history

## Примеры работы запросов и получаемые данные:

Сразу оговорюсь, что, если у параметра __не указано__, что он __обязательный__, то он __не обязательный__.

### Первый запрос:

`https://rapidapi.com/api-sports/api/api-football/v3/standings`


#### Параметры запроса:

- 'league': int - id нужной лиги (у Испании он 140);

- 'season': integer = 4 characters YYYY - Обязательный параметр. Вводится год начала сезона в формате ГГГГ;

- 'team': integer - id нужной команды.

При параметрах: 

`params = {'league': 140, 'season': 2023, 'team': 547}`

Получим таблицу со всей информацией по чемпионату сезона 2023/2024 (чтобы не захламлять файл данными, в качестве примера только команда с первой строчки таблицы, по остальным командам данные отображаются):

{ "get": "standings", "parameters": { "league": "140", "season": "2023" }, "errors": [], "results": 1, "paging": { "current": 1, "total": 1 }, "response": [ { "league": { "id": 140, "name": "La Liga", "country": "Spain", "logo": "https://media.api-sports.io/football/leagues/140.png", "flag": "https://media.api-sports.io/flags/es.svg", "season": 2023, "standings": [ [ { "rank": 1, "team": { "id": 541, "name": "Real Madrid", "logo": "https://media.api-sports.io/football/teams/541.png" }, "points": 72, "goalsDiff": 44, "group": "Primera Divisi\u00f3n", "form": "WWDWD", "status": "same", "description": "Promotion - Champions League (Group Stage: )", "all": { "played": 29, "win": 22, "draw": 6, "lose": 1, "goals": { "for": 64, "against": 20 } }, "home": { "played": 14, "win": 12, "draw": 2, "lose": 0, "goals": { "for": 35, "against": 7 } }, "away": { "played": 15, "win": 10, "draw": 4, "lose": 1, "goals": { "for": 29, "against": 13 } }, "update": "2024-03-20T00:00:00+00:00" }, ] ] } } ] }

Если добавим команду:

`params = {'league': 140, 'season': 2023, 'team': 547}`

То получим данные о нужной команде (в данном случае это Жирона):

{ "get": "standings", "parameters": { "league": "140", "season": "2023", "team": "547" }, "errors": [], "results": 1, "paging": { "current": 1, "total": 1 }, "response": [ { "league": { "id": 140, "name": "La Liga", "country": "Spain", "logo": "https://media.api-sports.io/football/leagues/140.png", "flag": "https://media.api-sports.io/flags/es.svg", "season": 2023, "standings": [ [ { "rank": 3, "team": { "id": 547, "name": "Girona", "logo": "https://media.api-sports.io/football/teams/547.png" }, "points": 62, "goalsDiff": 25, "group": "Primera Divisi\u00f3n", "form": "LWLWL", "status": "same", "description": "Promotion - Champions League (Group Stage: )", "all": { "played": 29, "win": 19, "draw": 5, "lose": 5, "goals": { "for": 59, "against": 34 } }, "home": { "played": 14, "win": 11, "draw": 2, "lose": 1, "goals": { "for": 35, "against": 14 } }, "away": { "played": 15, "win": 8, "draw": 3, "lose": 4, "goals": { "for": 24, "against": 20 } }, "update": "2024-03-20T00:00:00+00:00" } ] ] } } ] }

### Второй запрос:

`https://api-football-v1.p.rapidapi.com/v3/teams/statistics`

#### Параметры запроса:

- 'league': int - Обязательный параметр. Указывается id нужной лиги (у Испании он 140);

- 'season': integer = 4 characters YYYY - Обязательный параметр. Вводится год начала сезона в формате ГГГГ;

- 'team': integer - Обязательный параметр. Указывается id нужной команды;

- 'date': string = YYYY-MM-DD - Дата, на которую нужна статистика. Вводится в формате ГГГГ-ММ-ДД.

Если указать только первые 3 параметра:

`params = {'league': 140, 'season': 2023, 'team': 529}`

То получим информацию по команде Барселона:

{ "get": "teams/statistics", "parameters": { "league": "140", "season": "2023", "team": "529" }, "errors": [], "results": 11, "paging": { "current": 1, "total": 1 }, "response": { "league": { "id": 140, "name": "La Liga", "country": "Spain", "logo": "https://media.api-sports.io/football/leagues/140.png", "flag": "https://media.api-sports.io/flags/es.svg", "season": 2023 }, "team": { "id": 529, "name": "Barcelona", "logo": "https://media.api-sports.io/football/teams/529.png" }, "form": "DWWWWWDWDWLWWDWLDWWWLWWDWWDWW", "fixtures": { "played": { "home": 15, "away": 14, "total": 29 }, "wins": { "home": 11, "away": 8, "total": 19 }, "draws": { "home": 1, "away": 6, "total": 7 }, "loses": { "home": 3, "away": 0, "total": 3 } }, "goals": { "for": { "total": { "home": 33, "away": 27, "total": 60 }, "average": { "home": "2.2", "away": "1.9", "total": "2.1" }, "minute": { "0-15": { "total": 4, "percentage": "7.02%" }, "16-30": { "total": 6, "percentage": "10.53%" }, "31-45": { "total": 5, "percentage": "8.77%" }, "46-60": { "total": 11, "percentage": "19.30%" }, "61-75": { "total": 12, "percentage": "21.05%" }, "76-90": { "total": 12, "percentage": "21.05%" }, "91-105": { "total": 7, "percentage": "12.28%" }, "106-120": { "total": null, "percentage": null } } }, "against": { "total": { "home": 19, "away": 15, "total": 34 }, "average": { "home": "1.3", "away": "1.1", "total": "1.2" }, "minute": { "0-15": { "total": 5, "percentage": "13.51%" }, "16-30": { "total": 3, "percentage": "8.11%" }, "31-45": { "total": 6, "percentage": "16.22%" }, "46-60": { "total": 8, "percentage": "21.62%" }, "61-75": { "total": 5, "percentage": "13.51%" }, "76-90": { "total": 6, "percentage": "16.22%" }, "91-105": { "total": 4, "percentage": "10.81%" }, "106-120": { "total": null, "percentage": null } } } }, "biggest": { "streak": { "wins": 5, "draws": 1, "loses": 1 }, "wins": { "home": "5-0", "away": "0-3" }, "loses": { "home": "3-5", "away": null }, "goals": { "for": { "home": 5, "away": 4 }, "against": { "home": 5, "away": 3 } } }, "clean_sheet": { "home": 8, "away": 4, "total": 12 }, "failed_to_score": { "home": 0, "away": 2, "total": 2 }, "penalty": { "scored": { "total": 4, "percentage": "100.00%" }, "missed": { "total": 0, "percentage": "0%" }, "total": 4 }, "lineups": [ { "formation": "4-3-3", "played": 23 }, { "formation": "4-2-3-1", "played": 3 }, { "formation": "3-4-1-2", "played": 2 }, { "formation": "3-4-2-1", "played": 1 } ], "cards": { "yellow": { "0-15": { "total": 1, "percentage": "1.54%" }, "16-30": { "total": 6, "percentage": "9.23%" }, "31-45": { "total": 14, "percentage": "21.54%" }, "46-60": { "total": 10, "percentage": "15.38%" }, "61-75": { "total": 6, "percentage": "9.23%" }, "76-90": { "total": 15, "percentage": "23.08%" }, "91-105": { "total": 13, "percentage": "20.00%" }, "106-120": { "total": null, "percentage": null } }, "red": { "0-15": { "total": null, "percentage": null }, "16-30": { "total": null, "percentage": null }, "31-45": { "total": 1, "percentage": "50.00%" }, "46-60": { "total": null, "percentage": null }, "61-75": { "total": 1, "percentage": "50.00%" }, "76-90": { "total": null, "percentage": null }, "91-105": { "total": null, "percentage": null }, "106-120": { "total": null, "percentage": null } } } } }

Если добавим дату:

`params = {'league': 140, 'season': 2023, 'team': 529, 'date': '2024-01-01'}`

То результат будет таким:

{ "get": "teams/statistics", "parameters": { "league": "140", "season": "2023", "date": "2024-01-01", "team": "529" }, "errors": [], "results": 11, "paging": { "current": 1, "total": 1 }, "response": { "league": { "id": 140, "name": "La Liga", "country": "Spain", "logo": "https://media.api-sports.io/football/leagues/140.png", "flag": "https://media.api-sports.io/flags/es.svg", "season": 2023 }, "team": { "id": 529, "name": "Barcelona", "logo": "https://media.api-sports.io/football/teams/529.png" }, "form": "DWWWWWDWDWLWWDWLDW", "fixtures": { "played": { "home": 10, "away": 8, "total": 18 }, "wins": { "home": 8, "away": 3, "total": 11 }, "draws": { "home": 0, "away": 5, "total": 5 }, "loses": { "home": 2, "away": 0, "total": 2 } }, "goals": { "for": { "total": { "home": 21, "away": 13, "total": 34 }, "average": { "home": "2.1", "away": "1.6", "total": "1.9" }, "minute": { "0-15": { "total": 3, "percentage": "9.38%" }, "16-30": { "total": 3, "percentage": "9.38%" }, "31-45": { "total": 3, "percentage": "9.38%" }, "46-60": { "total": 5, "percentage": "15.63%" }, "61-75": { "total": 5, "percentage": "15.63%" }, "76-90": { "total": 10, "percentage": "31.25%" }, "91-105": { "total": 3, "percentage": "9.38%" }, "106-120": { "total": null, "percentage": null } } }, "against": { "total": { "home": 11, "away": 10, "total": 21 }, "average": { "home": "1.1", "away": "1.3", "total": "1.2" }, "minute": { "0-15": { "total": 4, "percentage": "17.39%" }, "16-30": { "total": 3, "percentage": "13.04%" }, "31-45": { "total": 4, "percentage": "17.39%" }, "46-60": { "total": 2, "percentage": "8.70%" }, "61-75": { "total": 3, "percentage": "13.04%" }, "76-90": { "total": 5, "percentage": "21.74%" }, "91-105": { "total": 2, "percentage": "8.70%" }, "106-120": { "total": null, "percentage": null } } } }, "biggest": { "streak": { "wins": 5, "draws": 1, "loses": 1 }, "wins": { "home": "5-0", "away": "3-4" }, "loses": { "home": "2-4", "away": null }, "goals": { "for": { "home": 5, "away": 4 }, "against": { "home": 4, "away": 3 } } }, "clean_sheet": { "home": 5, "away": 2, "total": 7 }, "failed_to_score": { "home": 0, "away": 1, "total": 1 }, "penalty": { "scored": { "total": 2, "percentage": "100.00%" }, "missed": { "total": 0, "percentage": "0%" }, "total": 2 }, "lineups": [ { "formation": "4-3-3", "played": 12 }, { "formation": "4-2-3-1", "played": 3 }, { "formation": "3-4-1-2", "played": 2 }, { "formation": "3-4-2-1", "played": 1 } ], "cards": { "yellow": { "0-15": { "total": 1, "percentage": "2.27%" }, "16-30": { "total": 5, "percentage": "11.36%" }, "31-45": { "total": 9, "percentage": "20.45%" }, "46-60": { "total": 7, "percentage": "15.91%" }, "61-75": { "total": 2, "percentage": "4.55%" }, "76-90": { "total": 11, "percentage": "25.00%" }, "91-105": { "total": 9, "percentage": "20.45%" }, "106-120": { "total": null, "percentage": null } }, "red": { "0-15": { "total": null, "percentage": null }, "16-30": { "total": null, "percentage": null }, "31-45": { "total": 1, "percentage": "100.00%" }, "46-60": { "total": null, "percentage": null }, "61-75": { "total": null, "percentage": null }, "76-90": { "total": null, "percentage": null }, "91-105": { "total": null, "percentage": null }, "106-120": { "total": null, "percentage": null } } } } }

### Третий запрос:

`https://api-football-v1.p.rapidapi.com/v3/teams`

#### Параметры запроса:

- 'id': integer - Указывается id команды;

- 'name': string -Указывается название команды;

- 'league': int - Указывается id нужной лиги (у Испании он 140);

- 'season': integer = 4 characters YYYY - Вводится год начала сезона в формате ГГГГ;

- 'country': string - Указывается страна команды;

- 'code': string = 3 characters - Код команды из 3 заглавных букв;

- 'venue': integer - Указывается id стадиона;

- 'search': string >= 3 characters - Код команды или страны из 3 букв (по аналогии с параметром 'code').

Так как в рамках проекта нам нужно будет отображать либо все команды, либо что-то одно, то примера будет два. Параметры первого:

`params = {'league': 140, 'season': 2023}`

Получаем информацию по всем командам (тут добавлены только первые две, чтобы не нагромождать данными файл):

{ "get": "teams", "parameters": { "league": "140", "season": "2023" }, "errors": [], "results": 20, "paging": { "current": 1, "total": 1 }, "response": [ { "team": { "id": 529, "name": "Barcelona", "code": "BAR", "country": "Spain", "founded": 1899, "national": false, "logo": "https://media.api-sports.io/football/teams/529.png" }, "venue": { "id": 19939, "name": "Estadi Ol\u00edmpic Llu\u00eds Companys", "address": "Carrer de l'Estadi", "city": "Barcelona", "capacity": 55926, "surface": "grass", "image": "https://media.api-sports.io/football/venues/19939.png" } }, { "team": { "id": 530, "name": "Atletico Madrid", "code": "MAD", "country": "Spain", "founded": 1903, "national": false, "logo": "https://media.api-sports.io/football/teams/530.png" }, "venue": { "id": 19217, "name": "Est\u00e1dio C\u00edvitas Metropolitano", "address": "Rosas", "city": "Madrid", "capacity": 70460, "surface": "grass", "image": "https://media.api-sports.io/football/venues/19217.png" } }, ] }


Параметры второго:

`params = {'league': 140, 'season': 2023, 'name': 'Real Madrid'}`

Получаем данные по команде Реал Мадрид:

{ "get": "teams", "parameters": { "league": "140", "name": "Real Madrid", "season": "2023" }, "errors": [], "results": 1, "paging": { "current": 1, "total": 1 }, "response": [ { "team": { "id": 541, "name": "Real Madrid", "code": "REA", "country": "Spain", "founded": 1902, "national": false, "logo": "https://media.api-sports.io/football/teams/541.png" }, "venue": { "id": 1456, "name": "Estadio Santiago Bernab\u00e9u", "address": "Avenida de Concha Espina 1, Chamart\u00edn", "city": "Madrid", "capacity": 85454, "surface": "grass", "image": "https://media.api-sports.io/football/venues/1456.png" } } ] }


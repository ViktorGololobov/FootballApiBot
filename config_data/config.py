import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN") # ключ от тестового бота, нужно будет поменять
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ('start', 'Запустить бота'),
    ('help', 'Помощь'),
    ('lowstat_champ', 'Наименьший показатель чемпионата'),
    ('highstat_champ', 'Наибольший показатель чемпионата'),
    ('custom_champ', 'Информация по показателю в указанном диапазоне'),
    ('stadiums', 'Стадионы команд'),
    ('team_statistics', 'Статистика команды'),
    ('history', 'История запросов')
)

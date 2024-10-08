from typing import Dict
from .football_api import get_request_for_season


LEAGUE = 140
SEASON = get_request_for_season('https://api-football-v1.p.rapidapi.com/v3/leagues/seasons')['response'][-3]
NAME = ''
TEAM = int()

methods_endswith_list = ['/v3/standings', '/v3/teams', '/v3/teams/statistics']

params_dict: Dict[str, Dict] = {
    'standings_and_all_stadiums':
        {
            'league': LEAGUE,
            'season': SEASON
        },
    'teams':
        {
            'league': LEAGUE,
            'season': SEASON,
            'name': NAME
        },
    'teams_statistics':
        {
            'league': LEAGUE,
            'season': SEASON,
            'team': TEAM
        }
}

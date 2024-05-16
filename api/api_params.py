from typing import Dict


LEAGUE = 140
SEASON = 2023
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

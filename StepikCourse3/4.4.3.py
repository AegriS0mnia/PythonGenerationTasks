import json

club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
         "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}

club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
         "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}

club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
         "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}

with open('data_4_4_3.json', 'w', encoding='utf-8') as _4_4_3:
    clubs = [club1, club2, club3]

    json.dump(clubs, _4_4_3, indent=3)

import json
from nba_api.live.nba.endpoints import scoreboard

"""
This is a test and should be handled by the frontend dynamically
realistically and is proof of concept for what I'm looking for
"""


class Live:
    def __init__(self):
        pass

    def live_teams(self):
        games = scoreboard.ScoreBoard()
        score = games.get_json()
        scores = json.loads(score)
        base = scores["scoreboard"]["games"]
        for i in range(len(base)):
            return [
                {base[i]["homeTeam"]["teamCity"]},
                {base[i]["homeTeam"]["teamName"]},
                {base[i]["awayTeam"]["teamCity"]},
                {base[i]["awayTeam"]["teamName"]},
            ]

    def live_leaders(self):
        games = scoreboard.ScoreBoard()

        score = games.get_json()
        scores = json.loads(score)

        # a base variable to step through json
        base = scores["scoreboard"]["games"]

        # loops through the base value to extract specifics
        for i in range(len(base)):
            # need to account for accented characters for names
            print(f"Player: {base[i]['gameLeaders']['homeLeaders']['name']}")
            print(f"Points: {base[i]['gameLeaders']['homeLeaders']['points']}")
            print(f"Rebounds: {base[i]['gameLeaders']['homeLeaders']['rebounds']}")
            print(f"Assists: {base[i]['gameLeaders']['homeLeaders']['assists']}")
            print(f"Player: {base[i]['gameLeaders']['awayLeaders']['name']}")
            print(f"Points: {base[i]['gameLeaders']['awayLeaders']['points']}")
            print(f"Rebounds: {base[i]['gameLeaders']['awayLeaders']['rebounds']}")
            print(f"Assists: {base[i]['gameLeaders']['awayLeaders']['assists']}")

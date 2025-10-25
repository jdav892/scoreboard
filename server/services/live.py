import json
from nba_api.live.nba.endpoints import scoreboard


class Live:
    def __init__(self) -> None:
        pass

    def live_teams(self) -> None:
        """
        This will be a similar implementation to below of teams currently playing to be displayed in a card format
        with their associated players and their stats to be rotated in and out with each other as games progress
        throughout the day.
        """
        games = scoreboard.ScoreBoard()
        score = games.get_json()
        scores = json.loads(score)
        base = scores["scoreboard"]["games"]
        for i in range(len(base)):
            print(
                f"{base[i]['homeTeam']['teamCity']} {base[i]['homeTeam']['teamName']}"
            )
            print(
                f"{base[i]['awayTeam']['teamCity']} {base[i]['awayTeam']['teamName']}"
            )

    def live_leaders(self) -> None:
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


live_runner = Live()
live_runner.live_teams()
live_runner.live_leaders()

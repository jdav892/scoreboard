from nba_api.live.nba.endpoints import scoreboard
import json


class Live:
    def __init__(self) -> None:
        pass

    def live_teams(self) -> None:
        """
        This will be a similar implementation to below of teams currently playing to be displayed in a card format
        with their associated players and their stats to be rotated in and out with each other as games progress
        throughout the day.
        """

    def live_leaders(self) -> None:
        # career = playercareerstats.PlayerCareerStats(player_id="203999")
        # data = career.get_json()

        games = scoreboard.ScoreBoard()

        score = games.get_json()
        scores = json.loads(score)

        # a base variable to step through json
        base = scores["scoreboard"]["games"]
        first = base[0]
        second = base[1]
        third = base[2]
        print(first)
        print(second)
        print(third)

        # loops through the base value to print scoreboard
        for i in range(len(base)):
            print(base[i]["gameLeaders"]["homeLeaders"]["name"])
            print(base[i]["gameLeaders"]["awayLeaders"]["name"])

        # home and away leader names
        # first_home_game_leader_name = first["gameLeaders"]["homeLeaders"]["name"]
        # first_away_game_leader_name = first["gameLeaders"]["awayLeaders"]["name"]
        #
        # second_home_game_leader_name = second["gameLeaders"]["homeLeaders"]["name"]
        # second_away_game_leader_name = second["gameLeaders"]["awayLeaders"]["name"]
        #
        # third_home_game_leader_name = third["gameLeaders"]["homeLeaders"]["name"]
        # third_away_game_leader_name = third["gameLeaders"]["awayLeaders"]["name"]
        #
        # print(first_home_game_leader_name)
        # print(first_away_game_leader_name)
        # print(second_home_game_leader_name)
        # print(second_away_game_leader_name)
        # print(third_home_game_leader_name)
        # print(third_away_game_leader_name)
        #


live_runner = Live()
live_runner.live_leaders()

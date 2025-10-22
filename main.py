# from nba_api.stats.endpoints import playercareerstats
from nba_api.live.nba.endpoints import scoreboard
import json


def main():
    # career = playercareerstats.PlayerCareerStats(player_id="203999")
    # data = career.get_json()

    games = scoreboard.ScoreBoard()

    score = games.get_json()
    scores = json.loads(score)

    # a base variable to step through json
    base = scores["scoreboard"]["games"]
    first = base[0]
    second = base[1]
    print(first)
    print(second)

    # loops through the base value to print scoreboard
    for i in range(len(base)):
        print(base[i])

    # home and away leader names
    home_game_leader_name = first["gameLeaders"]["homeLeaders"]["name"]
    away_game_leader_name = first["gameLeaders"]["awayLeaders"]["name"]

    print(home_game_leader_name)
    print(away_game_leader_name)


main()

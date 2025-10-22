from nba_api.live.nba.endpoints import scoreboard
import json


def live_teams():
    """
    This will be a similar implementation to below of teams currently playing to be displayed in a card format
    with their associated players and their stats to be rotated in and out with each other as games progress
    throughout the day.
    """


def live_leaders():
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


live_leaders()

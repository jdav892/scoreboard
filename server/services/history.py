from nba_api.stats.endpoints import playercareerstats
import json


class History:
    def __init__(self) -> None:
        pass

    def career_stats(self) -> None:
        player = playercareerstats.PlayerCareerStats(player_id="203999")

        player_career = player.get_json()

        player_career_stats = json.loads(player_career)

        print(player_career_stats)


player_history = History()

player_history.career_stats()

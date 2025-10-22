from nba_api.stats.endpoints import playercareerstats
import json


def career_stats():
    player = playercareerstats.PlayerCareerStats(player_id="203999")

    player_career = player.get_json()

    player_career_stats = json.loads(player_career)

    print(player_career_stats)


career_stats()

from fastapi import APIRouter, WebSocket
from nba_api.live.nba.endpoints import scoreboard
import asyncio

router = APIRouter()


@router.websocket("/sb/live-scores")
async def live_scores_socket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            scores = scoreboard.ScoreBoard()
            games = scores.games.get_dict()

            await websocket.send_json(games)

            await asyncio.sleep(10)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()

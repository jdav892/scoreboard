from fastapi import APIRouter, WebSocket
from nba_api.live.nba.endpoints import scoreboard
from starlette.websockets import WebSocketState
import asyncio

router = APIRouter()


@router.websocket("/sb/live-scores")
async def live_scores_socket(websocket: WebSocket):
    # using a polling approach to update every 3 seconds
    await websocket.accept()
    try:
        while True:
            scores = scoreboard.ScoreBoard()
            games = scores.games.get_dict()

            await websocket.send_json(games)

            await asyncio.sleep(3)
    except Exception as e:
        print(f"ws error: {e}")
    finally:
        if websocket.client_state != WebSocketState.DISCONNECTED:
            await websocket.close()


@router.websocket("/sb/live-leaders")
async def live_leaders_socket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            scores = scoreboard.ScoreBoard()
            # Need to reread the json for this
            games = scores.games.get_dict()

            await websocket.send_json(games)

            await asyncio.sleep(5)
    except Exception as e:
        print(f"ws error: {e}")
    finally:
        if websocket.client_state != WebSocketState.DISCONNECTED:
            await websocket.close()

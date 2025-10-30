from fastapi import FastAPI

from routers import router
from nba_api.live.nba.endpoints import scoreboard

app = FastAPI()
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Start of something fun!, go to /sb"}


@app.get("/sb")
async def get_live_scores():
    board = scoreboard.ScoreBoard()
    games = board.games.get_dict()
    return games

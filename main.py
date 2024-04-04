import uuid

from fastapi import FastAPI

from models.player import Player
from models.course import Course, Get_Data


app = FastAPI()

players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}

@app.get("/players")
async def get_players(): 
    pass

@app.post("/players")
async def add_players():
    pass 

@app.put("/players/{id}")
async def update_players():
    pass

@app.delete("/players{id}")
async def delete_players(): 
    pass


@app.get("/courses")
async def get_courses(): 
    pass

@app.post("/courses")
async def add_courses():
    pass 

@app.put("/courses/{id}")
async def update_courses():
    pass

@app.delete("/courses{id}")
async def delete_courses(): 
    pass
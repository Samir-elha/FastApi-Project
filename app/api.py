from fastapi import FastAPI, Body

from fastapi.middleware.cors import CORSMiddleware
from app.model import MovieSchema
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost",
    "https://samir-elha2.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

genres = [
    {"id": 1, "genre": "Horror","movies": ["The Conjuring", "IT 2", "Annabelle"]},
    {"id": 2, "genre": "Comedy","movies": ["See How They Run", "Big Momma 2", "The Banshees of Inisherin"]}
]

@app.get("/", tags=["Home"])
def get_root() -> dict:
    return {
        "message": "Welcome to the okteto's app."
    }

@app.get("/genre", tags=["Genre"])
async def get_genres() -> dict:
    return {
        "data": genres
    }
@app.get("/genre/{id}", tags=["Genre"])
async def get_genre(id: int) -> dict:
    if id > len(genres) or id < 1:
        return {
            "error": "Invalid ID passed."
        }
    for genre in genres:
        if genre['id'] == id:
            return {
                "data": [
                    genre
                ]
            }

    return {
        "error": "No such genre with ID {} exist".format(id)
    }

@app.post("/genre", tags=["Genre"])
async def add_genre(genre: MovieSchema = Body(...)) -> dict:
    genre.id = len(genres) + 1
    genres.append(genre.dict())
    return {
        "message": "Genre added successfully."
    }
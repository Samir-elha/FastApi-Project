from fastapi import FastAPI, Body

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost",
    "https://samir-elha.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# recipes = [
#     {
#         "id": 1,
#         "name": "Donuts",
#         "ingredients": ["Flour", "Milk", "Sugar", "Vegetable Oil"]
#     }
# ]

genres = [
    {"id": 1, "genre": "Horror","movies": ["The Conjuring", "IT 2", "Annabelle"]},
    {"id": 2, "genre": "Comedy","movies": ["See How They Run", "Big Momma 2", "The Banshees of Inisherin"]}
]

@app.get("/", tags=["Home"])
def get_root() -> dict:
    return {
        "message": "Welcome to the okteto's app."
    }

# @app.get("/recipe", tags=["Recipe"])
# def get_recipes() -> dict:
#     return {
#         "data": recipes
#     }

@app.get("/genre", tags=["Genre"])
def get_genres() -> dict:
    return {
        "data": genres
    }
@app.get("/genre/{id}", tags=["Genre"])
def get_genre(id: int) -> dict:
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
        "error": "No such recipe with ID {} exist".format(id)
    }

# @app.get("/recipe/{id}", tags=["Recipe"])
# def get_recipe(id: int) -> dict:
#     if id > len(recipes) or id < 1:
#         return {
#             "error": "Invalid ID passed."
#         }
#
#     for recipe in recipes:
#         if recipe['id'] == id:
#             return {
#                 "data": [
#                     recipe
#                 ]
#             }
#
#     return {
#         "error": "No such recipe with ID {} exist".format(id)
#     }
#

class MovieSchema(BaseModel):
    id: int
    genre: str
    movies: [str]

@app.post("/genre", tags=["Genre"])
def add_recipe(genre: MovieSchema = Body(...)) -> dict:
    genre.id = len(genres) + 1
    genres.append(genre.dict())
    return {
        "message": "Recipe added successfully."
    }
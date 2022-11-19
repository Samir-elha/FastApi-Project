from pymongo import MongoClient
from bson import ObjectId
from decouple import config

connection_details = config("DB_HOST")

client = MongoClient(connection_details)

database = client.recipes

movie_collection = database.get_collection('movies_collection')

def parse_movie_data(movie) -> dict:
    return {
        "id": str(movie["_id"]),
        "genre": movie["genre"],
        "name": movie["name"]
    }

def save_movie(movie_data: dict) -> dict:
    movie = movie_collection.insert_one(movie_data).inserted_id
    return {
        "id": str(movie)
    }

def get_single_movie(id: str) -> dict:
    movie = movie_collection.find_one({"_id": ObjectId(id)})
    if movie:
        return parse_movie_data(movie)

def get_all_movies() -> list:
    movies = []
    for recipe in movie_collection.find():
        movies.append(parse_movie_data(recipe))

    return movies

def update_movie_data(id: str, data: dict):
    movie = movie_collection.find_one({"_id": ObjectId(id)})
    if movie:
        movie_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True

def remove_movie(id: str):
    movie = movie_collection.find_one({"_id": ObjectId(id)})
    if movie:
        movie_collection.delete_one({"_id": ObjectId(id)})
        return True
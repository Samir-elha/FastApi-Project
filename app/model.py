from pydantic import BaseModel, Field
from typing import Optional, List


class MovieSchema(BaseModel):
    id: Optional[int]
    genre: str = Field(...)
    movies: List[str] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Horror",
                "movies": ["The Conjuring", "IT 2", "Annabelle"]
            }
        }


class UpdateMovieSchema(BaseModel):
    genre: Optional[str]
    movies: Optional[List[str]]

    class Config:
        schema_extra = {
            "example": {
                "Genre": "Comedy",
                "movies": ["See How They Run", "Big Momma 2", "The Banshees of Inisherin"]
            }
        }
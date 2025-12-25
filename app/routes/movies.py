from models import Movie
from typing import Any
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

movie_router = APIRouter()

@movie_router.get("/movies")
def list_movies(request: Request):
    movie_list = []
    for movie in Movie.select():
        movie_list.append(movie.to_json())
    return JSONResponse(content={ "movies": movie_list })

@movie_router.get("/movies/{id}")
def get_movie(id: int):
    movie = Movie.get(Movie.id == id)
    if movie:
        return JSONResponse(content={ "movie": movie.to_json() })
    return JSONResponse(content={ "error": "err" })


@movie_router.post("/movies")
def add_movie(params: dict[str, Any]):
    movie = Movie(title=params['title'], year=params['year'], actors=params['actors'])
    if movie.save():
        return JSONResponse(content={ "message": "Movie added successfully" })
    return JSONResponse(content={ "error": "err" })

@movie_router.put("/movies/{id}")
def update_movie(id: int, params: dict[str, Any]):
    query = Movie.update(title=params['title'], year=params['year'], actors=params['actors']).where(Movie.id == id)
    if query.execute():
        return JSONResponse(content={ "message": "Movie updated successfully" })
    return JSONResponse(content={ "error": "err" })

@movie_router.delete("/movies/{id}")
def delete_movie(id: int):
    movie = Movie.get(Movie.id == id)
    if movie.delete_instance():
        return JSONResponse(content={ "message": "Movie deleted successfully" })
    return JSONResponse(content={ "error": "err" })

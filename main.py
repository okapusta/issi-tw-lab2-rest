from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from models import Movie
from lib.nominatim import Nominatim
from typing import Any

app = FastAPI()

@app.route("/")
def read_root(request: Request):
    return JSONResponse(content={ "message": "Hello world!" })

@app.get("/sum")
def sum(x: int = 0, y: int = 10):
    return JSONResponse(content={"result": x+y})

@app.get("/geocode")
def sum(lat: float, lon: float):
    nominatim = Nominatim(lat, lon)
    result = nominatim.call()

    return JSONResponse(content={ "result": result })

@app.get("/movies")
def list_movies(request: Request):
    movie_list = []
    for movie in Movie.select():
        movie_list.append(movie.to_json())
    return JSONResponse(content={ "movies": movie_list })

@app.get("/movies/{id}")
def get_movie(id: int):
    movie = Movie.get(Movie.id == id)
    if movie:
        return JSONResponse(content={ "movie": movie.to_json() })
    return JSONResponse(content={ "error": "err" })


@app.post("/movies")
def add_movie(params: dict[str, Any]):
    movie = Movie(title=params['title'], year=params['year'], actors=params['actors'])
    if movie.save():
        return JSONResponse(content={ "message": "Movie added successfully" })
    return JSONResponse(content={ "error": "err" })

@app.put("/movies/{id}")
def update_movie(id: int, params: dict[str, Any]):
    query = Movie.update(title=params['title'], year=params['year'], actors=params['actors']).where(Movie.id == id)
    if query.execute():
        return JSONResponse(content={ "message": "Movie updated successfully" })
    return JSONResponse(content={ "error": "err" })

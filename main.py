from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from models import Movie
from lib.nominatim import Nominatim

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


@app.route("/movies", methods=['GET'])
def list_movies(request: Request):
    movie_list = []
    for movie in Movie.select():
        movie_list.append(movie.to_json())
    return JSONResponse(content={ "movies": movie_list })

# @app.route("/movies", methods=['POST'])
# def create_movie():
#     movie = Movie(
#         title=request.form.get('title'),
#         year=request.form.get('year'),
#         actors=request.form.get('actors')
#     )
#     if movie.valid():
#         manager = DatabaseManager(dataclass=Movie)
#         manager.create_movie(movie)
#         return redirect("/")
#     else:
#         return redirect('/movies/new')

# @app.route("/movies-destroy", methods=['POST'])
# def destroy_movie():
#     movies_to_remove_ids = request.form.getlist('movies-to-remove')
#     # app.logger.debug('movies to remove', list(movies_to_remove_ids))
#     manager = DatabaseManager(dataclass=Movie)
#     manager.destroy_movies(list(movies_to_remove_ids))
#     return redirect("/")

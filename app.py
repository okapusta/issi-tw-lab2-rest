from flask import Flask, render_template, redirect, request
from models import Movie
from lib.database_manager import DatabaseManager

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html", movies=__fetch_movies())

@app.route("/movies/new", methods=['GET'])
def new_movie():
    return render_template("new.html")

@app.route("/movies", methods=['POST'])
def create_movie():
    movie = Movie(
        title=request.form.get('title'),
        year=request.form.get('year'),
        actors=request.form.get('actors')
    )
    if movie.valid():
        __create_movie(movie)
        return redirect("/")
    else:
        pass

def __fetch_movies():
    manager = DatabaseManager(dataclass=Movie)
    return manager.list_movies()

def __create_movie(movie):
    manager = DatabaseManager(dataclass=Movie)
    manager.create_movie(movie)


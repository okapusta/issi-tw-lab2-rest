from flask import Flask, render_template
from models import Movie
from lib.database_manager import DatabaseManager

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html", movies=__fetch_movies())

@app.route("/movies/new", methods=['GET'])
def new_movie():
    return render_template("new.html")

def __fetch_movies():
    manager = DatabaseManager(dataclass=Movie)
    movies = manager.list_movies()
    return movies

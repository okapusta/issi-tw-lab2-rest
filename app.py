from flask import Flask, render_template
from models import Movie
from lib.database_manager import DatabaseManager

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html", movies=__fetch_movies())

def __fetch_movies():
    manager = DatabaseManager(dataclass=Movie)
    movies = manager.list_movies()
    return movies

import sqlite3

class DatabaseManager():
  def __init__(self, dataclass=None):
    self.db = sqlite3.connect('movies.db')
    self.cursor = self.db.cursor()
    self.dataclass = dataclass

  def list_movies(self):
    movies = []
    self.cursor.execute('SELECT * FROM movies')
    for row in self.cursor:
      movies.append(self.dataclass(id=row[0], title=row[1], year=row[2], actors=row[3]))

    return movies

  def create_movie(self, movie):
    self.cursor.execute(f'INSERT INTO movies (title, year, actors) VALUES ("{movie.title}", "{movie.year}", "{movie.actors}")')
    self.db.commit()

  def destroy_movies(self, ids_to_remove):
    self.cursor.execute(f'DELETE FROM movies WHERE id IN (?)', ids_to_remove)
    self.db.commit()

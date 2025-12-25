from models import Movie
class MovieRepository:
  @classmethod
  def list_movies(cls):
    movie_list = []
    for movie in Movie.select():
        movie_list.append(movie.to_json())
    return movie_list

  @classmethod
  def get_movie():
     pass

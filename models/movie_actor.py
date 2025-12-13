from peewee import *
from .base_model import BaseModel
from .movie import Movie
from .actor import Actor

class MovieActor(BaseModel):
  movie_id = ForeignKeyField(Movie)
  actor_id = ForeignKeyField(Actor)

  class Meta:
    table_name = 'movie_actors'

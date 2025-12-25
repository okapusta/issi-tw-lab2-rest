from peewee import *
from .base_model import BaseModel
from .actor import Actor
class Movie(BaseModel):
  actors = TextField("actors")
  new_actors = ManyToManyField(Actor, backref='movies')

  title = CharField()
  director = CharField()
  year = IntegerField()
  description = TextField()

  class Meta:
    table_name = 'movies'

  def to_json(self):
    return {
      "id": self.id,
      "title": self.title,
      "year": self.year,
      "actors": self.actors
    }

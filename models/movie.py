from peewee import *
from .base_model import BaseModel
from .actor import Actor
class Movie(BaseModel):
  actors = ManyToManyField(Actor, backref='movies')

  title = CharField()
  director = CharField()
  year = IntegerField()
  description = TextField()

  class Meta:
    table_name = 'movie'

  def to_json(self):
    return {
      "id": self.id,
      "title": self.title,
      "year": self.year,
      "director": self.director,
      "description": self.description,
      "actors": list(map(lambda a: a.to_json(), self.actors))
    }

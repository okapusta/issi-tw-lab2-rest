from peewee import *
from .base_model import BaseModel

class Movie(BaseModel):
  title = CharField()
  year = IntegerField()
  actors = CharField()

  class Meta:
    table_name = 'movies'

  def to_json(self):
    return {
      "id": self.id,
      "title": self.title,
      "year": self.year,
      "actors": self.actors
    }

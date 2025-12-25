from peewee import *
from .base_model import BaseModel

class Actor(BaseModel):
  name = CharField()
  surname = IntegerField()

  class Meta:
    table_name = 'actor'

  def to_json(self):
    return {
      "id": self.id,
      "name": self.name,
      "surname": self.surname,
    }

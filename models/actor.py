from peewee import *
from .base_model import BaseModel

class Actor(BaseModel):
  name = CharField()
  surname = IntegerField()

  class Meta:
    table_name = 'actors'

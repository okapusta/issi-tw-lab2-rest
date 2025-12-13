from peewee import *

db = SqliteDatabase('movies.db')

class BaseModel(Model):
  class Meta:
    database = db

db.connect()

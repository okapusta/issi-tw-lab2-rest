from peewee import *

db = SqliteDatabase('movies-extended.db')

class BaseModel(Model):
  class Meta:
    database = db

db.connect()

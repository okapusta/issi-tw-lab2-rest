from peewee import *

db = SqliteDatabase('movies.db')

class Movie(Model):
  title = CharField()
  year = IntegerField()
  actors = CharField()

  class Meta:
    database = db
    table_name = 'movies'

  def to_json(self):
    return {
      "id": self.id,
      "title": self.title,
      "year": self.year,
      "actors": self.actors
    }

db.connect()

from models import Actor, Movie

class ActorRepository:
  @classmethod
  def list_actors(cls):
    actor_list = []
    for actor in Actor.select():
        actor_list.append(actor.to_json())
    return actor_list

  @classmethod
  def movie_actors(cls, id: int):
    movie = Movie.get_by_id(id)
    actor_list = []
    for actor in movie.actors:
        actor_list.append(actor.to_json())
    return actor_list

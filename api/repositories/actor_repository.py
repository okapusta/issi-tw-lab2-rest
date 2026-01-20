from models import Actor, Movie
from typing import Any

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

  @classmethod
  def create_actor(cls, params: dict[str, Any]):
    actor = Actor(name=params["name"], surname=params["surname"])
    if actor.save():
      return actor, True
    else:
       return None, False

  @classmethod
  def get_actor(cls, id: int):
     return Actor.get_by_id(id)

  @classmethod
  def get_actors(cls, ids: [int]):
     return Actor.select().where(Actor.id == ids)

  @classmethod
  def update_actor(cls, actor: Actor, params: dict[str, Any]):
    # if actor.update(params):
    #    return actor, True
    # return None, False
    query = Actor.update(name=params['name'], surname=params['surname']).where(Actor.id == actor.id)
    if query.execute():
       return actor, True
    return None, False


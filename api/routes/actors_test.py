import os
import sys

sys.path.append(os.path.dirname("__file__"))

from fastapi.testclient import TestClient
from api.repositories import ActorRepository

from main import app
from models import Actor, Movie

client = TestClient(app)

def test_list_actors():
  response = client.get("/actors")
  assert response.status_code == 200
  assert response.json()["actors"]
  actors = response.json()["actors"]
  assert len(actors) > 1

def test_create_actor():
  response = client.post("/actors", json={
    "name": "Oskar",
    "surname": "Tester"
  }, headers={
    "Content-Type": "application/json"
  })
  assert response.status_code == 200
  actor_id = response.json()["actor"]["id"]
  assert actor_id
  actor = ActorRepository.get_actor(actor_id)
  assert actor.id == actor_id


def test_update_actor():
  response = client.put("/actors/20", json={
    "name": "Oskar",
    "surname": "Tester 2"
  }, headers={
    "Content-Type": "application/json"
  })
  assert response.status_code == 200
  actor_id = response.json()["actor"]["id"]
  assert actor_id
  actor = ActorRepository.get_actor(actor_id)
  assert actor.surname == "Tester 2"

def test_delete_actor():
  actor = Actor(name="tester", surname="tobedeleted")
  actor.save()
  response = client.delete(f"/actors/{actor.id}")
  assert response.status_code == 200
  try:
    actor = ActorRepository.get_actor(actor.id)
  except Exception as ex:
    # assert ex.args == "instance matching query does not exist"
    assert ex

def test_assign_actor():
  actor = Actor(name="tester", surname="tester")
  other_actor = Actor(name="tester", surname="tester")
  actor.save()
  response = client.put(f"/movies/4/actors", json={
    "actor_ids": [actor.id, other_actor.id]
  }, headers={
    "Content-Type": "application/json"
  })
  assert response.status_code == 200
  movie = Movie.get_by_id(4)
  movie.actors

def test_movie_actors():
  response = client.get("/movies/4/actors")
  assert response.status_code == 200
  assert response.json()["actors"]
  actors = response.json()["actors"]
  assert len(actors) >= 1

import os
import sys

sys.path.append(os.path.dirname("__file__"))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_actors():
  response = client.get("/actors")
  assert response.status_code == 200
  assert response.json()["actors"]
  actors = response.json()["actors"]
  assert len(actors) > 1

def test_create_actor():
  pass

def test_update_actor():
  pass

def test_delete_actor():
  pass

def test_assign_actor():
  pass

def test_movie_actors():
  response = client.get("/movies/4/actors")
  assert response.status_code == 200
  assert response.json()["actors"]
  actors = response.json()["actors"]
  assert len(actors) > 1

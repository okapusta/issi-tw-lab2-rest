import os
import sys

sys.path.append(os.path.dirname("__file__"))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_movies():
  response = client.get("/movies")
  assert response.status_code == 200
  assert response.json()["movies"]
  movies = response.json()["movies"]
  assert len(movies) > 1

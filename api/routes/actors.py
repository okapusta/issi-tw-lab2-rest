from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from api.repositories import ActorRepository
from typing import Any
from models import Movie

actor_router = APIRouter()

@actor_router.get("/actors")
def list_actors(request: Request):
    return JSONResponse(content={ "actors": ActorRepository.list_actors() })

@actor_router.post("/actors")
def create_actor(params: dict[str, Any]):
    actor, success = ActorRepository.create_actor(params)
    if success:
      return JSONResponse(content={ "actor": actor.to_json() })
    else:
      return JSONResponse(content={ "error": "invalid" })

@actor_router.put("/actors/{id}")
def update_actor(id: int, params: dict[str, Any]):
    actor = ActorRepository.get_actor(id)
    if actor is None:
       return JSONResponse(content={ "error": "not found" }, status=404)
    updated, success = ActorRepository.update_actor(actor, params)
    if success:
      return JSONResponse(content={ "actor": updated.to_json() })
    else:
      return JSONResponse(content={ "error": "invalid" })

@actor_router.delete("/actors/{id}")
def update_actor(id: int):
    actor = ActorRepository.get_actor(id)
    if actor is None:
       return JSONResponse(content={ "error": "not found" }, status=404)

    if actor.delete_instance():
      return JSONResponse(content={ "success": True })
    else:
      return JSONResponse(content={ "error": "invalid" })

@actor_router.put("/movies/{id}/actors")
def movie_actors(id: int, params: dict[str, Any]):
    movie = Movie.get_by_id(id)
    if movie is None:
       return JSONResponse(content={ "error": "not found" }, status=404)
    actors = ActorRepository.get_actors(params["actor_ids"])
    if actors is None:
       return JSONResponse(content={ "error": "not found" }, status=404)
    movie.actors = actors
    if movie.save():
       return JSONResponse(content={ "success": True })
    return JSONResponse(content={ "error": "invalid" })

@actor_router.get("/movies/{id}/actors")
def movie_actors(id: int):
    return JSONResponse(content={ "actors": ActorRepository.movie_actors(id) })

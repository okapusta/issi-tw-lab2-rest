from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from api.repositories import ActorRepository

actor_router = APIRouter()

@actor_router.get("/actors")
def list_actors(request: Request):
    return JSONResponse(content={ "actors": ActorRepository.list_actors() })

@actor_router.get("/movies/{id}/actors")
def movie_actors(id: int):
    return JSONResponse(content={ "actors": ActorRepository.movie_actors(id) })

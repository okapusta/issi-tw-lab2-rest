from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import heathcheck_router, calculator_router, geolocator_router, movie_router, actor_router

origins = [
    "http://localhost:8888",
    "*" # Yuck :)
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(heathcheck_router, tags=["healthcheck"])
app.include_router(calculator_router, tags=["calculator"])
app.include_router(geolocator_router, tags=["geolocator"])
app.include_router(movie_router, tags=["movies"])
app.include_router(actor_router, tags=["actors"])

from fastapi import FastAPI

from api import heathcheck_router, calculator_router, geolocator_router, movie_router

app = FastAPI()
app.include_router(heathcheck_router, tags=["healthcheck"])
app.include_router(calculator_router, tags=["calculator"])
app.include_router(geolocator_router, tags=["geolocator"])
app.include_router(movie_router, tags=["movies"])

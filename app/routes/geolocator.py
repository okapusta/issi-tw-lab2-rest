from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from lib.nominatim import Nominatim

geolocator_router = APIRouter()

@geolocator_router.get("/geocode")
def sum(lat: float, lon: float):
    nominatim = Nominatim(lat, lon)
    result = nominatim.call()

    return JSONResponse(content={ "result": result })

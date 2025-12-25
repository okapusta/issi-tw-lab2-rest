from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

calculator_router = APIRouter()

@calculator_router.get("/sum")
def sum(x: int = 0, y: int = 10):
    return JSONResponse(content={"result": x+y})

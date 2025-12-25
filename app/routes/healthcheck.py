from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

heathcheck_router = APIRouter()

@heathcheck_router.route("/")
def read_root(request: Request):
    return JSONResponse(content={ "message": "Hello world!" })

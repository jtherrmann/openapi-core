from fastapi import FastAPI
from openapi_core.contrib.starlette.middlewares import (
    StarletteOpenAPIMiddleware,
)

from fastapiproject.openapi import openapi
from fastapiproject.routers import pets


app = FastAPI()
app.add_middleware(StarletteOpenAPIMiddleware, openapi=openapi)
app.include_router(pets.router)

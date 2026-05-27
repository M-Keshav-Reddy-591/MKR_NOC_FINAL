from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from database import Base
from utils.security import (
    hash_password,
    verify_password
)
import models

from routers import (
    auth_routes,
    dashboard_routes,
    shift_routes,
)

Base.metadata.create_all(
    bind=engine
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

app.include_router(
    auth_routes.router
)
app.include_router(
    shift_routes.router
)
app.include_router(
    dashboard_routes.router
)


@app.get("/")
def root():

    return {
        "message":
        "NOC Attendance Backend Running"
    }
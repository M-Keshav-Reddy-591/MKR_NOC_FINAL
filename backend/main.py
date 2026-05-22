from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine

from routers import auth_routes
from routers import attendance_routes
from routers import shift_routes
from routers import shift_assignment_routes
from routers import dashboard_routes
from routers import swap_routes


# CREATE DATABASE TABLES
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NOC Attendance System"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ROUTERS
app.include_router(auth_routes.router)
app.include_router(attendance_routes.router)
app.include_router(shift_routes.router)
app.include_router(shift_assignment_routes.router)
app.include_router(dashboard_routes.router)
app.include_router(swap_routes.router)


@app.get("/")
def root():
    return {
        "message": "NOC Attendance Backend Running"
    }
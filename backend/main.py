from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from database import Base

import models
from routers import auth_routes
from routers import employee_routes
from routers import attendance_routes
from routers import shift_routes
from routers import shift_assignment_routes
from routers import dashboard_routes
from routers import leave_routes
from routers import report_routes
from routers import swap_routes
from routers import live_attendance_routes
from routers import export_routes
from routers import csv_upload_routes




# ==========================================
# CREATE DATABASE TABLES
# ==========================================

Base.metadata.create_all(bind=engine)


# ==========================================
# FASTAPI APP
# ==========================================

app = FastAPI(
    title="NOC Attendance Management System"
)


# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# ROUTES
# ==========================================

app.include_router(auth_routes.router)
app.include_router(attendance_routes.router)
app.include_router(employee_routes.router)
app.include_router(shift_routes.router)
app.include_router(shift_assignment_routes.router)
app.include_router(dashboard_routes.router)
app.include_router(leave_routes.router)
app.include_router(report_routes.router)
app.include_router(swap_routes.router)
app.include_router(live_attendance_routes.router)
app.include_router(export_routes.router)
app.include_router(csv_upload_routes.router)

# ==========================================
# ROOT
# ==========================================

@app.get("/")
def home():

    return {
        "message": "NOC Attendance Backend Running"
    }
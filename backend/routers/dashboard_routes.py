from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

import models

from database import SessionLocal


router = APIRouter(

    prefix="/api/v1/dashboard",

    tags=["Dashboard"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/admin")

def admin_dashboard(

    db: Session = Depends(get_db)
):

    total_employees = db.query(
        models.Employee
    ).count()

    total_attendance = db.query(
        models.Attendance
    ).filter(
        models.Attendance.date == date.today()
    ).count()

    total_shifts = db.query(
        models.Shift
    ).count()

    total_leaves = 0

    return {

        "total_employees": total_employees,

        "present_today": total_attendance,

        "total_shifts": total_shifts,

        "total_leaves": total_leaves
    }
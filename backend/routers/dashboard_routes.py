from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database import get_db

import models

from datetime import date

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"]
)


@router.get("/stats")
def get_dashboard_stats(
    db: Session = Depends(get_db)
):

    today = date.today()

    total_employees = db.query(
        models.Employee
    ).count()

    present_today = db.query(
        models.Attendance
    ).filter(
        models.Attendance.attendance_date
        == today
    ).count()

    absent_today = (
        total_employees - present_today
    )

    return {

        "total_employees":
        total_employees,

        "present_today":
        present_today,

        "absent_today":
        absent_today
    }


@router.get("/absent-employees")
def get_absent_employees(
    db: Session = Depends(get_db)
):

    today = date.today()

    attendance_ids = db.query(
        models.Attendance.employee_id
    ).filter(
        models.Attendance.attendance_date
        == today
    ).all()

    attendance_ids = [
        item[0]
        for item in attendance_ids
    ]

    absent_employees = db.query(
        models.Employee
    ).filter(
        ~models.Employee.id.in_(
            attendance_ids
        )
    ).all()

    return absent_employees
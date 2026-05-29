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


# =====================================================
# DASHBOARD STATS
# =====================================================

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

        "employees":
        total_employees,

        "present":
        present_today,

        "absent":
        absent_today,

        "total_employees":
        total_employees,

        "present_today":
        present_today,

        "absent_today":
        absent_today
    }


# =====================================================
# ABSENT EMPLOYEES
# =====================================================

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
        ~models.Employee.emp_id.in_(
            attendance_ids
        )
    ).all()

    result = []

    for employee in absent_employees:

        result.append({

            "employee_id":
            employee.emp_id,

            "employee_name":
            employee.emp_name,

            "department":
            employee.department,

            "designation":
            employee.designation

        })

    return result
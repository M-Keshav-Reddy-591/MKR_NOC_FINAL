from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models

from database import SessionLocal


router = APIRouter(

    prefix="/api/v1/reports",

    tags=["Reports"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# EMPLOYEE REPORT

@router.get("/employees")

def employee_report(

    db: Session = Depends(get_db)
):

    employees = db.query(models.Employee).all()

    report = []

    for emp in employees:

        attendance_count = db.query(
            models.Attendance
        ).filter(
            models.Attendance.employee_id == emp.id
        ).count()

        report.append({

            "emp_id": emp.emp_id,

            "emp_name": emp.emp_name,

            "department": emp.department,

            "designation": emp.designation,

            "attendance_count": attendance_count
        })

    return report


# ATTENDANCE REPORT

@router.get("/attendance")

def attendance_report(

    db: Session = Depends(get_db)
):

    attendance = db.query(
        models.Attendance
    ).all()

    return attendance


# DASHBOARD SUMMARY REPORT

@router.get("/summary")

def summary_report(

    db: Session = Depends(get_db)
):

    total_employees = db.query(
        models.Employee
    ).count()

    total_attendance = db.query(
        models.Attendance
    ).count()

    total_shifts = db.query(
        models.Shift
    ).count()

    total_leaves = db.query(
        models.Leave
    ).count()

    return {

        "total_employees": total_employees,

        "total_attendance": total_attendance,

        "total_shifts": total_shifts,

        "total_leaves": total_leaves
    }
from fastapi import APIRouter
from database import SessionLocal
import models

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"]
)

@router.get("/stats")
def get_dashboard_stats():

    db = SessionLocal()

    total_employees = db.query(
        models.Employee
    ).count()

    total_attendance = db.query(
        models.Attendance
    ).count()

    total_shifts = db.query(
        models.ShiftAssignment
    ).count()

    return {

        "total_employees": total_employees,
        "total_attendance": total_attendance,
        "total_shifts": total_shifts

    }

@router.get("/absent-employees")
def get_absent_employees():

    db = SessionLocal()

    employees = db.query(
        models.Employee
    ).all()

    attendance_records = db.query(
        models.Attendance
    ).all()

    present_ids = []

    for row in attendance_records:

        present_ids.append(
            row.employee_id
        )

    absent = []

    for emp in employees:

        if emp.id not in present_ids:

            absent.append({

                "emp_id": emp.emp_id,
                "emp_name": emp.emp_name

            })

    return absent
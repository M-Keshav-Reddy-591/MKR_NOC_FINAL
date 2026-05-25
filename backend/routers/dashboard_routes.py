from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
import models
from datetime import date

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"]
)

@router.get("/stats")
def get_dashboard_stats(db: Session = Depends(get_db)):

    today = date.today()

    total_employees = db.query(models.Employee).count()

    present_today = db.query(models.Attendance).filter(
        models.Attendance.attendance_date == today,
        models.Attendance.status == "Present"
    ).count()

    absent_today = total_employees - present_today

    total_leaves = db.query(models.Leave).filter(
        models.Leave.status == "Approved"
    ).count()

    total_shifts = db.query(models.Shift).count()

    attendance_percentage = 0

    if total_employees > 0:
        attendance_percentage = round(
            (present_today / total_employees) * 100,
            2
        )

    return {
        "total_employees": total_employees,
        "present_today": present_today,
        "absent_today": absent_today,
        "total_leaves": total_leaves,
        "total_shifts": total_shifts,
        "attendance_percentage": attendance_percentage
    }


@router.get("/recent-attendance")
def recent_attendance(db: Session = Depends(get_db)):

    records = db.query(models.Attendance).order_by(
        models.Attendance.id.desc()
    ).limit(10).all()

    result = []

    for record in records:

        employee = db.query(models.Employee).filter(
            models.Employee.id == record.employee_id
        ).first()

        result.append({
            "emp_id": employee.emp_id,
            "emp_name": employee.emp_name,
            "status": record.status,
            "date": record.attendance_date
        })

    return result
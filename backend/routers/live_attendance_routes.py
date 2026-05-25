from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models

router = APIRouter(
    prefix="/api/v1/live-attendance",
    tags=["Live Attendance"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_live_attendance(db: Session = Depends(get_db)):

    attendance = db.query(models.Attendance).all()

    result = []

    for item in attendance:

        employee = db.query(models.Employee).filter(
            models.Employee.id == item.employee_id
        ).first()

        result.append({
            "employee_name": employee.emp_name if employee else "Unknown",
            "department": employee.department if employee else "N/A",
            "status": item.status,
            "check_in": str(item.check_in),
            "check_out": str(item.check_out),
            "attendance_date": str(item.attendance_date)
        })

    return result
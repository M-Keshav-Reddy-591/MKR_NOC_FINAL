from fastapi import APIRouter
from database import SessionLocal
import models
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(
    prefix="/api/v1/attendance",
    tags=["Attendance"]
)

class AttendanceRequest(BaseModel):

    emp_id: str
    status: str

@router.post("/mark")
def mark_attendance(
    data: AttendanceRequest
):

    db = SessionLocal()

    employee = db.query(
        models.Employee
    ).filter(
        models.Employee.emp_id ==
        data.emp_id
    ).first()

    if not employee:

        return {
            "message": "Employee Not Found"
        }

    attendance = models.Attendance(

        employee_id=employee.id,

        status=data.status,

        check_in=datetime.now()

    )

    db.add(attendance)

    db.commit()

    return {
        "message": "Attendance Marked"
    }

@router.get("/{emp_id}")
def get_employee_attendance(
    emp_id: str
):

    db = SessionLocal()

    employee = db.query(
        models.Employee
    ).filter(
        models.Employee.emp_id ==
        emp_id
    ).first()

    if not employee:

        return []

    attendance = db.query(
        models.Attendance
    ).filter(
        models.Attendance.employee_id ==
        employee.id
    ).all()

    return attendance
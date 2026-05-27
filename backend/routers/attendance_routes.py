from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime
import models

router = APIRouter(
    prefix="/api/v1/attendance",
    tags=["Attendance"]
)

# =========================================
# EMPLOYEE MARK ATTENDANCE
# =========================================

@router.post("/mark")
def mark_attendance(
    data: dict,
    db: Session = Depends(get_db)
):

    employee_id = data.get(
        "employee_id"
    )

    today = datetime.today().date()

    existing = db.query(
        models.Attendance
    ).filter(
        models.Attendance.employee_id == employee_id,
        models.Attendance.attendance_date == today
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Attendance already marked today"
        )

    attendance = models.Attendance(

        employee_id=employee_id,
        attendance_date=today,
        status="Present",
        check_in=datetime.now()
    )

    db.add(attendance)

    db.commit()

    return {
        "message": "Attendance marked successfully"
    }

# =========================================
# GET EMPLOYEE ATTENDANCE
# =========================================

@router.get("/employee/{employee_id}")
def get_employee_attendance(
    employee_id: str,
    db: Session = Depends(get_db)
):

    attendance = db.query(
        models.Attendance
    ).filter(
        models.Attendance.employee_id == employee_id
    ).all()

    result = []

    for row in attendance:

        result.append({

            "id": row.id,
            "employee_id": row.employee_id,
            "attendance_date": str(row.attendance_date),
            "status": row.status,
            "check_in": str(row.check_in)
        })

    return result

# =========================================
# GET ALL ATTENDANCE
# =========================================

@router.get("/")
def get_all_attendance(
    db: Session = Depends(get_db)
):

    attendance = db.query(
        models.Attendance
    ).all()

    result = []

    for row in attendance:

        result.append({

            "id": row.id,
            "employee_id": row.employee_id,
            "attendance_date": str(row.attendance_date),
            "status": row.status,
            "check_in": str(row.check_in)
        })

    return result
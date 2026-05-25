from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, date

import models
import schemas

from database import SessionLocal

router = APIRouter(
    prefix="/api/v1/attendance",
    tags=["Attendance"]
)

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# MARK ATTENDANCE

@router.post("/mark")

def mark_attendance(
    attendance_data: schemas.AttendanceSchema,
    db: Session = Depends(get_db)
):

    employee = db.query(models.Employee).filter(
        models.Employee.id == attendance_data.employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    attendance = models.Attendance(

        employee_id=attendance_data.employee_id,

        date=date.today(),

        check_in=datetime.now(),

        status=attendance_data.status
    )

    db.add(attendance)

    db.commit()

    db.refresh(attendance)

    return {
        "message": "Attendance marked successfully"
    }


# GET ALL ATTENDANCE

@router.get("/all")

def get_attendance(
    db: Session = Depends(get_db)
):

    data = db.query(models.Attendance).all()

    return data
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

import database
import models

router = APIRouter(
    prefix="/api/v1/attendance",
    tags=["Attendance"]
)

@router.get("")
def get_attendance(
    db: Session = Depends(database.get_db)
):

    return db.query(models.Attendance).all()


@router.post("")
def mark_attendance(
    attendance_data: dict,
    db: Session = Depends(database.get_db)
):

    attendance = models.Attendance(
        emp_id=attendance_data["emp_id"],
        status=attendance_data["status"],
        date=date.today()
    )

    db.add(attendance)

    db.commit()

    db.refresh(attendance)

    return attendance


@router.get("/absent")
def absent_employees(
    db: Session = Depends(database.get_db)
):

    return db.query(models.Attendance).filter(
        models.Attendance.status == "Absent"
    ).all()
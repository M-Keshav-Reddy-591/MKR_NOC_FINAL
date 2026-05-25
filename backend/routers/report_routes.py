from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
import models

router = APIRouter(
    prefix="/api/v1/reports",
    tags=["Reports"]
)

@router.get("/all")
def all_reports(
    db: Session = Depends(database.get_db)
):

    reports = db.query(
        models.Attendance
    ).all()

    return reports


@router.get("/employee/{emp_id}")
def employee_reports(
    emp_id: str,
    db: Session = Depends(database.get_db)
):

    reports = db.query(
        models.Attendance
    ).filter(
        models.Attendance.emp_id == emp_id
    ).all()

    return reports
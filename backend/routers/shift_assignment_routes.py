from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

import database
import models

router = APIRouter(
    prefix="/api/v1/shift-assignments",
    tags=["Shift Assignments"]
)

@router.get("/{emp_id}")
def upcoming_shifts(
    emp_id: str,
    db: Session = Depends(database.get_db)
):

    shifts = db.query(
        models.ShiftAssignment
    ).filter(
        models.ShiftAssignment.employee_id == emp_id,
        models.ShiftAssignment.shift_date >= date.today()
    ).all()

    return shifts


@router.get("/history/{emp_id}")
def shift_history(
    emp_id: str,
    db: Session = Depends(database.get_db)
):

    history = db.query(
        models.ShiftAssignment
    ).filter(
        models.ShiftAssignment.employee_id == emp_id,
        models.ShiftAssignment.shift_date < date.today()
    ).all()

    return history
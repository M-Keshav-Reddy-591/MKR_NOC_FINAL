from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database import get_db

import models
import schemas

from auth import get_current_user


router = APIRouter(
    prefix="/api/v1/shift-assignment",
    tags=["Shift Assignment"]
)


# =====================================================
# ASSIGN SHIFT
# =====================================================

@router.post("/assign")
def assign_shift(
    shift_data: schemas.ShiftAssignSchema,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    employee = db.query(models.Employee).filter(
        models.Employee.id == shift_data.employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    shift = db.query(models.Shift).filter(
        models.Shift.id == shift_data.shift_id
    ).first()

    if not shift:

        raise HTTPException(
            status_code=404,
            detail="Shift not found"
        )

    assignment = models.ShiftAssignment(

        employee_id=shift_data.employee_id,

        shift_id=shift_data.shift_id,

        shift_date=shift_data.shift_date
    )

    db.add(assignment)

    db.commit()

    return {
        "message": "Shift assigned successfully"
    }


# =====================================================
# MY SCHEDULE
# =====================================================

@router.get("/my-schedule")
def my_schedule(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    assignments = db.query(models.ShiftAssignment).filter(
        models.ShiftAssignment.employee_id == current_user.id
    ).all()

    result = []

    for assignment in assignments:

        shift = db.query(models.Shift).filter(
            models.Shift.id == assignment.shift_id
        ).first()

        result.append({
            "date": assignment.shift_date,
            "shift_name": shift.shift_name,
            "start_time": shift.start_time,
            "end_time": shift.end_time
        })

    return result
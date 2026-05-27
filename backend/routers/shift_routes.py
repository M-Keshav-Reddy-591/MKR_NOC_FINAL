from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models

from database import get_db

router = APIRouter(

    prefix="/api/v1/shifts",

    tags=["Shifts"]
)

# =========================
# GET ALL SHIFTS
# =========================

@router.get("/")
def get_shifts(

    db: Session = Depends(get_db)

):

    shifts = db.query(
        models.ShiftAssignment
    ).all()

    result = []

    for shift in shifts:

        result.append({

            "id": shift.id,
            "employee_id": shift.employee_id,
            "shift_name": shift.shift_name,
            "shift_date": str(shift.shift_date),
            "start_time": str(shift.start_time),
            "end_time": str(shift.end_time),
            "is_holiday": shift.is_holiday,
            "holiday_note": shift.holiday_note
        })

    return result

# =========================
# CREATE SHIFT
# =========================

@router.post("/create")
def create_shift(

    data: dict,

    db: Session = Depends(get_db)

):

    shift = models.ShiftAssignment(

        employee_id=data["employee_id"],
        shift_name=data["shift_name"],
        shift_date=data["shift_date"],
        start_time=data["start_time"],
        end_time=data["end_time"],
        is_holiday=data["is_holiday"],
        holiday_note=data["holiday_note"]
    )

    db.add(shift)

    db.commit()

    return {

        "message": "Shift Assigned Successfully"
    }
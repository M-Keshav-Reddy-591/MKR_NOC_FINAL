from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
from datetime import date

router = APIRouter(
    prefix="/api/v1/manual-shifts",
    tags=["Manual Shift Assignment"]
)

# CREATE SHIFT

@router.post("/assign")

def assign_shift(
    data: dict,
    db: Session = Depends(get_db)
):

    employee_id = data.get("employee_id")
    shift_date = data.get("shift_date")
    shift_name = data.get("shift_name")
    start_time = data.get("start_time")
    end_time = data.get("end_time")
    is_holiday = data.get("is_holiday", False)
    holiday_note = data.get("holiday_note")
    assigned_by = data.get("assigned_by")

    # CHECK DUPLICATE SHIFT

    existing = db.query(
        models.ManualShiftAssignment
    ).filter(
        models.ManualShiftAssignment.employee_id == employee_id,
        models.ManualShiftAssignment.shift_date == shift_date
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Shift already assigned"
        )

    new_shift = models.ManualShiftAssignment(

        employee_id=employee_id,
        shift_date=shift_date,
        shift_name=shift_name,
        start_time=start_time,
        end_time=end_time,
        is_holiday=is_holiday,
        holiday_note=holiday_note,
        assigned_by=assigned_by
    )

    db.add(new_shift)

    # HOLIDAY LOG

    if is_holiday:

        holiday_log = models.HolidayWorkLog(

            employee_id=employee_id,
            work_date=shift_date,
            note=holiday_note
        )

        db.add(holiday_log)

    db.commit()

    return {
        "message": "Shift assigned successfully"
    }


# GET ALL SHIFTS

@router.get("/")

def get_all_shifts(
    db: Session = Depends(get_db)
):

    shifts = db.query(
        models.ManualShiftAssignment
    ).all()

    return shifts


# GET EMPLOYEE SHIFTS

@router.get("/{employee_id}")

def get_employee_shifts(
    employee_id: str,
    db: Session = Depends(get_db)
):

    shifts = db.query(
        models.ManualShiftAssignment
    ).filter(
        models.ManualShiftAssignment.employee_id == employee_id
    ).all()

    return shifts
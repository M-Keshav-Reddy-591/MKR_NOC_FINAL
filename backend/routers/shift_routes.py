from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database import get_db

import models
import schemas

from auth import get_current_user


router = APIRouter(
    prefix="/api/v1/shifts",
    tags=["Shifts"]
)


# =====================================================
# CREATE SHIFT
# =====================================================

@router.post("/create")
def create_shift(
    shift_data: schemas.ShiftCreateSchema,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    new_shift = models.Shift(

        shift_name=shift_data.shift_name,

        start_time=shift_data.start_time,

        end_time=shift_data.end_time
    )

    db.add(new_shift)

    db.commit()

    db.refresh(new_shift)

    return {
        "message": "Shift created successfully"
    }


# =====================================================
# GET ALL SHIFTS
# =====================================================

@router.get("/all")
def get_all_shifts(
    db: Session = Depends(get_db)
):

    shifts = db.query(models.Shift).all()

    result = []

    for shift in shifts:

        result.append({
            "id": shift.id,
            "shift_name": shift.shift_name,
            "start_time": shift.start_time,
            "end_time": shift.end_time,
            "is_active": shift.is_active
        })

    return result


# =====================================================
# DELETE SHIFT
# =====================================================

@router.delete("/delete/{shift_id}")
def delete_shift(
    shift_id: int,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    shift = db.query(models.Shift).filter(
        models.Shift.id == shift_id
    ).first()

    if not shift:

        raise HTTPException(
            status_code=404,
            detail="Shift not found"
        )

    db.delete(shift)

    db.commit()

    return {
        "message": "Shift deleted successfully"
    }
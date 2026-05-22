from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

import models
import schemas
import auth

from database import SessionLocal


router = APIRouter()


# ==========================================
# DATABASE
# ==========================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ==========================================
# CREATE SHIFT
# ADMIN ONLY
# ==========================================

@router.post("/create-shift")
def create_shift(
    shift: schemas.ShiftCreate,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    existing_shift = db.query(
        models.Shift
    ).filter(
        models.Shift.shift_name == shift.shift_name
    ).first()

    if existing_shift:

        raise HTTPException(
            status_code=400,
            detail="Shift already exists"
        )

    new_shift = models.Shift(
        shift_name=shift.shift_name,
        start_time=shift.start_time,
        end_time=shift.end_time,
        grace_minutes=shift.grace_minutes
    )

    db.add(new_shift)

    db.commit()

    db.refresh(new_shift)

    return {
        "message": "Shift Created Successfully"
    }


# ==========================================
# VIEW SHIFTS
# ==========================================

@router.get("/shifts")
def get_all_shifts(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.get_current_user
    )
):

    shifts = db.query(
        models.Shift
    ).all()

    return shifts


# ==========================================
# ASSIGN SHIFT
# ADMIN ONLY
# ==========================================

@router.post("/assign-shift")
def assign_shift(
    roster: schemas.RosterCreate,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    employee = db.query(
        models.Employee
    ).filter(
        models.Employee.emp_id == roster.emp_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    shift = db.query(
        models.Shift
    ).filter(
        models.Shift.id == roster.shift_id
    ).first()

    if not shift:

        raise HTTPException(
            status_code=404,
            detail="Shift not found"
        )

    existing_roster = db.query(
        models.Roster
    ).filter(
        models.Roster.emp_id == roster.emp_id,
        models.Roster.shift_date == roster.shift_date
    ).first()

    if existing_roster:

        raise HTTPException(
            status_code=400,
            detail="Shift already assigned"
        )

    new_roster = models.Roster(
        emp_id=roster.emp_id,
        shift_id=roster.shift_id,
        shift_date=roster.shift_date
    )

    db.add(new_roster)

    db.commit()

    db.refresh(new_roster)

    return {
        "message": "Shift Assigned Successfully"
    }


# ==========================================
# VIEW ROSTER
# ==========================================

@router.get("/roster")
def view_roster(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.get_current_user
    )
):

    roster = db.query(
        models.Roster
    ).all()

    return roster
# ==========================================
# GET ALL SHIFTS
# ==========================================

@router.get("/all")
def get_all_shifts(

    db: Session = Depends(get_db)
):

    return db.query(
        models.Shift
    ).all()
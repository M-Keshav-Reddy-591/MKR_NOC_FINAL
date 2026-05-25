from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

import models
import schemas

from database import SessionLocal


router = APIRouter(

    prefix="/api/v1/swaps",

    tags=["Shift Swaps"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# REQUEST SWAP

@router.post("/request")

def request_swap(

    swap_data: schemas.ShiftSwapSchema,

    db: Session = Depends(get_db)
):

    requester = db.query(models.Employee).filter(
        models.Employee.id == swap_data.requester_id
    ).first()

    if not requester:

        raise HTTPException(
            status_code=404,
            detail="Requester not found"
        )

    target = db.query(models.Employee).filter(
        models.Employee.id == swap_data.target_employee_id
    ).first()

    if not target:

        raise HTTPException(
            status_code=404,
            detail="Target employee not found"
        )

    swap = models.ShiftSwap(

        requester_id=swap_data.requester_id,

        target_employee_id=swap_data.target_employee_id,

        current_shift_id=swap_data.current_shift_id,

        requested_shift_id=swap_data.requested_shift_id
    )

    db.add(swap)

    db.commit()

    db.refresh(swap)

    return {
        "message": "Shift swap request created"
    }


# GET ALL SWAPS

@router.get("/all")

def get_swaps(

    db: Session = Depends(get_db)
):

    return db.query(models.ShiftSwap).all()


# APPROVE SWAP

@router.put("/approve/{swap_id}")

def approve_swap(

    swap_id: int,

    db: Session = Depends(get_db)
):

    swap = db.query(models.ShiftSwap).filter(
        models.ShiftSwap.id == swap_id
    ).first()

    if not swap:

        raise HTTPException(
            status_code=404,
            detail="Swap not found"
        )

    swap.status = "Approved"

    db.commit()

    return {
        "message": "Swap approved"
    }


# REJECT SWAP

@router.put("/reject/{swap_id}")

def reject_swap(

    swap_id: int,

    db: Session = Depends(get_db)
):

    swap = db.query(models.ShiftSwap).filter(
        models.ShiftSwap.id == swap_id
    ).first()

    if not swap:

        raise HTTPException(
            status_code=404,
            detail="Swap not found"
        )

    swap.status = "Rejected"

    db.commit()

    return {
        "message": "Swap rejected"
    }
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database import get_db

import models
import schemas

from auth import get_current_user


router = APIRouter(
    prefix="/api/v1/swaps",
    tags=["Shift Swaps"]
)


# =====================================================
# REQUEST SWAP
# =====================================================

@router.post("/request")
def request_swap(
    swap_data: schemas.ShiftSwapSchema,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    new_swap = models.ShiftSwap(

        requester_id=swap_data.requester_id,

        receiver_id=swap_data.receiver_id,

        requester_shift_id=swap_data.requester_shift_id,

        receiver_shift_id=swap_data.receiver_shift_id,

        reason=swap_data.reason
    )

    db.add(new_swap)

    db.commit()

    return {
        "message": "Swap request submitted"
    }


# =====================================================
# GET ALL SWAPS
# =====================================================

@router.get("/all")
def all_swaps(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    swaps = db.query(models.ShiftSwap).all()

    result = []

    for swap in swaps:

        result.append({
            "id": swap.id,
            "requester_id": swap.requester_id,
            "receiver_id": swap.receiver_id,
            "status": swap.status,
            "reason": swap.reason
        })

    return result


# =====================================================
# APPROVE SWAP
# =====================================================

@router.put("/approve/{swap_id}")
def approve_swap(
    swap_id: int,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    swap = db.query(models.ShiftSwap).filter(
        models.ShiftSwap.id == swap_id
    ).first()

    if not swap:

        raise HTTPException(
            status_code=404,
            detail="Swap not found"
        )

    swap.status = "approved"

    db.commit()

    return {
        "message": "Swap approved"
    }


# =====================================================
# REJECT SWAP
# =====================================================

@router.put("/reject/{swap_id}")
def reject_swap(
    swap_id: int,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    swap = db.query(models.ShiftSwap).filter(
        models.ShiftSwap.id == swap_id
    ).first()

    if not swap:

        raise HTTPException(
            status_code=404,
            detail="Swap not found"
        )

    swap.status = "rejected"

    db.commit()

    return {
        "message": "Swap rejected"
    }
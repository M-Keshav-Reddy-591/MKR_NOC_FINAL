from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database import get_db

import models
import auth

from datetime import date
from dependencies import get_current_user

router = APIRouter()


# ==========================================
# REQUEST SHIFT SWAP
# ==========================================

@router.post("/request-shift-swap")
def request_shift_swap(

    data: dict,

    db: Session = Depends(get_db),

    current_user: models.Employee = Depends(
        auth.get_current_user
    )
):

    # ======================================
    # FIND REQUESTER SHIFT
    # ======================================

    requester_shift = db.query(

        models.ShiftAssignment

    ).filter(

        models.ShiftAssignment.employee_id
        == data["requester_emp_id"],

        models.ShiftAssignment.shift_date
        == data["shift_date"]

    ).first()


    if not requester_shift:

        raise HTTPException(

            status_code=404,

            detail="Requester Shift Not Found"
        )


    # ======================================
    # FIND TARGET SHIFT
    # ======================================

    target_shift = db.query(

        models.ShiftAssignment

    ).filter(

        models.ShiftAssignment.employee_id
        == data["target_emp_id"],

        models.ShiftAssignment.shift_date
        == data["shift_date"]

    ).first()


    if not target_shift:

        raise HTTPException(

            status_code=404,

            detail="Target Shift Not Found"
        )


    # ======================================
    # CREATE SWAP REQUEST
    # ======================================

    swap = models.ShiftSwap(

        requester_emp_id=data["requester_emp_id"],

        target_emp_id=data["target_emp_id"],

        shift_date=data["shift_date"],

        requester_shift=requester_shift.shift_name,

        target_shift=target_shift.shift_name,

        reason=data.get("reason", ""),

        status="Pending"
    )


    db.add(swap)

    db.commit()

    db.refresh(swap)


    return {

        "message":
        "Shift Swap Request Created",

        "swap_id":
        swap.id
    }


# ==========================================
# VIEW SHIFT SWAPS
# ==========================================

@router.get("/shift-swaps")
def view_shift_swaps(

    db: Session = Depends(get_db)
):

    swaps = db.query(

        models.ShiftSwap

    ).all()


    return swaps


# ==========================================
# APPROVE SHIFT SWAP
# ==========================================

@router.put("/approve-shift-swap/{swap_id}")
def approve_shift_swap(

    swap_id: int,

    db: Session = Depends(get_db)
):

    swap = db.query(

        models.ShiftSwap

    ).filter(

        models.ShiftSwap.id == swap_id

    ).first()


    if not swap:

        raise HTTPException(

            status_code=404,

            detail="Swap Request Not Found"
        )


    swap.status = "Approved"

    db.commit()


    return {

        "message":
        "Shift Swap Approved"
    }


# ==========================================
# DECLINE SHIFT SWAP
# ==========================================

@router.put("/decline-shift-swap/{swap_id}")
def decline_shift_swap(

    swap_id: int,

    db: Session = Depends(get_db)
):

    swap = db.query(

        models.ShiftSwap

    ).filter(

        models.ShiftSwap.id == swap_id

    ).first()


    if not swap:

        raise HTTPException(

            status_code=404,

            detail="Swap Request Not Found"
        )


    swap.status = "Declined"

    db.commit()


    return {

        "message":
        "Shift Swap Declined"
    }
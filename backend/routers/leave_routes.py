from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

import models
import schemas

from database import SessionLocal
import auth

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
# APPLY LEAVE
# ==========================================

@router.post("/apply-leave")
def apply_leave(
    leave: schemas.LeaveCreate,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.employee_required
    )
):

    # ======================================
    # CHECK EMPLOYEE
    # ======================================

    employee = db.query(
        models.Employee
    ).filter(
        models.Employee.emp_id == leave.emp_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    # ======================================
    # DATE VALIDATION
    # ======================================

    if leave.to_date < leave.from_date:

        raise HTTPException(
            status_code=400,
            detail="Invalid leave dates"
        )

    # ======================================
    # DUPLICATE LEAVE CHECK
    # ======================================

    existing_leave = db.query(
        models.Leave
    ).filter(
        models.Leave.emp_id == leave.emp_id,
        models.Leave.from_date == leave.from_date,
        models.Leave.to_date == leave.to_date
    ).first()

    if existing_leave:

        raise HTTPException(
            status_code=400,
            detail="Leave already applied"
        )

    # ======================================
    # SAVE LEAVE
    # ======================================

    new_leave = models.Leave(
        emp_id=leave.emp_id,
        from_date=leave.from_date,
        to_date=leave.to_date,
        reason=leave.reason,
        status="Pending"
    )

    db.add(new_leave)

    db.commit()

    db.refresh(new_leave)

    return {
        "message": "Leave Applied Successfully",
        "status": "Pending"
    }


# ==========================================
# VIEW ALL LEAVES
# ==========================================

@router.get("/leaves")
def get_all_leaves(
    db: Session = Depends(get_db)
):

    leaves = db.query(
        models.Leave
    ).all()

    return leaves


# ==========================================
# APPROVE LEAVE
# ==========================================

@router.put("/approve-leave/{leave_id}")
def approve_leave(
    leave_id: int,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    leave = db.query(
        models.Leave
    ).filter(
        models.Leave.id == leave_id
    ).first()

    if not leave:

        raise HTTPException(
            status_code=404,
            detail="Leave not found"
        )

    leave.status = "Approved"

    db.commit()

    return {
        "message": "Leave Approved"
    }


# ==========================================
# REJECT LEAVE
# ==========================================

@router.put("/reject-leave/{leave_id}")
def reject_leave(
    leave_id: int,
    db: Session = Depends(get_db)
):

    leave = db.query(
        models.Leave
    ).filter(
        models.Leave.id == leave_id
    ).first()

    if not leave:

        raise HTTPException(
            status_code=404,
            detail="Leave not found"
        )

    leave.status = "Rejected"

    db.commit()

    return {
        "message": "Leave Rejected"
    }
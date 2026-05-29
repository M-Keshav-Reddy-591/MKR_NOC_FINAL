from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import get_db

from models import (
    ShiftSwap,
    ShiftAssignment,
    Employee,
    Notification
)

router = APIRouter(
    prefix="/api/v1/swaps",
    tags=["Shift Swaps"]
)


# =========================================================
# REQUEST SHIFT SWAP
# =========================================================

@router.post("/request")
def request_swap(
    data: dict,
    db: Session = Depends(get_db)
):

    requester = db.query(
        Employee
    ).filter(
        Employee.emp_id == data["requester_id"]
    ).first()

    target = db.query(
        Employee
    ).filter(
        Employee.emp_id == data["target_employee_id"]
    ).first()

    if not requester or not target:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    requester_shift = db.query(
        ShiftAssignment
    ).filter(

        ShiftAssignment.employee_id == data["requester_id"],

        ShiftAssignment.shift_date == data["shift_date"]

    ).first()

    target_shift = db.query(
        ShiftAssignment
    ).filter(

        ShiftAssignment.employee_id == data["target_employee_id"],

        ShiftAssignment.shift_date == data["shift_date"]

    ).first()

    if not requester_shift:

        raise HTTPException(
            status_code=400,
            detail="Your shift not assigned"
        )

    if not target_shift:

        raise HTTPException(
            status_code=400,
            detail="Target employee has no shift"
        )

    existing = db.query(
        ShiftSwap
    ).filter(

        ShiftSwap.current_shift_id == requester_shift.id,

        ShiftSwap.requested_shift_id == target_shift.id,

        ShiftSwap.status == "Pending"

    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Swap already requested"
        )

    swap = ShiftSwap(

        requester_id=requester.id,

        target_employee_id=target.id,

        current_shift_id=requester_shift.id,

        requested_shift_id=target_shift.id,

        status="Pending"

    )

    db.add(swap)

    # =====================================================
    # ADMIN NOTIFICATION
    # =====================================================

    notification = Notification(

        employee_id="ADMIN",

        title="Shift Swap Request",

        message=f"{requester.emp_name} requested shift swap with {target.emp_name}",

        is_read=False

    )

    db.add(notification)

    db.commit()

    return {
        "message": "Shift swap request sent"
    }


# =========================================================
# GET ALL SWAPS
# =========================================================

@router.get("/")
def get_swaps(
    db: Session = Depends(get_db)
):

    swaps = db.query(
        ShiftSwap
    ).all()

    result = []

    for swap in swaps:

        requester = db.query(
            Employee
        ).filter(
            Employee.id == swap.requester_id
        ).first()

        target = db.query(
            Employee
        ).filter(
            Employee.id == swap.target_employee_id
        ).first()

        current_shift = db.query(
            ShiftAssignment
        ).filter(
            ShiftAssignment.id == swap.current_shift_id
        ).first()

        requested_shift = db.query(
            ShiftAssignment
        ).filter(
            ShiftAssignment.id == swap.requested_shift_id
        ).first()

        result.append({

            "swap_id": swap.id,

            "requester_name":
            requester.emp_name if requester else "",

            "requester_emp_id":
            requester.emp_id if requester else "",

            "target_name":
            target.emp_name if target else "",

            "target_emp_id":
            target.emp_id if target else "",

            "date":
            str(current_shift.shift_date)
            if current_shift else "",

            "requester_shift":
            current_shift.shift_name
            if current_shift else "",

            "target_shift":
            requested_shift.shift_name
            if requested_shift else "",

            "status":
            swap.status

        })

    return result


# =========================================================
# APPROVE SWAP
# =========================================================

@router.put("/approve/{swap_id}")
def approve_swap(
    swap_id: int,
    db: Session = Depends(get_db)
):

    swap = db.query(
        ShiftSwap
    ).filter(
        ShiftSwap.id == swap_id
    ).first()

    if not swap:

        raise HTTPException(
            status_code=404,
            detail="Swap not found"
        )

    current_shift = db.query(
        ShiftAssignment
    ).filter(
        ShiftAssignment.id == swap.current_shift_id
    ).first()

    requested_shift = db.query(
        ShiftAssignment
    ).filter(
        ShiftAssignment.id == swap.requested_shift_id
    ).first()

    if not current_shift or not requested_shift:

        raise HTTPException(
            status_code=404,
            detail="Shift not found"
        )

    temp_employee = current_shift.employee_id

    current_shift.employee_id = requested_shift.employee_id

    requested_shift.employee_id = temp_employee

    swap.status = "Approved"

    notification1 = Notification(

        employee_id=current_shift.employee_id,

        title="Shift Swap Approved",

        message="Your shift swap approved",

        is_read=False

    )

    notification2 = Notification(

        employee_id=requested_shift.employee_id,

        title="Shift Swap Approved",

        message="Your shift was swapped",

        is_read=False

    )

    db.add(notification1)
    db.add(notification2)

    db.commit()

    return {
        "message": "Shift swap approved"
    }


# =========================================================
# REJECT SWAP
# =========================================================

@router.put("/reject/{swap_id}")
def reject_swap(
    swap_id: int,
    db: Session = Depends(get_db)
):

    swap = db.query(
        ShiftSwap
    ).filter(
        ShiftSwap.id == swap_id
    ).first()

    if not swap:

        raise HTTPException(
            status_code=404,
            detail="Swap not found"
        )

    swap.status = "Rejected"

    db.commit()

    return {
        "message": "Shift swap rejected"
    }

# =====================================================
# MY SWAP REQUESTS
# =====================================================

@router.get("/my-requests/{emp_id}")
def my_requests(
    emp_id: str,
    db: Session = Depends(get_db)
):

    employee = db.query(
        Employee
    ).filter(
        Employee.emp_id == emp_id
    ).first()

    if not employee:

        return []

    swaps = db.query(
        ShiftSwap
    ).filter(
        ShiftSwap.requester_id == employee.id
    ).all()

    result = []

    for swap in swaps:

        target_emp = db.query(
            Employee
        ).filter(
            Employee.id ==
            swap.target_employee_id
        ).first()

        current_shift = db.query(
            ShiftAssignment
        ).filter(
            ShiftAssignment.id ==
            swap.current_shift_id
        ).first()

        requested_shift = db.query(
            ShiftAssignment
        ).filter(
            ShiftAssignment.id ==
            swap.requested_shift_id
        ).first()

        result.append({

            "target_employee": (
                target_emp.emp_name
                if target_emp else ""
            ),

            "date": str(
                current_shift.shift_date
            ) if current_shift else "",

            "your_shift": (
                current_shift.shift_name
                if current_shift else ""
            ),

            "target_shift": (
                requested_shift.shift_name
                if requested_shift else ""
            ),

            "status": swap.status
        })

    return result

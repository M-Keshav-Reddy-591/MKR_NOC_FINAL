from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import get_db

from models import (
    Employee,
    ShiftAssignment,
    ShiftSwap,
    Notification
)

router = APIRouter(
    prefix="/api/v1/swap",
    tags=["Shift Swap"]
)


# =====================================================
# REQUEST SHIFT SWAP
# =====================================================

@router.post("/request")
def request_swap(
    data: dict,
    db: Session = Depends(get_db)
):

    requester = db.query(
        Employee
    ).filter(
        Employee.emp_id ==
        data["requester_emp_id"]
    ).first()

    target = db.query(
        Employee
    ).filter(
        Employee.emp_id ==
        data["target_emp_id"]
    ).first()

    if not requester or not target:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    requester_shift = db.query(
        ShiftAssignment
    ).filter(

        ShiftAssignment.employee_id ==
        requester.emp_id,

        ShiftAssignment.shift_date ==
        data["shift_date"]

    ).first()

    target_shift = db.query(
        ShiftAssignment
    ).filter(

        ShiftAssignment.employee_id ==
        target.emp_id,

        ShiftAssignment.shift_date ==
        data["shift_date"]

    ).first()

    if not requester_shift:

        raise HTTPException(
            status_code=400,
            detail="Your shift not found"
        )


    if not target_shift:

        raise HTTPException(
            status_code=400,
            detail="Target employee shift not found"
        )

    # =====================================================
    # CHECK EXISTING SWAP REQUEST
    # =====================================================

    existing_swap = db.query(
        ShiftSwap
    ).filter(

        ShiftSwap.requester_id ==
        requester.id,

        ShiftSwap.target_employee_id ==
        target.id,

        ShiftSwap.current_shift_id ==
        requester_shift.id,

        ShiftSwap.requested_shift_id ==
        target_shift.id,

        ShiftSwap.status == "Pending"

    ).first()

    if existing_swap:

        raise HTTPException(
            status_code=400,
            detail=(
                "Shift swap request already sent "
                "and waiting for approval"
            )
        )



    swap = ShiftSwap(

        requester_id=requester.id,

        target_employee_id=target.id,

        current_shift_id=requester_shift.id,

        requested_shift_id=target_shift.id,

        status="Pending"
    )

    db.add(swap)

    notification = Notification(

        employee_id=target.emp_id,

        title="Shift Swap Request",

        message=(
            f"{requester.emp_name} "
            f"requested a shift swap"
        ),

        is_read=False
    )

    db.add(notification)

    db.commit()

    return {
        "message": "Shift swap request sent"
    }


# =====================================================
# MY REQUESTS
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
        ShiftSwap.requester_id ==
        employee.id
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


# =====================================================
# INCOMING REQUESTS
# =====================================================

@router.get("/incoming/{emp_id}")
def incoming_requests(
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
        ShiftSwap.target_employee_id ==
        employee.id
    ).all()

    result = []

    for swap in swaps:

        requester = db.query(
            Employee
        ).filter(
            Employee.id ==
            swap.requester_id
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

            "swap_id": swap.id,

            "requester_name": (
                requester.emp_name
                if requester else ""
            ),

            "date": str(
                current_shift.shift_date
            ) if current_shift else "",

            "their_shift": (
                current_shift.shift_name
                if current_shift else ""
            ),

            "your_shift": (
                requested_shift.shift_name
                if requested_shift else ""
            ),

            "status": swap.status
        })

    return result


# =====================================================
# APPROVE SWAP
# =====================================================

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
            detail="Swap request not found"
        )

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

    requester = db.query(
        Employee
    ).filter(
        Employee.id ==
        swap.requester_id
    ).first()

    target = db.query(
        Employee
    ).filter(
        Employee.id ==
        swap.target_employee_id
    ).first()

    # =====================================================
    # SWAP EMPLOYEES
    # =====================================================

    temp_employee = current_shift.employee_id

    current_shift.employee_id = (
        requested_shift.employee_id
    )

    requested_shift.employee_id = temp_employee

    swap.status = "Approved"

    # =====================================================
    # SEND NOTIFICATION TO REQUESTER
    # =====================================================

    notification = Notification(

        employee_id=requester.emp_id,

        title="Shift Swap Approved",

        message=(
            f"{target.emp_name} approved "
            f"your shift swap request"
        ),

        is_read=False
    )

    db.add(notification)

    db.commit()

    return {
        "message": "Shift swap approved"
    }




# =====================================================
# REJECT SWAP
# =====================================================


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
            detail="Swap request not found"
        )

    requester = db.query(
        Employee
    ).filter(
        Employee.id ==
        swap.requester_id
    ).first()

    target = db.query(
        Employee
    ).filter(
        Employee.id ==
        swap.target_employee_id
    ).first()

    swap.status = "Rejected"

    # =====================================================
    # SEND NOTIFICATION
    # =====================================================

    notification = Notification(

        employee_id=requester.emp_id,

        title="Shift Swap Rejected",

        message=(
            f"{target.emp_name} rejected "
            f"your shift swap request"
        ),

        is_read=False
    )

    db.add(notification)

    db.commit()

    return {
        "message": "Shift swap rejected"
    }


# =====================================================
# ADMIN - ALL SWAP REQUESTS
# =====================================================

@router.get("/all")
def all_swaps(
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
            Employee.id ==
            swap.requester_id
        ).first()

        target = db.query(
            Employee
        ).filter(
            Employee.id ==
            swap.target_employee_id
        ).first()

        requester_shift = db.query(
            ShiftAssignment
        ).filter(
            ShiftAssignment.id ==
            swap.current_shift_id
        ).first()

        target_shift = db.query(
            ShiftAssignment
        ).filter(
            ShiftAssignment.id ==
            swap.requested_shift_id
        ).first()

        result.append({

            "swap_id": swap.id,

            "requester": (
                requester.emp_name
                if requester else ""
            ),

            "target": (
                target.emp_name
                if target else ""
            ),

            "date": str(
                requester_shift.shift_date
            ) if requester_shift else "",

            "requester_shift": (
                requester_shift.shift_name
                if requester_shift else ""
            ),

            "target_shift": (
                target_shift.shift_name
                if target_shift else ""
            ),

            "status": swap.status
        })

    return result
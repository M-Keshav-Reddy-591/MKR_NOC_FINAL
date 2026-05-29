from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import get_db

from models import (
    Leave,
    Employee
)

router = APIRouter(
    prefix="/api/v1/leaves",
    tags=["Leaves"]
)


# =========================================================
# APPLY LEAVE
# =========================================================

# @router.post("/apply")
# def apply_leave(
#     data: dict,
#     db: Session = Depends(get_db)
# ):

#     employee = db.query(
#         Employee
#     ).filter(
#         Employee.emp_id == data["employee_id"]
#     ).first()

#     if not employee:

#         raise HTTPException(
#             status_code=404,
#             detail="Employee not found"
#         )

#     leave = Leave(

#         employee_id=data["employee_id"],

#         leave_date=data["leave_date"],

#         leave_type=data["leave_type"],

#         reason=data["reason"]

#     )

#     db.add(leave)

#     db.commit()

#     return {
#         "message": "Leave applied successfully"
#     }


# =========================================================
# ALL LEAVES
# =========================================================
@router.post("/apply")
def apply_leave(
    data: dict,
    db: Session = Depends(get_db)
):

    employee_id = str(
        data["employee_id"]
    ).strip()

    leave_date = data["leave_date"]

    shift_name = str(
        data["shift_name"]
    ).strip()

    # CHECK EMPLOYEE

    employee = db.query(
        Employee
    ).filter(
        Employee.emp_id == employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    # CHECK SHIFT EXISTS

    shift = db.query(
        ShiftAssignment
    ).filter(

        ShiftAssignment.employee_id == employee_id,

        ShiftAssignment.shift_date == leave_date,

        ShiftAssignment.shift_name == shift_name

    ).first()

    if not shift:

        raise HTTPException(
            status_code=404,
            detail="Shift not assigned"
        )

    # DUPLICATE CHECK

    existing_leave = db.query(
        Leave
    ).filter(

        Leave.employee_id == employee_id,

        Leave.leave_date == leave_date,

        Leave.shift_name == shift_name

    ).first()

    if existing_leave:

        raise HTTPException(
            status_code=400,
            detail="Leave already applied for this shift"
        )

    # SAVE LEAVE

    leave = Leave(

        employee_id=employee_id,

        leave_date=leave_date,

        shift_name=shift_name,

        leave_type=data["leave_type"],

        reason=data["reason"],

        status="Pending"

    )

    db.add(leave)

    db.commit()

    db.refresh(leave)

    return {
        "message": "Leave applied successfully"
    }
@router.get("/employee/{emp_id}")
def employee_leaves(
    emp_id: str,
    db: Session = Depends(get_db)
):

    leaves = db.query(
        Leave
    ).filter(
        Leave.employee_id == emp_id
    ).all()

    result = []

    for leave in leaves:

        result.append({

            "Date": str(
                leave.leave_date
            ),

            "Shift": leave.shift_name,

            "Type": leave.leave_type,

            "Reason": leave.reason,

            "Status": leave.status

        })

    return result
# @router.get("/")
# def all_leaves(
#     db: Session = Depends(get_db)
# ):

#     leaves = db.query(
#         Leave
#     ).all()

#     result = []

#     for leave in leaves:

#         employee = db.query(
#             Employee
#         ).filter(
#             Employee.emp_id == leave.employee_id
#         ).first()

#         result.append({
#             "id": leave.id,

#             "employee_id": leave.employee_id,

#             "employee_name": (
#                 employee.emp_name
#                 if employee else ""
#             ),

#             "leave_date": str(
#                 leave.leave_date
#             ),

#             "leave_type": leave.leave_type,

#             "reason": leave.reason,

#             "status": leave.status

#         })

#     return result


# =========================================================
# APPROVE LEAVE
# =========================================================

@router.put("/approve/{leave_id}")
def approve_leave(
    leave_id: int,
    db: Session = Depends(get_db)
):

    leave = db.query(
        Leave
    ).filter(
        Leave.id == leave_id
    ).first()

    if not leave:

        raise HTTPException(
            status_code=404,
            detail="Leave not found"
        )

    leave.status = "Approved"

    db.commit()

    return {
        "message": "Leave approved"
    }


# =========================================================
# REJECT LEAVE
# =========================================================

@router.put("/reject/{leave_id}")
def reject_leave(
    leave_id: int,
    db: Session = Depends(get_db)
):

    leave = db.query(
        Leave
    ).filter(
        Leave.id == leave_id
    ).first()

    if not leave:

        raise HTTPException(
            status_code=404,
            detail="Leave not found"
        )

    leave.status = "Rejected"

    db.commit()

    return {
        "message": "Leave rejected"
    }
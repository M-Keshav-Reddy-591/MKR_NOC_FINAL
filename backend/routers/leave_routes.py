from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import get_db

from models import (
    Leave,
    Employee,
    ShiftAssignment
)

router = APIRouter(
    prefix="/api/v1/leaves",
    tags=["Leaves"]
)


# =========================================================
# APPLY LEAVE
# =========================================================

@router.post("/apply")
def apply_leave(
    data: dict,
    db: Session = Depends(get_db)
):

    employee = db.query(
        Employee
    ).filter(
        Employee.emp_id == data["employee_id"]
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    # ============================================
    # CHECK SHIFT EXISTS
    # ============================================

    shift = db.query(
        ShiftAssignment
    ).filter(

        ShiftAssignment.employee_id == employee.emp_id,

        ShiftAssignment.shift_date == data["leave_date"],

        ShiftAssignment.shift_name == data["shift_name"]

    ).first()

    if not shift:

        raise HTTPException(
            status_code=400,
            detail="No shift assigned"
        )

    # ============================================
    # CHECK DUPLICATE LEAVE
    # ============================================

    existing_leave = db.query(
        Leave
    ).filter(

        Leave.employee_id == employee.emp_id,

        Leave.leave_date == data["leave_date"],

        Leave.shift_name == data["shift_name"]

    ).first()

    if existing_leave:

        raise HTTPException(
            status_code=400,
            detail="Leave already applied for this shift"
        )

    # ============================================
    # SAVE LEAVE
    # ============================================

    leave = Leave(

        employee_id=employee.emp_id,

        leave_date=data["leave_date"],

        shift_name=data["shift_name"],

        leave_type=data["leave_type"],

        reason=data["reason"],

        status="Pending"

    )

    db.add(leave)

    db.commit()

    return {
        "message": "Leave applied successfully"
    }


# =========================================================
# ALL LEAVES
# =========================================================

@router.get("/")
def all_leaves(
    db: Session = Depends(get_db)
):

    leaves = db.query(
        Leave
    ).all()

    result = []

    for leave in leaves:

        employee = db.query(
            Employee
        ).filter(
            Employee.emp_id == leave.employee_id
        ).first()

        result.append({

            "employee_id": leave.employee_id,

            "employee_name": (
                employee.emp_name
                if employee else ""
            ),

            "date": str(
                leave.leave_date
            ),

            "shift": leave.shift_name,

            "leave_type": leave.leave_type,

            "reason": leave.reason,

            "status": leave.status

        })

    return result


# =========================================================
# EMPLOYEE LEAVES
# =========================================================

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
# =========================================================
# UPDATE LEAVE STATUS
# =========================================================

@router.put("/update-status")
def update_leave_status(
    data: dict,
    db: Session = Depends(get_db)
):

    leave = db.query(
        Leave
    ).filter(

        Leave.employee_id == data["employee_id"],

        Leave.leave_date == data["leave_date"],

        Leave.shift_name == data["shift_name"]

    ).first()

    if not leave:

        raise HTTPException(
            status_code=404,
            detail="Leave request not found"
        )

    leave.status = data["status"]

    db.commit()

    return {
        "message": f"Leave {data['status']}"
    }
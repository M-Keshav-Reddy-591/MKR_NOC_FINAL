from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import get_db

from models import (
    ShiftAssignment,
    Notification,
    Employee
)


router = APIRouter(
    prefix="/api/v1/shifts",
    tags=["Shifts"]
)


# =========================================================
# CREATE SHIFT
# =========================================================

@router.post("/create")
def create_shift(
    data: dict,
    db: Session = Depends(get_db)
):

    # ============================================
    # CHECK EMPLOYEE
    # ============================================

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
    # CHECK DUPLICATE SHIFT
    # SAME SHIFT + SAME DATE
    # ============================================

    existing_shift = db.query(
        ShiftAssignment
    ).filter(

        ShiftAssignment.shift_name == data["shift_name"],

        ShiftAssignment.shift_date == data["shift_date"]

    ).first()

    if existing_shift:

        existing_employee = db.query(
            Employee
        ).filter(
            Employee.emp_id == existing_shift.employee_id
        ).first()

        raise HTTPException(

            status_code=400,

            detail=(
                f"{data['shift_name']} shift already assigned "
                f"to {existing_employee.emp_name}"
            )

        )

    # ============================================
    # CHECK EMPLOYEE ALREADY HAS SHIFT
    # ============================================

    employee_shift = db.query(
        ShiftAssignment
    ).filter(

        ShiftAssignment.employee_id == employee.emp_id,

        ShiftAssignment.shift_date == data["shift_date"]

    ).first()

    if employee_shift:

        raise HTTPException(

            status_code=400,

            detail=(
                "Employee already has a shift "
                "assigned for this date"
            )

        )

    # ============================================
    # CREATE SHIFT
    # ============================================

    shift = ShiftAssignment(

        employee_id=employee.emp_id,

        shift_name=data["shift_name"],

        shift_date=data["shift_date"],

        is_holiday=data.get(
            "is_holiday",
            False
        ),

        holiday_note=data.get(
            "holiday_note",
            ""
        )

    )

    db.add(shift)
    notification = Notification(

        employee_id=data["employee_id"],

        title="New Shift Assigned",

        message=f"You have been assigned {data['shift_name']} shift on {data['shift_date']}"

    )

    db.add(notification)


    db.commit()

    return {
        "message": "Shift assigned successfully"
    }

# @router.post("/create")
# def create_shift(
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

#     shift = ShiftAssignment(

#         employee_id=employee.emp_id,

#         shift_name=data["shift_name"],

#         start_time=data.get(
#             "start_time"
#         ),

#         end_time=data.get(
#             "end_time"
#         ),

#         shift_date=data["shift_date"],

#         is_holiday=data.get(
#             "is_holiday",
#             False
#         ),

#         holiday_note=data.get(
#             "holiday_note",
#             ""
#         )

#     )

#     db.add(shift)

#     db.commit()

#     return {
#         "message": "Shift assigned successfully"
#     }


# =========================================================
# ALL SHIFTS
# =========================================================

@router.get("/")
def all_shifts(
    db: Session = Depends(get_db)
):

    shifts = db.query(
        ShiftAssignment
    ).all()

    result = []

    for shift in shifts:

        employee = db.query(
            Employee
        ).filter(
            Employee.emp_id == shift.employee_id
        ).first()

        result.append({

            "employee_id": shift.employee_id,

            "employee_name": (
                employee.emp_name
                if employee else ""
            ),

            "shift_name": shift.shift_name,

            "shift_date": str(
                shift.shift_date
            ),

            "start_time": str(
                shift.start_time
            ),

            "end_time": str(
                shift.end_time
            ),

            "holiday": shift.is_holiday

        })

    return result


# =========================================================
# EMPLOYEE SHIFTS
# =========================================================

@router.get("/{emp_id}")
def employee_shifts(
    emp_id: str,
    db: Session = Depends(get_db)
):

    shifts = db.query(
        ShiftAssignment
    ).filter(
        ShiftAssignment.employee_id == emp_id
    ).all()

    result = []

    for shift in shifts:

        result.append({

            "shift_name": shift.shift_name,

            "shift_date": str(
                shift.shift_date
            ),

            "start_time": str(
                shift.start_time
            ),

            "end_time": str(
                shift.end_time
            ),

            "holiday": shift.is_holiday

        })

    return result


# =========================================================
# SHIFTS BY DATE
# =========================================================

@router.get("/{emp_id}/{shift_date}")
def shifts_by_date(
    emp_id: str,
    shift_date: str,
    db: Session = Depends(get_db)
):

    shifts = db.query(
        ShiftAssignment
    ).filter(

        ShiftAssignment.employee_id == emp_id,

        ShiftAssignment.shift_date == shift_date

    ).all()

    result = []

    for shift in shifts:

        result.append({

            "shift_name": shift.shift_name,

            "start_time": str(
                shift.start_time
            ),

            "end_time": str(
                shift.end_time
            )

        })

    return result
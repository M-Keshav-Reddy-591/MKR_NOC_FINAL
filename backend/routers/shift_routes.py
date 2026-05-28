from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import get_db

from models import (
    ShiftAssignment,
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

    shift = ShiftAssignment(

        employee_id=employee.id,

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

    db.commit()

    return {
        "message": "Shift assigned successfully"
    }


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
            Employee.id == shift.employee_id
        ).first()

        result.append({

            "employee_id": (
                employee.emp_id
                if employee else ""
            ),

            "employee_name": (
                employee.emp_name
                if employee else ""
            ),

            "shift": shift.shift_name,

            "date": str(
                shift.shift_date
            ),

            "holiday": shift.is_holiday

        })

    return result


# =========================================================
# EMPLOYEE SHIFTS
# =========================================================

# @router.get("/{emp_id}")
# def employee_shifts(
#     emp_id: str,
#     db: Session = Depends(get_db)
# ):

#     employee = db.query(
#         Employee
#     ).filter(
#         Employee.emp_id == emp_id
#     ).first()

#     if not employee:
#         return []

#     shifts = db.query(
#         ShiftAssignment
#     ).filter(
#         ShiftAssignment.employee_id == employee.id
#     ).all()

#     result = []

#     for shift in shifts:

#         result.append({

#             "shift": shift.shift_name,

#             "date": str(
#                 shift.shift_date
#             ),

#             "holiday": shift.is_holiday

#         })

#     return result
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
            )

        })

    return result


# =========================================================
# SHIFTS BY DATE
# =========================================================

# @router.get("/{emp_id}/{shift_date}")
# def shifts_by_date(
#     emp_id: str,
#     shift_date: str,
#     db: Session = Depends(get_db)
# ):

#     employee = db.query(
#         Employee
#     ).filter(
#         Employee.emp_id == emp_id
#     ).first()

#     if not employee:
#         return []

#     shifts = db.query(
#         ShiftAssignment
#     ).filter(

#         ShiftAssignment.employee_id == employee.id,

#         ShiftAssignment.shift_date == shift_date

#     ).all()

#     result = []

#     for shift in shifts:

#         result.append(
#             shift.shift_name
#         )

#     return result
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

        result.append(
            shift.shift_name
        )

    return result
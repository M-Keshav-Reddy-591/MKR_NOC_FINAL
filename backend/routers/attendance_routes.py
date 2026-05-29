from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import get_db

from models import (
    Attendance,
    Employee
)

router = APIRouter(
    prefix="/api/v1/attendance",
    tags=["Attendance"]
)


# =========================================================
# MANUAL ATTENDANCE
# =========================================================

# @router.post("/manual")
# def manual_attendance(
#     data: dict,
#     db: Session = Depends(get_db)
# ):

#     # ============================================
#     # CHECK EMPLOYEE
#     # ============================================

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

#     # ============================================
#     # CHECK DUPLICATE ATTENDANCE
#     # ============================================

#     existing = db.query(
#         Attendance
#     ).filter(

#         Attendance.employee_id == employee.emp_id,

#         Attendance.attendance_date == data["attendance_date"],

#         Attendance.shift_name == data["shift_name"]

#     ).first()

#     if existing:

#         raise HTTPException(
#             status_code=400,
#             detail="Attendance already marked for this shift"
#         )

#     # ============================================
#     # SAVE ATTENDANCE
#     # ============================================

#     attendance = Attendance(

#         employee_id=employee.emp_id,

#         attendance_date=data["attendance_date"],

#         status=data["status"],

#         shift_name=data["shift_name"]

#     )

#     db.add(attendance)

#     db.commit()

#     return {
#         "message": "Attendance marked successfully"
#     }
@router.post("/manual")
def manual_attendance(
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

    # =====================================================
    # CHECK EXISTING ATTENDANCE
    # =====================================================

    existing = db.query(
        Attendance
    ).filter(

        Attendance.employee_id == data["employee_id"],

        Attendance.attendance_date == data["attendance_date"],

        Attendance.shift_name == data["shift_name"]

    ).first()

    # =====================================================
    # UPDATE EXISTING
    # =====================================================

    if existing:

        existing.status = data["status"]

        db.commit()

        return {
            "message": "Attendance updated successfully"
        }

    # =====================================================
    # CREATE NEW
    # =====================================================

    attendance = Attendance(

        employee_id=data["employee_id"],

        attendance_date=data["attendance_date"],

        shift_name=data["shift_name"],

        status=data["status"]

    )

    db.add(attendance)

    db.commit()

    return {
        "message": "Attendance marked successfully"
    }


# =========================================================
# GET ALL ATTENDANCE
# =========================================================

@router.get("/")
def get_attendance(
    db: Session = Depends(get_db)
):

    records = db.query(
        Attendance
    ).all()

    result = []

    for row in records:

        employee = db.query(
            Employee
        ).filter(
            Employee.emp_id == row.employee_id
        ).first()

        result.append({

            "employee_id": row.employee_id,

            "employee_name": (
                employee.emp_name
                if employee else ""
            ),

            "date": str(
                row.attendance_date
            ),

            "shift": row.shift_name,

            "status": row.status

        })

    return result


# =========================================================
# EMPLOYEE ATTENDANCE
# =========================================================

@router.get("/employee/{emp_id}")
def employee_attendance(
    emp_id: str,
    db: Session = Depends(get_db)
):

    records = db.query(
        Attendance
    ).filter(
        Attendance.employee_id == emp_id
    ).all()

    result = []

    for row in records:

        result.append({

            "date": str(
                row.attendance_date
            ),

            "shift": row.shift_name,

            "status": row.status

        })

    return result
from datetime import date

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

    attendance = Attendance(

        employee_id=employee.emp_id,

        attendance_date=data["attendance_date"],

        status=data["status"],

        shift_name=data["shift_name"]

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

            "status": row.status

        })

    return result
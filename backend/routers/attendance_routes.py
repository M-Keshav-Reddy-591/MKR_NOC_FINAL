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
from datetime import (
    datetime,
    date
)
from models import ShiftAssignment
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
    existing = db.query(
        Attendance
    ).filter(

        Attendance.employee_id == employee.emp_id,

        Attendance.attendance_date == data["attendance_date"],

        Attendance.shift_name == data["shift_name"]

    ).first()

    if existing:

        raise HTTPException(

            status_code=400,

            detail="Attendance already marked"

        )

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

            "shift_name": row.shift_name,

            "status": row.status

        })

    return result
@router.post("/auto-absent")
def auto_absent(
    db: Session = Depends(get_db)
):

    today = date.today()

    shifts = db.query(
        ShiftAssignment
    ).filter(
        ShiftAssignment.shift_date == today
    ).all()

    current_time = datetime.now().time()

    count = 0

    for shift in shifts:

        if shift.end_time:

            if current_time > shift.end_time:

                existing = db.query(
                    Attendance
                ).filter(

                    Attendance.employee_id == shift.employee_id,

                    Attendance.attendance_date == today,

                    Attendance.shift_name == shift.shift_name

                ).first()

                if not existing:

                    absent = Attendance(

                        employee_id=shift.employee_id,

                        attendance_date=today,

                        shift_name=shift.shift_name,

                        status="Absent"

                    )

                    db.add(absent)

                    count += 1

    db.commit()

    return {

        "message": f"{count} employees marked absent"

    }
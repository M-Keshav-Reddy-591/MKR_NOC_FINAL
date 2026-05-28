from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database import get_db

from models import (
    Attendance,
    Employee
)

router = APIRouter(
    prefix="/api/v1/reports",
    tags=["Reports"]
)


# =========================================================
# ALL REPORTS
# =========================================================

@router.get("/all")
def get_all_reports(
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

            "shift_name": row.shift_name,

            "status": row.status



        })

    return result


# =========================================================
# EMPLOYEE REPORT
# =========================================================

@router.get("/employee/{emp_id}")
def employee_report(
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
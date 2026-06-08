# from fastapi import (
#     APIRouter,
#     Depends
# )

# from sqlalchemy.orm import Session

# from database import get_db

# from models import (
#     Attendance,
#     Employee
# )

# router = APIRouter(
#     prefix="/api/v1/reports",
#     tags=["Reports"]
# )


# # =========================================================
# # ALL REPORTS
# # =========================================================

# @router.get("/all")
# def get_all_reports(
#     db: Session = Depends(get_db)
# ):

#     records = db.query(
#         Attendance
#     ).all()

#     result = []

#     for row in records:

#         employee = db.query(
#             Employee
#         ).filter(
#             Employee.emp_id == row.employee_id
#         ).first()

#         result.append({

#             "employee_id": row.employee_id,

#             "employee_name": (
#                 employee.emp_name
#                 if employee else ""
#             ),

#             "date": str(
#                 row.attendance_date
#             ),

#             "shift_name": row.shift_name,

#             "status": row.status



#         })

#     return result


# # =========================================================
# # EMPLOYEE REPORT
# # =========================================================

# @router.get("/employee/{emp_id}")
# def employee_report(
#     emp_id: str,
#     db: Session = Depends(get_db)
# ):

#     records = db.query(
#         Attendance
#     ).filter(
#         Attendance.employee_id == emp_id
#     ).all()

#     result = []

#     for row in records:

#         result.append({

#             "date": str(
#                 row.attendance_date
#             ),

#             "shift_name": row.shift_name,

#             "status": row.status

#         })

#     return result
from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from sqlalchemy import extract

from database import get_db

from models import (
    Attendance,
    Employee
)

router = APIRouter(
    prefix="/api/v1/reports",
    tags=["Reports"]
)

from models import ShiftAssignment

@router.get("/available-periods")
def available_periods(
    db: Session = Depends(get_db)
):

    records = db.query(
        ShiftAssignment
    ).all()

    periods = {}

    for row in records:

        year = row.shift_date.year
        month = row.shift_date.month

        if str(year) not in periods:

            periods[str(year)] = []

        if month not in periods[str(year)]:

            periods[str(year)].append(month)

    for year in periods:

        periods[year].sort()

    return periods
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
            Employee.emp_id ==
            row.employee_id
        ).first()

        result.append({

            "employee_id":
            row.employee_id,

            "employee_name":
            employee.emp_name if employee else "",

            "date":
            str(row.attendance_date),

            "shift_name":
            row.shift_name,

            "status":
            row.status

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
        Attendance.employee_id ==
        emp_id
    ).all()

    result = []

    for row in records:

        result.append({

            "date":
            str(row.attendance_date),

            "shift_name":
            row.shift_name,

            "status":
            row.status

        })

    return result


# =========================================================
# MONTHLY SUMMARY
# =========================================================

@router.get("/monthly")
def monthly_summary(
    month: int,
    year: int,
    db: Session = Depends(get_db)
):

    employees = db.query(
        Employee
    ).all()

    result = []

    for emp in employees:

        records = db.query(
            Attendance
        ).filter(

            Attendance.employee_id ==
            emp.emp_id,

            extract(
                "month",
                Attendance.attendance_date
            ) == month,

            extract(
                "year",
                Attendance.attendance_date
            ) == year

        ).all()

        present = 0
        absent = 0
        leave = 0

        for row in records:

            status = (
                row.status.lower()
                if row.status else ""
            )

            if status == "present":
                present += 1

            elif status == "absent":
                absent += 1

            elif status == "leave":
                leave += 1

        total = (
            present +
            absent +
            leave
        )

        percentage = 0

        if total > 0:

            percentage = round(
                (present / total) * 100,
                2
            )

        result.append({

            "employee_id":
            emp.emp_id,

            "employee_name":
            emp.emp_name,

            "present":
            present,

            "absent":
            absent,

            "leave":
            leave,

            "attendance_percentage":
            percentage

        })

    return result


# =========================================================
# ABSENT REPORT
# =========================================================

@router.get("/absent")
def absent_report(
    month: int,
    year: int,
    db: Session = Depends(get_db)
):

    records = db.query(
        Attendance
    ).filter(

        Attendance.status == "Absent",

        extract(
            "month",
            Attendance.attendance_date
        ) == month,

        extract(
            "year",
            Attendance.attendance_date
        ) == year

    ).all()

    result = []

    for row in records:

        employee = db.query(
            Employee
        ).filter(
            Employee.emp_id ==
            row.employee_id
        ).first()

        result.append({

            "employee_id":
            row.employee_id,

            "employee_name":
            employee.emp_name if employee else "",

            "date":
            str(row.attendance_date),

            "shift_name":
            row.shift_name,

            "status":
            row.status

        })

    return result


# =========================================================
# TODAY ABSENT EMPLOYEES
# =========================================================

@router.get("/today-absent")
def today_absent(
    db: Session = Depends(get_db)
):

    records = db.query(
        Attendance
    ).filter(
        Attendance.status == "Absent"
    ).all()

    result = []

    for row in records:

        employee = db.query(
            Employee
        ).filter(
            Employee.emp_id ==
            row.employee_id
        ).first()

        result.append({

            "employee_id":
            row.employee_id,

            "employee_name":
            employee.emp_name if employee else "",

            "date":
            str(row.attendance_date),

            "shift_name":
            row.shift_name

        })

    return result
@router.get("/employee-detailed/{emp_id}")
def employee_detailed_report(
    emp_id: str,
    month: int,
    year: int,
    db: Session = Depends(get_db)
):

    records = db.query(
        Attendance
    ).filter(

        Attendance.employee_id == emp_id,

        extract(
            "month",
            Attendance.attendance_date
        ) == month,

        extract(
            "year",
            Attendance.attendance_date
        ) == year

    ).all()

    result = []

    for row in records:

        result.append({

            "date":
            str(row.attendance_date),

            "shift_name":
            row.shift_name,

            "status":
            row.status

        })

    return result
from sqlalchemy import extract

# =========================================================
# AVAILABLE REPORT PERIODS
# =========================================================

@router.get("/available-periods")
def available_periods(
    db: Session = Depends(get_db)
):

    records = db.query(
        Attendance
    ).all()

    periods = {}

    for row in records:

        year = row.attendance_date.year
        month = row.attendance_date.month

        if year not in periods:

            periods[year] = []

        if month not in periods[year]:

            periods[year].append(month)

    for year in periods:

        periods[year].sort()

    return periods
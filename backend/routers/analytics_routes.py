from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from datetime import date

import models
import auth

from database import SessionLocal


router = APIRouter()


# ==========================================
# DATABASE
# ==========================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ==========================================
# MONTHLY ATTENDANCE ANALYTICS
# ==========================================

@router.get("/monthly-attendance-analytics")
def monthly_attendance_analytics(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    employees = db.query(
        models.Employee
    ).all()

    analytics = []

    for employee in employees:

        total_records = db.query(
            models.Attendance
        ).filter(
            models.Attendance.emp_id == employee.emp_id
        ).count()

        present_count = db.query(
            models.Attendance
        ).filter(
            models.Attendance.emp_id == employee.emp_id,
            models.Attendance.status == "Present"
        ).count()

        late_count = db.query(
            models.Attendance
        ).filter(
            models.Attendance.emp_id == employee.emp_id,
            models.Attendance.status == "Late"
        ).count()

        half_day_count = db.query(
            models.Attendance
        ).filter(
            models.Attendance.emp_id == employee.emp_id,
            models.Attendance.status == "Half Day"
        ).count()

        absent_count = db.query(
            models.Attendance
        ).filter(
            models.Attendance.emp_id == employee.emp_id,
            models.Attendance.status == "Absent"
        ).count()

        attendance_percentage = 0

        if total_records > 0:

            attendance_percentage = round(
                (
                    (
                        present_count +
                        late_count +
                        half_day_count
                    ) / total_records
                ) * 100,
                2
            )

        analytics.append({

            "employee_id": employee.emp_id,

            "employee_name": employee.name,

            "department": employee.department,

            "total_records": total_records,

            "present_days": present_count,

            "late_days": late_count,

            "half_days": half_day_count,

            "absent_days": absent_count,

            "attendance_percentage": attendance_percentage
        })

    return analytics


# ==========================================
# DEPARTMENT ANALYTICS
# ==========================================

@router.get("/department-analytics")
def department_analytics(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    employees = db.query(
        models.Employee
    ).all()

    departments = {}

    for employee in employees:

        dept = employee.department

        if dept not in departments:

            departments[dept] = {

                "department": dept,

                "employee_count": 0,

                "present_count": 0,

                "late_count": 0,

                "absent_count": 0
            }

        departments[dept]["employee_count"] += 1

        present = db.query(
            models.Attendance
        ).filter(
            models.Attendance.emp_id == employee.emp_id,
            models.Attendance.status == "Present"
        ).count()

        late = db.query(
            models.Attendance
        ).filter(
            models.Attendance.emp_id == employee.emp_id,
            models.Attendance.status == "Late"
        ).count()

        absent = db.query(
            models.Attendance
        ).filter(
            models.Attendance.emp_id == employee.emp_id,
            models.Attendance.status == "Absent"
        ).count()

        departments[dept]["present_count"] += present

        departments[dept]["late_count"] += late

        departments[dept]["absent_count"] += absent

    return list(departments.values())


# ==========================================
# LEAVE ANALYTICS
# ==========================================

@router.get("/leave-analytics")
def leave_analytics(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    approved = db.query(
        models.Leave
    ).filter(
        models.Leave.status == "Approved"
    ).count()

    rejected = db.query(
        models.Leave
    ).filter(
        models.Leave.status == "Rejected"
    ).count()

    pending = db.query(
        models.Leave
    ).filter(
        models.Leave.status == "Pending"
    ).count()

    total = db.query(
        models.Leave
    ).count()

    return {

        "total_leave_requests": total,

        "approved_leaves": approved,

        "rejected_leaves": rejected,

        "pending_leaves": pending
    }


# ==========================================
# SHIFT ANALYTICS
# ==========================================

@router.get("/shift-analytics")
def shift_analytics(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    shifts = db.query(
        models.Shift
    ).all()

    data = []

    for shift in shifts:

        assigned_count = db.query(
            models.Roster
        ).filter(
            models.Roster.shift_id == shift.id
        ).count()

        data.append({

            "shift_name": shift.shift_name,

            "start_time": shift.start_time,

            "end_time": shift.end_time,

            "assigned_employees": assigned_count
        })

    return data


# ==========================================
# EMPLOYEE PERFORMANCE
# ==========================================

@router.get("/employee-performance")
def employee_performance(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    employees = db.query(
        models.Employee
    ).all()

    performance = []

    for employee in employees:

        present = db.query(
            models.Attendance
        ).filter(
            models.Attendance.emp_id == employee.emp_id,
            models.Attendance.status == "Present"
        ).count()

        late = db.query(
            models.Attendance
        ).filter(
            models.Attendance.emp_id == employee.emp_id,
            models.Attendance.status == "Late"
        ).count()

        absent = db.query(
            models.Attendance
        ).filter(
            models.Attendance.emp_id == employee.emp_id,
            models.Attendance.status == "Absent"
        ).count()

        score = (present * 2) - (late) - (absent * 2)

        performance.append({

            "employee_id": employee.emp_id,

            "employee_name": employee.name,

            "performance_score": score,

            "present_days": present,

            "late_days": late,

            "absent_days": absent
        })

    performance.sort(
        key=lambda x: x["performance_score"],
        reverse=True
    )

    return performance
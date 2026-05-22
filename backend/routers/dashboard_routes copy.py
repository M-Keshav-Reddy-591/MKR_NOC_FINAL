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
# ADMIN DASHBOARD
# ==========================================

@router.get("/admin-dashboard")
def admin_dashboard(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    today = date.today()

    # ======================================
    # TOTAL EMPLOYEES
    # ======================================

    total_employees = db.query(
        models.Employee
    ).count()

    # ======================================
    # PRESENT
    # ======================================

    present_count = db.query(
        models.Attendance
    ).filter(
        models.Attendance.shift_date == today,
        models.Attendance.status == "Present"
    ).count()

    # ======================================
    # LATE
    # ======================================

    late_count = db.query(
        models.Attendance
    ).filter(
        models.Attendance.shift_date == today,
        models.Attendance.status == "Late"
    ).count()

    # ======================================
    # HALF DAY
    # ======================================

    half_day_count = db.query(
        models.Attendance
    ).filter(
        models.Attendance.shift_date == today,
        models.Attendance.status == "Half Day"
    ).count()

    # ======================================
    # APPROVED LEAVES
    # ======================================

    leave_count = db.query(
        models.Leave
    ).filter(
        models.Leave.status == "Approved"
    ).count()

    # ======================================
    # TOTAL ATTENDANCE
    # ======================================

    total_attendance = db.query(
        models.Attendance
    ).filter(
        models.Attendance.shift_date == today
    ).count()

    # ======================================
    # ABSENT
    # ======================================

    absent_count = total_employees - total_attendance

    return {

        "date": today,

        "total_employees": total_employees,

        "present_today": present_count,

        "late_today": late_count,

        "half_day_today": half_day_count,

        "absent_today": absent_count,

        "employees_on_leave": leave_count
    }


# ==========================================
# EMPLOYEE DASHBOARD
# ==========================================

@router.get("/employee-dashboard")
def employee_dashboard(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.employee_required
    )
):

    employee_id = current_user.emp_id

    total_attendance = db.query(
        models.Attendance
    ).filter(
        models.Attendance.emp_id == employee_id
    ).count()

    present_count = db.query(
        models.Attendance
    ).filter(
        models.Attendance.emp_id == employee_id,
        models.Attendance.status == "Present"
    ).count()

    late_count = db.query(
        models.Attendance
    ).filter(
        models.Attendance.emp_id == employee_id,
        models.Attendance.status == "Late"
    ).count()

    half_day_count = db.query(
        models.Attendance
    ).filter(
        models.Attendance.emp_id == employee_id,
        models.Attendance.status == "Half Day"
    ).count()

    leave_count = db.query(
        models.Leave
    ).filter(
        models.Leave.emp_id == employee_id,
        models.Leave.status == "Approved"
    ).count()

    return {

        "employee_id": employee_id,

        "total_attendance": total_attendance,

        "present_days": present_count,

        "late_days": late_count,

        "half_days": half_day_count,

        "approved_leaves": leave_count
    }


# ==========================================
# ATTENDANCE REPORT
# ==========================================

@router.get("/attendance-report")
def attendance_report(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    attendance = db.query(
        models.Attendance
    ).all()

    report = []

    for item in attendance:

        report.append({

            "employee_id": item.emp_id,

            "date": item.shift_date,

            "login_time": item.login_time,

            "status": item.status
        })

    return report


# ==========================================
# LEAVE REPORT
# ==========================================

@router.get("/leave-report")
def leave_report(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    leaves = db.query(
        models.Leave
    ).all()

    report = []

    for item in leaves:

        report.append({

            "employee_id": item.emp_id,

            "from_date": item.from_date,

            "to_date": item.to_date,

            "reason": item.reason,

            "status": item.status
        })

    return report


# ==========================================
# SHIFT REPORT
# ==========================================

@router.get("/shift-report")
def shift_report(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    roster = db.query(
        models.Roster
    ).all()

    report = []

    for item in roster:

        shift = db.query(
            models.Shift
        ).filter(
            models.Shift.id == item.shift_id
        ).first()

        report.append({

            "employee_id": item.emp_id,

            "shift_name": shift.shift_name,

            "shift_date": item.shift_date
        })

    return report
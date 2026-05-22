from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import SessionLocal

import models
import auth


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
# DASHBOARD STATS
# ==========================================

@router.get("/stats")
def get_dashboard_stats(

    db: Session = Depends(get_db),

    current_user: models.Employee = Depends(
        auth.get_current_user
    )
):

    total_employees = db.query(
        models.Employee
    ).count()


    total_attendance = db.query(
        models.Attendance
    ).count()


    total_leaves = db.query(
        models.Leave
    ).count()


    total_swaps = db.query(
        models.ShiftSwap
    ).count()


    return {

        "employees": total_employees,

        "attendance": total_attendance,

        "leaves": total_leaves,

        "swaps": total_swaps
    }
# ==========================================
# EMPLOYEE DASHBOARD
# ==========================================

@router.get("/employee-dashboard")
def employee_dashboard(

    db: Session = Depends(get_db),

    current_user: models.Employee = Depends(
        auth.get_current_user
    )
):

    attendance_count = db.query(
        models.Attendance
    ).filter(
        models.Attendance.employee_id
        == current_user.id
    ).count()


    return {

        "employee": current_user.name,

        "attendance_count": attendance_count
    }


# ==========================================
# ATTENDANCE REPORT
# ==========================================

@router.get("/attendance-report")
def attendance_report(

    db: Session = Depends(get_db),

    current_user: models.Employee = Depends(
        auth.get_current_user
    )
):

    attendance = db.query(
        models.Attendance
    ).all()


    report = []


    for item in attendance:

        report.append({

            "employee_id": item.employee_id,

            "date": item.date,

            "status": item.status
        })


    return report
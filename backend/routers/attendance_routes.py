from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from datetime import datetime
from datetime import date

from database import get_db

import models
import schemas

from auth import get_current_user


router = APIRouter(
    prefix="/api/v1/attendance",
    tags=["Attendance"]
)


# =====================================================
# EMPLOYEE CHECK-IN
# =====================================================

@router.post("/check-in")
def employee_check_in(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    today = date.today()

    existing_attendance = db.query(models.Attendance).filter(
        models.Attendance.employee_id == current_user.id,
        models.Attendance.attendance_date == today
    ).first()

    if existing_attendance:
        raise HTTPException(
            status_code=400,
            detail="Attendance already marked today"
        )

    attendance = models.Attendance(
        employee_id=current_user.id,
        attendance_date=today,
        status="Present",
        check_in=datetime.now()
    )

    db.add(attendance)

    db.commit()

    db.refresh(attendance)

    return {
        "message": "Check-in successful",
        "check_in": attendance.check_in
    }


# =====================================================
# EMPLOYEE CHECK-OUT
# =====================================================

@router.put("/check-out")
def employee_check_out(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    today = date.today()

    attendance = db.query(models.Attendance).filter(
        models.Attendance.employee_id == current_user.id,
        models.Attendance.attendance_date == today
    ).first()

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="No check-in found"
        )

    attendance.check_out = datetime.now()

    db.commit()

    return {
        "message": "Check-out successful",
        "check_out": attendance.check_out
    }


# =====================================================
# EMPLOYEE ATTENDANCE HISTORY
# =====================================================

@router.get("/my-attendance")
def my_attendance(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    attendance_records = db.query(models.Attendance).filter(
        models.Attendance.employee_id == current_user.id
    ).all()

    result = []

    for attendance in attendance_records:

        result.append({
            "id": attendance.id,
            "date": attendance.attendance_date,
            "status": attendance.status,
            "check_in": attendance.check_in,
            "check_out": attendance.check_out,
            "remarks": attendance.remarks
        })

    return result


# =====================================================
# ADMIN MARK ATTENDANCE
# =====================================================

@router.post("/admin-mark-attendance")
def admin_mark_attendance(
     attendance_data: schemas.AttendanceSchema,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    employee = db.query(models.Employee).filter(
        models.Employee.id == attendance_data.employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    today = date.today()

    existing_attendance = db.query(models.Attendance).filter(
        models.Attendance.employee_id == employee.id,
        models.Attendance.attendance_date == today
    ).first()

    if existing_attendance:
        raise HTTPException(
            status_code=400,
            detail="Attendance already exists"
        )

    attendance = models.Attendance(
        employee_id=employee.id,
        attendance_date=today,
        status=attendance_data.status,
        check_in=datetime.now()
        if attendance_data.check_in else None,
        check_out=datetime.now()
        if attendance_data.check_out else None,
        remarks=attendance_data.remarks
    )

    db.add(attendance)

    db.commit()

    db.refresh(attendance)

    return {
        "message": "Attendance marked successfully"
    }


# =====================================================
# ADMIN ALL ATTENDANCE
# =====================================================

@router.get("/all-attendance")
def get_all_attendance(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    records = db.query(models.Attendance).all()

    result = []

    for attendance in records:

        employee = db.query(models.Employee).filter(
            models.Employee.id == attendance.employee_id
        ).first()

        result.append({
            "attendance_id": attendance.id,
            "employee_name": employee.name,
            "emp_id": employee.emp_id,
            "department": employee.department,
            "date": attendance.attendance_date,
            "status": attendance.status,
            "check_in": attendance.check_in,
            "check_out": attendance.check_out,
            "remarks": attendance.remarks
        })

    return result
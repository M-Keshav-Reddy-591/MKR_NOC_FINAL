from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, date

import models

from database import SessionLocal
from dependencies import get_current_user

from sqlalchemy.orm import Session

from database import get_db

import auth
import schemas

from dependencies import get_current_user
router = APIRouter()


# =====================================================
# ADMIN MARK ATTENDANCE
# =====================================================

@router.post("/admin-mark-attendance")
def admin_mark_attendance(

    data: dict,

    db: Session = Depends(get_db),

    current_user: models.Employee = Depends(
        auth.get_current_user
    )
):

    if current_user.role != "admin":

        raise HTTPException(

            status_code=403,

            detail="Admin Only"
        )

    employee = db.query(

        models.Employee

    ).filter(

        models.Employee.emp_id
        == data["emp_id"]

    ).first()


    if not employee:

        raise HTTPException(

            status_code=404,

            detail="Employee Not Found"
        )


    attendance_date = date.today()


    existing = db.query(

        models.Attendance

    ).filter(

        models.Attendance.employee_id
        == employee.id,

        models.Attendance.date
        == attendance_date

    ).first()


    if existing:

        existing.status = data["status"]

        existing.login_time = data.get(
            "login_time"
        )

        existing.logout_time = data.get(
            "logout_time"
        )

        existing.ot_hours = data.get(
            "ot_hours",
            0
        )

        existing.remarks = data.get(
            "remarks"
        )

        db.commit()

        return {

            "message":
            "Attendance Updated Successfully"
        }


    attendance = models.Attendance(

        employee_id=employee.id,

        date=attendance_date,

        status=data["status"],

        login_time=data.get(
            "login_time"
        ),

        logout_time=data.get(
            "logout_time"
        ),

        ot_hours=data.get(
            "ot_hours",
            0
        ),

        remarks=data.get(
            "remarks"
        )
    )

    db.add(attendance)

    db.commit()


    return {

        "message":
        "Attendance Marked Successfully"
    }


# =====================================================
# GET TODAY ATTENDANCE
# =====================================================

@router.get("/today-attendance")
def today_attendance(

    db: Session = Depends(get_db),

    current_user: models.Employee = Depends(
        auth.get_current_user
    )
):

    records = db.query(

        models.Attendance

    ).all()


    output = []


    for record in records:

        output.append({

            "employee_name":
            record.employee.full_name,

            "emp_id":
            record.employee.emp_id,

            "status":
            record.status,

            "login_time":
            str(record.login_time),

            "logout_time":
            str(record.logout_time),

            "ot_hours":
            record.ot_hours,

            "remarks":
            record.remarks
        })


    return output
@router.post("/mark-attendance")
def mark_attendance(
    request: schemas.MarkAttendance,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    attendance = models.Attendance(

        employee_id=current_user.id,

        status=request.status,

        check_in=datetime.now(),

        late_minutes=request.late_minutes,

        ot_hours=request.ot_hours
    )

    db.add(attendance)

    db.commit()

    return {
        "message": "Attendance marked successfully"
    }

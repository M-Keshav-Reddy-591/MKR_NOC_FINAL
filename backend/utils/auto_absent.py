from datetime import datetime

from database import SessionLocal

from models import (
    ShiftAssignment,
    Attendance
)


def mark_absent_employees():
    print("AUTO ABSENT CHECK RUNNING...")

    db = SessionLocal()

    try:

        today = datetime.now().date()
        current_time = datetime.now().time()

        shifts = db.query(
            ShiftAssignment
        ).filter(
            ShiftAssignment.shift_date <= today
        ).all()

        for shift in shifts:

            if shift.is_holiday:
                continue

            if shift.end_time is None:
                continue

            # Shift not yet finished
            if current_time < shift.end_time:
                continue

            attendance = db.query(
                Attendance
            ).filter(

                Attendance.employee_id ==
                shift.employee_id,

                Attendance.attendance_date ==   
            shift.shift_date

            ).first()

            if attendance:
                continue

            absent = Attendance(

                employee_id=shift.employee_id,

                attendance_date=today,

                shift_name=shift.shift_name,

                status="Absent"

            )

            db.add(absent)

        db.commit()

    finally:

        db.close()
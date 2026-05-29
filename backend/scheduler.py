from apscheduler.schedulers.background import BackgroundScheduler

from datetime import date, timedelta

from database import SessionLocal

from models import (
    ShiftAssignment,
    Employee
)

from utils.email_service import send_email


def shift_email_job():

    db = SessionLocal()

    target_date = date.today() + timedelta(days=2)

    shifts = db.query(
        ShiftAssignment
    ).filter(
        ShiftAssignment.shift_date == target_date
    ).all()

    for shift in shifts:

        employee = db.query(
            Employee
        ).filter(
            Employee.emp_id == shift.employee_id
        ).first()

        if employee and employee.email:

            send_email(

                employee.email,

                "Upcoming Shift Reminder",

                f"""

Hello {employee.emp_name},

You have upcoming shift.

Shift: {shift.shift_name}

Date: {shift.shift_date}

Time:
{shift.start_time} to {shift.end_time}

"""

            )

    db.close()


scheduler = BackgroundScheduler()

scheduler.add_job(
    shift_email_job,
    "interval",
    hours=24
)

scheduler.start()

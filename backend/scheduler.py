from apscheduler.schedulers.background import BackgroundScheduler

from datetime import (
    date,
    timedelta
)

from database import SessionLocal

from models import (
    ShiftAssignment,
    Employee
)

from utils.email_service import send_email

from utils.auto_absent import (
    mark_absent_employees
)


def shift_email_job():

    print("SHIFT EMAIL JOB RUNNING...")

    db = SessionLocal()

    try:

        target_date = (
            date.today() +
            timedelta(days=2)
        )

        shifts = db.query(
            ShiftAssignment
        ).filter(
            ShiftAssignment.shift_date ==
            target_date
        ).all()

        for shift in shifts:

            employee = db.query(
                Employee
            ).filter(
                Employee.emp_id ==
                shift.employee_id
            ).first()

            if employee and employee.email:

                send_email(

                    employee.email,

                    "Upcoming Shift Reminder",

                    f"""
Hello {employee.emp_name},

You have an upcoming shift.

Shift :
{shift.shift_name}

Date :
{shift.shift_date}

Time :
{shift.start_time} to {shift.end_time}
"""
                )

    finally:

        db.close()


scheduler = BackgroundScheduler()

# Auto absent every 5 mins
scheduler.add_job(

    mark_absent_employees,

    trigger="interval",

    minutes=5,#hours=7,

    id="auto_absent_job"
)

# Run immediately at startup
# print("Running auto absent startup check...")
# mark_absent_employees()

scheduler.start()

print("Scheduler Started")
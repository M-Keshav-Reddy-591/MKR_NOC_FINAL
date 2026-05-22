from datetime import datetime
from datetime import date

from sqlalchemy.orm import Session

import models


# ==========================================
# AUTO ABSENT LOGIC
# ==========================================

def mark_absent_employees(db: Session):

    today = date.today()

    roster_entries = db.query(
        models.Roster
    ).filter(
        models.Roster.shift_date == today
    ).all()

    absent_marked = 0

    for roster in roster_entries:

        emp_id = roster.emp_id

        # ======================================
        # CHECK APPROVED LEAVE
        # ======================================

        approved_leave = db.query(
            models.Leave
        ).filter(
            models.Leave.emp_id == emp_id,
            models.Leave.status == "Approved",
            models.Leave.from_date <= today,
            models.Leave.to_date >= today
        ).first()

        if approved_leave:

            continue

        # ======================================
        # CHECK ATTENDANCE
        # ======================================

        attendance = db.query(
            models.Attendance
        ).filter(
            models.Attendance.emp_id == emp_id,
            models.Attendance.shift_date == today
        ).first()

        if attendance:

            continue

        # ======================================
        # GET SHIFT
        # ======================================

        shift = db.query(
            models.Shift
        ).filter(
            models.Shift.id == roster.shift_id
        ).first()

        if not shift:

            continue

        # ======================================
        # SHIFT END TIME VALIDATION
        # ======================================

        current_time = datetime.now().time()

        if current_time < shift.end_time:

            continue

        # ======================================
        # MARK ABSENT
        # ======================================

        absent_entry = models.Attendance(

            emp_id=emp_id,

            shift_date=today,

            login_time=datetime.now(),

            status="Absent"
        )

        db.add(absent_entry)

        absent_marked += 1

    db.commit()

    return {

        "message": "Auto absent process completed",

        "absent_marked": absent_marked
    }
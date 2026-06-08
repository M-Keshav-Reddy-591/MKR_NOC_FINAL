from datetime import (
    datetime,
    timedelta
)

from database import SessionLocal

from models import (
    ShiftAssignment,
    Attendance,
    Leave
)


def mark_absent_employees():

    print("AUTO ABSENT CHECK RUNNING...")

    db = SessionLocal()

    try:

        current_datetime = datetime.now()

        shifts = db.query(
            ShiftAssignment
        ).all()

        for shift in shifts:

            # -----------------------------------
            # HOLIDAY
            # -----------------------------------

            if shift.is_holiday:
                continue

            # -----------------------------------
            # INVALID SHIFT
            # -----------------------------------

            if (
                shift.start_time is None
                or
                shift.end_time is None
            ):
                continue

            # -----------------------------------
            # SHIFT END DATETIME
            # -----------------------------------

            shift_date = shift.shift_date

            # Night Shift
            if shift.start_time > shift.end_time:

                shift_end_datetime = datetime.combine(
                    shift_date + timedelta(days=1),
                    shift.end_time
                )

            else:

                shift_end_datetime = datetime.combine(
                    shift_date,
                    shift.end_time
                )

            # -----------------------------------
            # SHIFT NOT COMPLETED
            # -----------------------------------

            if current_datetime < shift_end_datetime:
                continue

            # -----------------------------------
            # APPROVED LEAVE EXISTS
            # -----------------------------------

            leave = db.query(
                Leave
            ).filter(

                Leave.employee_id ==
                shift.employee_id,

                Leave.leave_date ==
                shift.shift_date,

                Leave.status ==
                "Approved"

            ).first()

            if leave:
                continue

            # -----------------------------------
            # ATTENDANCE ALREADY EXISTS
            # -----------------------------------

            attendance = db.query(
                Attendance
            ).filter(

                Attendance.employee_id ==
                shift.employee_id,

                Attendance.attendance_date ==
                shift.shift_date,

                Attendance.shift_name ==
                shift.shift_name

            ).first()

            if attendance:
                continue

            # -----------------------------------
            # CREATE ABSENT
            # -----------------------------------

            absent = Attendance(

                employee_id=shift.employee_id,

                attendance_date=shift.shift_date,

                shift_name=shift.shift_name,

                status="Absent"

            )

            db.add(absent)

            print(
                f"ABSENT MARKED -> "
                f"{shift.employee_id} | "
                f"{shift.shift_date} | "
                f"{shift.shift_name}"
            )

        db.commit()

    except Exception as e:

        print(
            f"AUTO ABSENT ERROR : {e}"
        )

        db.rollback()

    finally:

        db.close()
from datetime import datetime
from datetime import timedelta


# ==========================================
# CHECK ATTENDANCE STATUS
# ==========================================

def calculate_attendance_status(
    shift_start,
    grace_minutes,
    login_time
):

    shift_datetime = datetime.combine(
        login_time.date(),
        shift_start
    )

    present_limit = shift_datetime + timedelta(
        minutes=grace_minutes
    )

    late_limit = shift_datetime + timedelta(
        minutes=30
    )

    if login_time <= present_limit:

        return "Present"

    elif login_time <= late_limit:

        return "Late"

    else:

        return "Half Day"
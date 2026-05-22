from datetime import datetime, timedelta

def check_attendance_status(
    shift_start,
    login_time,
    grace_minutes
):

    shift_datetime = datetime.combine(
        login_time.date(),
        shift_start
    )

    grace_time = shift_datetime + timedelta(
        minutes=grace_minutes
    )

    half_day_time = shift_datetime + timedelta(
        minutes=30
    )

    if login_time <= grace_time:
        return "Present"

    elif login_time <= half_day_time:
        return "Late"

    else:
        return "Half Day"
from datetime import (
    date,
    datetime
)

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import get_db

from models import (
    Attendance,
    Employee,
    ShiftAssignment
)

router = APIRouter(
    prefix="/api/v1/attendance",
    tags=["Attendance"]
)


# =========================================================
# MANUAL ATTENDANCE BY ADMIN
# =========================================================

@router.post("/manual")
def manual_attendance(
    data: dict,
    db: Session = Depends(get_db)
):

    employee = db.query(
        Employee
    ).filter(
        Employee.emp_id == data["employee_id"]
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    existing = db.query(
        Attendance
    ).filter(

        Attendance.employee_id == data["employee_id"],

        Attendance.attendance_date == data["attendance_date"],

        Attendance.shift_name == data["shift_name"]

    ).first()

    # =====================================================
    # ADMIN CAN UPDATE EXISTING
    # =====================================================

    if existing:

        existing.status = data["status"]

        db.commit()

        return {
            "message": "Attendance updated successfully"
        }

    attendance = Attendance(

        employee_id=data["employee_id"],

        attendance_date=data["attendance_date"],

        status=data["status"],

        shift_name=data["shift_name"]

    )

    db.add(attendance)

    db.commit()

    return {
        "message": "Attendance marked successfully"
    }


# =========================================================
# EMPLOYEE MARK PRESENT
# =========================================================


@router.post("/mark")
def mark_attendance(
    data: dict,
    db: Session = Depends(get_db)
):

    employee_id = data["employee_id"]

    attendance_date = data["attendance_date"]

    shift_name = data["shift_name"]

    # ============================================
    # CHECK SHIFT
    # ============================================

    shift = db.query(
        ShiftAssignment
    ).filter(

        ShiftAssignment.employee_id == employee_id,

        ShiftAssignment.shift_date == attendance_date,

        ShiftAssignment.shift_name == shift_name

    ).first()

    if not shift:

        raise HTTPException(
            status_code=404,
            detail="Shift not assigned"
        )

    # ============================================
    # CHECK SHIFT TIME EXISTS
    # ============================================

    if not shift.start_time or not shift.end_time:

        raise HTTPException(
            status_code=400,
            detail="Shift timing missing"
        )

    current_time = datetime.now().time()

    start_time = shift.start_time

    end_time = shift.end_time

    # ============================================
    # NORMAL SHIFT
    # ============================================

    if start_time < end_time:

        if current_time < start_time:

            raise HTTPException(
                status_code=400,
                detail=f"Shift starts at {start_time}"
            )

        if current_time > end_time:

            raise HTTPException(
                status_code=400,
                detail=f"Shift ended at {end_time}"
            )

    # ============================================
    # NIGHT SHIFT
    # ============================================

    else:

        allowed = (

            current_time >= start_time

            or

            current_time <= end_time

        )

        if not allowed:

            raise HTTPException(
                status_code=400,
                detail="Outside shift timing"
            )

    # ============================================
    # CHECK DUPLICATE ATTENDANCE
    # ============================================

    existing = db.query(
        Attendance
    ).filter(

        Attendance.employee_id == employee_id,

        Attendance.attendance_date == attendance_date,

        Attendance.shift_name == shift_name

    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Attendance already marked"
        )

    # ============================================
    # SAVE ATTENDANCE
    # ============================================

    attendance = Attendance(

        employee_id=employee_id,

        attendance_date=attendance_date,

        shift_name=shift_name,

        status="Present"

    )

    db.add(attendance)

    db.commit()

    return {
        "message": "Attendance marked successfully"
    }


# =========================================================
# GET ALL ATTENDANCE
# =========================================================

@router.get("/")
def get_attendance(
    db: Session = Depends(get_db)
):

    records = db.query(
        Attendance
    ).all()

    result = []

    for row in records:

        employee = db.query(
            Employee
        ).filter(
            Employee.emp_id == row.employee_id
        ).first()

        result.append({

            "employee_id": row.employee_id,

            "employee_name": (
                employee.emp_name
                if employee else ""
            ),

            "date": str(
                row.attendance_date
            ),

            "shift_name": row.shift_name,

            "status": row.status

        })

    return result


# =========================================================
# EMPLOYEE ATTENDANCE
# =========================================================

@router.get("/employee/{emp_id}")
def employee_attendance(
    emp_id: str,
    db: Session = Depends(get_db)
):

    records = db.query(
        Attendance
    ).filter(
        Attendance.employee_id == emp_id
    ).all()

    result = []

    for row in records:

        result.append({

            "date": str(
                row.attendance_date
            ),

            "shift_name": row.shift_name,

            "status": row.status

        })

    return result
@router.get("/employee-summary/{emp_id}")
def employee_summary(
    emp_id: str,
    db: Session = Depends(get_db)
):

    employee = db.query(
        Employee
    ).filter(
        Employee.emp_id == emp_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    shifts = db.query(
        ShiftAssignment
    ).filter(
        ShiftAssignment.employee_id == emp_id
    ).all()

    attendance = db.query(
        Attendance
    ).filter(
        Attendance.employee_id == emp_id
    ).all()

    return {

        "employee": {

            "emp_id": employee.emp_id,
            "emp_name": employee.emp_name,
            "department": employee.department,
            "designation": employee.designation,
            "role": employee.role

        },

        "shifts": [

            {

                "date": str(s.shift_date),
                "shift_name": s.shift_name,
                "start_time": str(s.start_time),
                "end_time": str(s.end_time)

            }

            for s in shifts
        ],

        "attendance": [

            {

                "date": str(a.attendance_date),
                "shift_name": a.shift_name,
                "status": a.status

            }

            for a in attendance
        ]
    }
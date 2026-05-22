from pydantic import BaseModel

from datetime import time
from datetime import date


# ==========================================
# EMPLOYEE
# ==========================================

class EmployeeCreate(BaseModel):

    emp_id: str
    name: str
    department: str
    role: str
    password: str


# ==========================================
# LOGIN
# ==========================================

class LoginSchema(BaseModel):

    emp_id: str
    password: str


# ==========================================
# SHIFT
# ==========================================

class ShiftCreate(BaseModel):

    shift_name: str
    start_time: time
    end_time: time
    grace_minutes: int


# ==========================================
# ROSTER
# ==========================================

class RosterCreate(BaseModel):

    emp_id: str
    shift_id: int
    shift_date: date


# ==========================================
# ATTENDANCE
# ==========================================

class AttendanceCreate(BaseModel):

    emp_id: str


# ==========================================
# LEAVE
# ==========================================

class LeaveCreate(BaseModel):

    emp_id: str
    from_date: date
    to_date: date
    reason: str


# ==========================================
# SHIFT SWAP
# ==========================================

class ShiftSwapCreate(BaseModel):

    requester_emp_id: str
    target_emp_id: str
    shift_date: date
class ChangePassword(BaseModel):

    old_password: str

    new_password: str
# ==========================================
# SHIFT ASSIGNMENT
# ==========================================

class ShiftAssignmentCreate(BaseModel):

    employee_id: int

    shift_id: int

    shift_date: date


# ==========================================
# SWAP APPROVAL
# ==========================================

class ShiftSwapApproval(BaseModel):

    status: str





class MarkAttendance(BaseModel):

    status: str

    late_minutes: int = 0

    ot_hours: float = 0
from pydantic import BaseModel


# ==========================================
# LOGIN SCHEMA
# ==========================================

class LoginSchema(BaseModel):

    emp_id: str

    password: str

    role: str


# ==========================================
# REGISTER SCHEMA
# ==========================================

class RegisterSchema(BaseModel):

    emp_id: str

    name: str

    password: str

    department: str

    role: str


# ==========================================
# CHANGE PASSWORD SCHEMA
# ==========================================

class ChangePasswordSchema(BaseModel):

    old_password: str

    new_password: str
from typing import Optional


# ==========================================
# ATTENDANCE SCHEMA
# ==========================================

class AttendanceSchema(BaseModel):

    employee_id: int

    attendance_date: str

    status: str

    remarks: Optional[str] = None


# ==========================================
# ADMIN MARK ATTENDANCE
# ==========================================

class AdminAttendanceSchema(BaseModel):

    employee_id: int

    status: str

    check_in: Optional[str] = None

    check_out: Optional[str] = None

    remarks: Optional[str] = None

# ==========================================
# EMPLOYEE UPDATE SCHEMA
# ==========================================

class EmployeeUpdateSchema(BaseModel):

    name: str

    department: str

    role: str

    is_active: bool
# =====================================================
# SHIFT SCHEMAS
# =====================================================

class ShiftCreateSchema(BaseModel):

    shift_name: str

    start_time: str

    end_time: str


class ShiftAssignSchema(BaseModel):

    employee_id: int

    shift_id: int

    shift_date: date


class ShiftSwapSchema(BaseModel):

    requester_id: int

    receiver_id: int

    requester_shift_id: int

    receiver_shift_id: int

    reason: str
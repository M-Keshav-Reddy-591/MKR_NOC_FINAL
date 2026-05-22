from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

# =========================
# AUTH
# =========================

class RegisterSchema(BaseModel):
    employee_id: str
    full_name: str
    password: str
    role: str = "employee"


class LoginSchema(BaseModel):
    employee_id: str
    password: str


# =========================
# EMPLOYEE
# =========================

class EmployeeResponse(BaseModel):
    id: int
    employee_id: str
    full_name: str
    role: str

    class Config:
        from_attributes = True


# =========================
# ATTENDANCE
# =========================

class AttendanceCreate(BaseModel):
    employee_id: int
    status: str
    remarks: Optional[str] = None


class AttendanceResponse(BaseModel):
    id: int
    employee_id: int
    status: str
    check_in: Optional[datetime]
    check_out: Optional[datetime]
    remarks: Optional[str]

    class Config:
        from_attributes = True


# =========================
# SHIFT
# =========================

class ShiftCreate(BaseModel):
    shift_name: str
    start_time: str
    end_time: str


class ShiftResponse(BaseModel):
    id: int
    shift_name: str
    start_time: str
    end_time: str

    class Config:
        from_attributes = True

# =========================
# SHIFT ASSIGNMENT
# =========================

class ShiftAssignSchema(BaseModel):
    employee_id: int
    shift_id: int
    assigned_date: date


class ShiftAssignmentResponseSchema(BaseModel):
    id: int
    employee_id: int
    shift_id: int
    assigned_date: date

    class Config:
        from_attributes = True

# =========================
# SHIFT SWAP
# =========================

class ShiftSwapCreate(BaseModel):
    requester_id: int
    receiver_id: int
    requester_shift_id: int
    receiver_shift_id: int
    reason: Optional[str] = None
# =========================
# ADMIN ATTENDANCE
# =========================

class AdminAttendanceSchema(BaseModel):
    employee_id: int
    status: str
    check_in: Optional[datetime] = None
    check_out: Optional[datetime] = None
    remarks: Optional[str] = None
# =========================
# EMPLOYEE UPDATE
# =========================

class EmployeeUpdateSchema(BaseModel):
    full_name: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None
class ShiftCreateSchema(BaseModel):
    shift_name: str
    start_time: str
    end_time: str
class ShiftResponseSchema(BaseModel):
    id: int
    shift_name: str
    start_time: str
    end_time: str

    class Config:
        from_attributes = True
# =========================
# SHIFT SWAP
# =========================

class ShiftSwapSchema(BaseModel):
    requester_emp_id: int
    target_emp_id: int
    requester_shift_id: int
    target_shift_id: int
    swap_date: date
    reason: Optional[str] = None


class ShiftSwapResponseSchema(BaseModel):
    id: int
    requester_emp_id: int
    target_emp_id: int
    requester_shift_id: int
    target_shift_id: int
    swap_date: date
    reason: Optional[str]
    status: str

    class Config:
        from_attributes = True


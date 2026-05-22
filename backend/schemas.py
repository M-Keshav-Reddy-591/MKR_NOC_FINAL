from pydantic import BaseModel
from datetime import datetime, date, time


# =========================================
# LOGIN SCHEMA
# =========================================

class LoginSchema(BaseModel):
    emp_id: str
    password: str


# =========================================
# EMPLOYEE SCHEMA
# =========================================

class RegisterSchema(BaseModel):
    emp_id: str
    emp_name: str
    department: str
    designation: str
    password: str
    role: str = "employee"

    class Config:
        from_attributes = True


# =========================================
# SHIFT SCHEMA
# =========================================

class ShiftSchema(BaseModel):
    shift_name: str
    start_time: time
    end_time: time

    class Config:
        from_attributes = True


# =========================================
# ATTENDANCE SCHEMA
# =========================================

class AttendanceSchema(BaseModel):
    employee_id: int
    attendance_date: date
    status: str

    class Config:
        from_attributes = True


# =========================================
# SWAP SCHEMA
# =========================================

class SwapSchema(BaseModel):
    requester_id: int
    target_employee_id: int
    shift_date: date
    reason: str

    class Config:
        from_attributes = True
from pydantic import BaseModel
from datetime import datetime, date

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
# ATTENDANCE SCHEMA
# =========================================
class AttendanceSchema(BaseModel):

    employee_id: int

    status: str = "Present"


class AttendanceResponse(BaseModel):

    id: int

    employee_id: int

    date: date

    check_in: datetime = None

    check_out: datetime = None

    status: str

    class Config:
        from_attributes = True
class AttendanceSchema(BaseModel):

    employee_id: int

    status: str = "Present"


class AttendanceResponse(BaseModel):

    id: int

    employee_id: int

    date: date

    check_in: datetime = None

    check_out: datetime = None

    status: str

    class Config:
        from_attributes = True

class ShiftSchema(BaseModel):

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

class ShiftAssignSchema(BaseModel):

    employee_id: int

    shift_id: int


class ShiftAssignResponse(BaseModel):

    id: int

    employee_id: int

    shift_id: int

    assigned_date: date

    class Config:
        from_attributes = True
class LeaveSchema(BaseModel):

    employee_id: int

    leave_type: str

    start_date: date

    end_date: date

    reason: str


class LeaveStatusSchema(BaseModel):

    status: str
class ShiftSwapSchema(BaseModel):

    requester_id: int

    target_employee_id: int

    current_shift_id: int

    requested_shift_id: int


class ShiftSwapResponse(BaseModel):

    id: int

    requester_id: int

    target_employee_id: int

    current_shift_id: int

    requested_shift_id: int

    status: str

    class Config:
        from_attributes = True
class ShiftSchema(BaseModel):

    shift_name: str
    start_time: str
    end_time: str
    description: str


class ShiftAssignSchema(BaseModel):

    employee_id: int
    shift_id: int
    assigned_date: date
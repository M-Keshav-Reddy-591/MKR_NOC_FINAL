from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Time
from sqlalchemy import ForeignKey

# =========================================
# EMPLOYEE TABLE
# =========================================

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    emp_id = Column(String(50), unique=True, nullable=False)

    emp_name = Column(String(100), nullable=False)

    department = Column(String(100))

    designation = Column(String(100))

    password = Column(String(100), nullable=False)

    role = Column(String(20), default="employee")


# =========================================
# ATTENDANCE TABLE
# =========================================

class Attendance(Base):

    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    attendance_date = Column(Date)

    check_in = Column(Time)

    check_out = Column(Time)

    status = Column(String(50))

class Shift(Base):

    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True, index=True)

    shift_name = Column(String(100))

    start_time = Column(String(20))

    end_time = Column(String(20))

    description = Column(String(255))

class ShiftAssignment(Base):

    __tablename__ = "shift_assignments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    shift_id = Column(
        Integer,
        ForeignKey("shifts.id")
    )

    assigned_date = Column(Date)
class Leave(Base):

    __tablename__ = "leaves"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    leave_type = Column(
        String(100)
    )

    start_date = Column(Date)

    end_date = Column(Date)

    reason = Column(String(255))

    status = Column(
        String(50),
        default="Pending"
    )
class ShiftSwap(Base):

    __tablename__ = "shift_swaps"

    id = Column(Integer, primary_key=True, index=True)

    requester_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    target_employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    current_shift_id = Column(
        Integer,
        ForeignKey("shifts.id")
    )

    requested_shift_id = Column(
        Integer,
        ForeignKey("shifts.id")
    )

    status = Column(String(50), default="Pending")










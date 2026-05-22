from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    Time,
    ForeignKey,
    Boolean
)

from sqlalchemy.orm import relationship

from database import Base

from datetime import datetime


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    emp_id = Column(String(50), unique=True)

    name = Column(String(100))

    password = Column(String(255))

    department = Column(String(100))

    role = Column(String(20), default="employee")

    is_active = Column(Boolean, default=True)


class Shift(Base):
    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True, index=True)

    shift_name = Column(String(100))

    start_time = Column(Time)

    end_time = Column(Time)


class ShiftAssignment(Base):
    __tablename__ = "shift_assignments"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    shift_id = Column(
        Integer,
        ForeignKey("shifts.id")
    )

    shift_date = Column(Date)

    employee = relationship("Employee")

    shift = relationship("Shift")


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    attendance_date = Column(Date)

    status = Column(String(20))

    check_in = Column(DateTime, nullable=True)

    check_out = Column(DateTime, nullable=True)

    remarks = Column(String(255), nullable=True)

    employee = relationship("Employee")


class ShiftSwap(Base):
    __tablename__ = "shift_swaps"

    id = Column(Integer, primary_key=True, index=True)

    requester_emp_id = Column(String(50))

    target_emp_id = Column(String(50))

    requester_shift_id = Column(Integer)

    target_shift_id = Column(Integer)

    swap_date = Column(Date)

    status = Column(String(20), default="pending")

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
# =====================================================
# SHIFT TABLE
# =====================================================

class Shift(Base):

    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True, index=True)

    shift_name = Column(String(100))

    start_time = Column(String(20))

    end_time = Column(String(20))

    is_active = Column(Boolean, default=True)


# =====================================================
# SHIFT ASSIGNMENT TABLE
# =====================================================

class ShiftAssignment(Base):

    __tablename__ = "shift_assignments"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, ForeignKey("employees.id"))

    shift_id = Column(Integer, ForeignKey("shifts.id"))

    shift_date = Column(Date)

    created_at = Column(DateTime, default=datetime.utcnow)


# =====================================================
# SHIFT SWAP TABLE
# =====================================================

class ShiftSwap(Base):

    __tablename__ = "shift_swaps"

    id = Column(Integer, primary_key=True, index=True)

    requester_id = Column(Integer)

    receiver_id = Column(Integer)

    requester_shift_id = Column(Integer)

    receiver_shift_id = Column(Integer)

    reason = Column(String(500))

    status = Column(String(50), default="pending")

    created_at = Column(DateTime, default=datetime.utcnow)
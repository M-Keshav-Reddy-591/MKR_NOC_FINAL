from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Boolean,
    Float,
    Time,
    Date
)

from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Text
from sqlalchemy import ForeignKey
# ==========================================
# EMPLOYEE
# ==========================================

class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    emp_id = Column(String(50), unique=True)

    name = Column(String(100))

    department = Column(String(100))

    role = Column(String(20))

    password = Column(String(255))


# ==========================================
# SHIFTS
# ==========================================

class Shift(Base):

    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True, index=True)

    shift_name = Column(String(50))

    start_time = Column(Time)

    end_time = Column(Time)

    grace_minutes = Column(Integer)


# ==========================================
# ROSTER
# ==========================================

class Roster(Base):

    __tablename__ = "roster"

    id = Column(Integer, primary_key=True, index=True)

    emp_id = Column(String(50))

    shift_id = Column(Integer)

    shift_date = Column(Date)


class Attendance(Base):

    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, ForeignKey("employees.id"))

    date = Column(Date)

    status = Column(String(50))

    login_time = Column(Time, nullable=True)

    logout_time = Column(Time, nullable=True)

    ot_hours = Column(Float, default=0)

    remarks = Column(String(255), nullable=True)

    employee = relationship("Employee")

# ==========================================
# SHIFT SWAP
# ==========================================

class ShiftSwap(Base):

    __tablename__ = "shift_swaps"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    requester_emp_id = Column(
        String(50)
    )


    target_emp_id = Column(
        String(50)
    )


    shift_date = Column(
        Date
    )


    requester_shift = Column(
        String(100)
    )


    target_shift = Column(
        String(100)
    )


    reason = Column(
        String(255)
    )


    status = Column(
        String(30),
        default="Pending"
    )
# ==========================================
# LEAVES
# ==========================================

class Leave(Base):

    __tablename__ = "leaves"

    id = Column(Integer, primary_key=True, index=True)

    emp_id = Column(String(50))

    from_date = Column(Date)

    to_date = Column(Date)

    reason = Column(Text)

    status = Column(String(20))


# ==========================================
# SHIFT ASSIGNMENT
# ==========================================

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
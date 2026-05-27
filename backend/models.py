from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    Time,
    ForeignKey,
    Text
)

from database import Base



class Employee(Base):

    __tablename__ = "employees"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    emp_id = Column(
        String(50),
        unique=True
    )

    emp_name = Column(
        String(100)
    )

    department = Column(
        String(100)
    )

    designation = Column(
        String(100)
    )

    password = Column(
        String(255)
    )

    role = Column(
        String(50)
    )


class Attendance(Base):

    __tablename__ = "attendance"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    attendance_date = Column(Date)

    check_in = Column(
        DateTime,
        default=datetime.utcnow
    )

    check_out = Column(DateTime)

    status = Column(
        String(50)
    )


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

    shift_name = Column(
        String(50)
    )

    start_time = Column(Time)

    end_time = Column(Time)

    shift_date = Column(Date)

    holiday_note = Column(Text)
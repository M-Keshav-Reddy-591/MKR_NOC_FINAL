from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    Time,
    ForeignKey,
    Text,
    Boolean
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

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(String(50))

    attendance_date = Column(Date)

    status = Column(String(50))

    shift_name = Column(String(100))

    check_in = Column(DateTime, default=datetime.utcnow)

class ShiftAssignment(Base):

    __tablename__ = "shift_assignments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_id = Column(
        String(50)
    )

    shift_name = Column(
        String(50)
    )

    start_time = Column(Time)

    end_time = Column(Time)

    shift_date = Column(Date)

    is_holiday = Column(
        Boolean,
        default=False
    )

    holiday_note = Column(
        String(500)
    )

class Leave(Base):

    __tablename__ = "leaves"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_id = Column(
        String(50)
    )

    leave_date = Column(
        Date
    )

    shift_name = Column(
        String(100)
    )

    leave_type = Column(
        String(100)
    )

    reason = Column(
        String(500)
    )

    status = Column(
        String(50),
        default="Pending"
    )


class PasswordLog(Base):

    __tablename__ = "password_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_id = Column(
        String(50)
    )

    employee_name = Column(
        String(100)
    )

    changed_by = Column(
        String(50)
    )

    changed_at = Column(
        DateTime,
        default=datetime.utcnow
    )

class Notification(Base):

    __tablename__ = "notifications"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_id = Column(
        String(50)
    )

    title = Column(
        String(255)
    )

    message = Column(
        Text
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    is_read = Column(
        Boolean,
        default=False
    )
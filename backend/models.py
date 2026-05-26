from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Time
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from datetime import datetime
from database import get_db
from database import Base



class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(String(20), unique=True, index=True)
    emp_name = Column(String(100))
    department = Column(String(100))
    designation = Column(String(100))
    password = Column(String(255))
    role = Column(String(20))

class ShiftAssignment(Base):
    __tablename__ = "shift_assignments"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    shift_name = Column(String(50))
    start_time = Column(Time)
    end_time = Column(Time)
    shift_date = Column(Date)

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    status = Column(String(20))
    check_in = Column(DateTime, default=datetime.utcnow)
    check_out = Column(DateTime, nullable=True)

class HolidayWorkLog(Base):
    __tablename__ = "holiday_work_log"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    shift_date = Column(Date)
    shift_name = Column(String(50))
    note = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class ManualShiftAssignment(Base):
    __tablename__ = "manual_shift_assignments"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    shift_date = Column(Date)
    shift_name = Column(String(50))
    is_holiday = Column(Integer, default=0)  # use 0/1 for boolean
    holiday_note = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)








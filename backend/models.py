from sqlalchemy import Column, Integer, String, Date, DateTime, Time, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(String(50), unique=True, nullable=False)
    emp_name = Column(String(100))
    department = Column(String(100))
    designation = Column(String(100))
    password = Column(String(255))
    role = Column(String(20), default="employee")


class Attendance(Base):

    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    status = Column(String(20))

    check_in = Column(String(20))

    check_out = Column(String(20))

    remarks = Column(String(255))

    created_at = Column(DateTime, default=datetime.utcnow)
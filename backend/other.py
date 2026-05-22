from sqlalchemy import Column, Integer, String, Date
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(String(50), unique=True)
    name = Column(String(100))
    department = Column(String(100))


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(String(50))
    date = Column(Date)
    status = Column(String(20))
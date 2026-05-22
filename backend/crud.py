from sqlalchemy.orm import Session
import models
import schemas

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        emp_id=employee.emp_id,
        name=employee.name,
        department=employee.department
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


def mark_attendance(db: Session, attendance: schemas.AttendanceCreate):
    db_attendance = models.Attendance(
        emp_id=attendance.emp_id,
        date=attendance.date,
        status=attendance.status
    )

    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)

    return db_attendance


def get_attendance(db: Session):
    return db.query(models.Attendance).all()
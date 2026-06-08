from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
import database
import models
from database import get_db
from models import Employee
from database import SessionLocal
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/v1/employees",
    tags=["Employees"]
)

# @router.get("")
# def get_employees(
#     db: Session = Depends(database.get_db)
# ):

#     employees = db.query(models.Employee).all()

#     return employees



# =====================================================
# GET ALL EMPLOYEES
# =====================================================

@router.get("")
def get_employees(
    db: Session = Depends(get_db)
):

    employees = db.query(
        Employee
    ).all()

    result = []

    for emp in employees:

        result.append({

            "Employee ID": emp.emp_id,

            "Name": emp.emp_name,

            "Department": emp.department,

            "Designation": emp.designation,

            "Phone": emp.phone_number,

            "Email": emp.email,

            "Role": emp.role

        })

    return result


# # ======================================================
# # GET ALL EMPLOYEES
# # ======================================================

# @router.get("/")
# def get_employees(
#     db: Session = Depends(get_db)
# ):

#     employees = db.query(
#         Employee
#     ).all()

#     result = []

#     for emp in employees:

#         result.append({

#             "id": emp.id,

#             "emp_id": emp.emp_id,

#             "name": emp.emp_name,

#             "department": emp.department,

#             "designation": emp.designation,

#             "role": emp.role

#         })

#     return result

@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(database.get_db)
):

    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

    if employee:

        db.delete(employee)

        db.commit()

    return {
        "message": "Employee Deleted"
    }




class PasswordChange(BaseModel):

    password: str

@router.put("/change-password/{emp_id}")
def change_password(
    emp_id: str,
    data: PasswordChange
):

    db = SessionLocal()

    employee = db.query(
        models.Employee
    ).filter(
        models.Employee.emp_id == emp_id
    ).first()

    if not employee:

        return {
            "message": "Employee Not Found"
        }

    employee.password = bcrypt.hash(
        data.password
    )

    db.commit()

    return {
        "message": "Password Updated Successfully"
    }

@router.put("/update/{emp_id}")
def update_employee(
    emp_id: str,
    data: dict,
    db: Session = Depends(get_db)
):

    employee = db.query(
        Employee
    ).filter(
        Employee.emp_id == emp_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    employee.emp_name = data.get(
        "emp_name",
        employee.emp_name
    )

    employee.department = data.get(
        "department",
        employee.department
    )

    employee.designation = data.get(
        "designation",
        employee.designation
    )

    employee.phone_number = data.get(
        "phone_number",
        employee.phone_number
    )

    employee.email = data.get(
        "email",
        employee.email
    )

    employee.role = data.get(
        "role",
        employee.role
    )

    db.commit()

    return {
        "message": "Employee updated successfully"
    }








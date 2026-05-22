from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query

from sqlalchemy.orm import Session

from database import get_db

import models
import schemas

from auth import get_current_user


router = APIRouter(
    prefix="/api/v1/employees",
    tags=["Employees"]
)


# =====================================================
# GET CURRENT EMPLOYEE PROFILE
# =====================================================

@router.get("/profile")
def employee_profile(
    current_user: models.Employee = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "emp_id": current_user.emp_id,
        "name": current_user.name,
        "department": current_user.department,
        "role": current_user.role,
        "is_active": current_user.is_active
    }


# =====================================================
# GET ALL EMPLOYEES
# =====================================================

@router.get("/all")
def get_all_employees(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    employees = db.query(models.Employee).all()

    result = []

    for employee in employees:

        result.append({
            "id": employee.id,
            "emp_id": employee.emp_id,
            "name": employee.name,
            "department": employee.department,
            "role": employee.role,
            "is_active": employee.is_active
        })

    return result


# =====================================================
# SEARCH EMPLOYEE
# =====================================================

@router.get("/search")
def search_employee(
    keyword: str = Query(...),
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    employees = db.query(models.Employee).filter(
        models.Employee.name.contains(keyword)
    ).all()

    result = []

    for employee in employees:

        result.append({
            "id": employee.id,
            "emp_id": employee.emp_id,
            "name": employee.name,
            "department": employee.department,
            "role": employee.role
        })

    return result


# =====================================================
# FILTER BY DEPARTMENT
# =====================================================

@router.get("/department/{department_name}")
def employees_by_department(
    department_name: str,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    employees = db.query(models.Employee).filter(
        models.Employee.department == department_name
    ).all()

    result = []

    for employee in employees:

        result.append({
            "id": employee.id,
            "emp_id": employee.emp_id,
            "name": employee.name,
            "role": employee.role
        })

    return result


# =====================================================
# UPDATE EMPLOYEE
# =====================================================

@router.put("/update/{employee_id}")
def update_employee(
    employee_id: int,
    employee_data: schemas.RegisterSchema,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    employee.name = employee_data.name
    employee.department = employee_data.department
    employee.role = employee_data.role
    employee.is_active = employee_data.is_active

    db.commit()

    return {
        "message": "Employee updated successfully"
    }


# =====================================================
# DELETE EMPLOYEE
# =====================================================

@router.delete("/delete/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db.delete(employee)

    db.commit()

    return {
        "message": "Employee deleted successfully"
    }


# =====================================================
# EMPLOYEE DASHBOARD STATS
# =====================================================

@router.get("/stats")
def employee_stats(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    total_employees = db.query(models.Employee).count()

    active_employees = db.query(models.Employee).filter(
        models.Employee.is_active == True
    ).count()

    admins = db.query(models.Employee).filter(
        models.Employee.role == "admin"
    ).count()

    normal_employees = db.query(models.Employee).filter(
        models.Employee.role == "employee"
    ).count()

    return {
        "total_employees": total_employees,
        "active_employees": active_employees,
        "admins": admins,
        "employees": normal_employees
    }
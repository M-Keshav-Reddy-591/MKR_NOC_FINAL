from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas

from database import get_db
from utils.jwt_handler import create_access_token
from utils.security import (
    hash_password,
    verify_password
)
router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)

@router.post("/register")

def register_user(
    user_data: schemas.RegisterSchema,
    db: Session = Depends(get_db)
):

    existing_user = db.query(
        models.Employee
    ).filter(
        models.Employee.emp_id == user_data.emp_id
    ).first()

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Employee ID already exists"
        )

    hashed_password = hash_password(
        user_data.password
    )

    new_user = models.Employee(

        emp_id=user_data.emp_id,
        emp_name=user_data.emp_name,
        department=user_data.department,
        designation=user_data.designation,
        password=hashed_password,
        role=user_data.role
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }


from models import Employee



@router.post("/login")
def login(
    data: dict,
    db: Session = Depends(get_db)
):

    emp_id = data.get("emp_id")
    password = data.get("password")
    role = data.get("role")

    user = db.query(Employee).filter(
        Employee.emp_id == emp_id
    ).first()

    # USER NOT FOUND

    if not user:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    # PASSWORD VERIFY

    if not verify_password(
        password,
        user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    # ROLE VERIFY

    if user.role != role:

        raise HTTPException(
            status_code=401,
            detail="Invalid role selected"
        )

    # JWT TOKEN

    access_token = create_access_token(
        data={
            "sub": user.emp_id,
            "role": user.role
        }
    )

    return {

        "message": "Login successful",

        "access_token": access_token,

        "role": user.role,

        "emp_id": user.emp_id,

        "emp_name": user.emp_name,

        "employee_id": user.id
    }

@router.get("/reset-test-password")
def reset_test_password(
    db: Session = Depends(get_db)
):

    user = db.query(Employee).filter(
        Employee.emp_id == "EMP001"
    ).first()

    user.password = hash_password("admin123")

    db.commit()

    return {
        "message": "Password reset success"
    }













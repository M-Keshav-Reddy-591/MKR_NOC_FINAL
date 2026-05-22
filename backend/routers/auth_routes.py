from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas

from database import get_db
from utils.jwt_handler import create_access_token

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register_user(
    user_data: schemas.RegisterSchema,
    db: Session = Depends(get_db)
):

    existing_user = db.query(models.Employee).filter(
        models.Employee.employee_id == user_data.employee_id
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Employee ID already exists"
        )

    new_user = models.Employee(
        employee_id=user_data.employee_id,
        full_name=user_data.full_name,
        password=user_data.password,
        department=user_data.department,
        designation=user_data.designation,
        phone=user_data.phone,
        role=user_data.role
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login_user(
    login_data: schemas.LoginSchema,
    db: Session = Depends(get_db)
):

    user = db.query(models.Employee).filter(
        models.Employee.employee_id == login_data.employee_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Employee ID not found"
        )

    if user.password != login_data.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token(
        {
            "employee_id": user.employee_id,
            "role": user.role
        }
    )

    return {
        "message": "Login successful",
        "token": token,
        "role": user.role,
        "employee_name": user.full_name
    }
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

@router.post("/login")

def login_user(
    login_data: schemas.LoginSchema,
    db: Session = Depends(get_db)
):

    user = db.query(
        models.Employee
    ).filter(
        models.Employee.emp_id == login_data.emp_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid Employee ID"
        )

    password_valid = verify_password(
        login_data.password,
        user.password
    )

    if not password_valid:

        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    access_token = create_access_token(
        data={
            "sub": user.emp_id,
            "role": user.role
        }
    )

    return {

        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role,
        "emp_name": user.emp_name
    }
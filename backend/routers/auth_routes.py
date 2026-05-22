from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database import get_db

import models
import schemas

from auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


# ==========================================
# REGISTER
# ==========================================

@router.post("/register")
def register_user(
    user_data: schemas.RegisterSchema,
    db: Session = Depends(get_db)
):

    existing_user = db.query(models.Employee).filter(
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
        name=user_data.name,
        password=hashed_password,
        department=user_data.department,
        role=user_data.role
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }


# ==========================================
# LOGIN
# ==========================================

@router.post("/login")
def login_user(
    login_data: schemas.LoginSchema,
    db: Session = Depends(get_db)
):

    user = db.query(models.Employee).filter(
        models.Employee.emp_id == login_data.emp_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Employee ID"
        )

    password_verified = verify_password(
        login_data.password,
        user.password
    )

    if not password_verified:
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    if user.role != login_data.role:
        raise HTTPException(
            status_code=401,
            detail="Wrong Login Type"
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
        "user": {
            "id": user.id,
            "emp_id": user.emp_id,
            "name": user.name,
            "department": user.department,
            "role": user.role
        }
    }


# ==========================================
# CURRENT USER
# ==========================================

@router.get("/me")
def get_me(
    current_user: models.Employee = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "emp_id": current_user.emp_id,
        "name": current_user.name,
        "department": current_user.department,
        "role": current_user.role
    }


# ==========================================
# CHANGE PASSWORD
# ==========================================

@router.put("/change-password")
def change_password(
    password_data: dict,
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(get_current_user)
):

    old_password = password_data.get("old_password")

    new_password = password_data.get("new_password")

    password_verified = verify_password(
        old_password,
        current_user.password
    )

    if not password_verified:
        raise HTTPException(
            status_code=400,
            detail="Old password incorrect"
        )

    current_user.password = hash_password(
        new_password
    )

    db.commit()

    return {
        "message": "Password updated successfully"
    }
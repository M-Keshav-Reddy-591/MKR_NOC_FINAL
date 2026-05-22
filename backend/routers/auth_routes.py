from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

import models
from database import SessionLocal
from dependencies import get_current_user

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)

SECRET_KEY = "SECRET123"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# DATABASE CONNECTION
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# PASSWORD HASH
def hash_password(password: str):
    return pwd_context.hash(password)


# PASSWORD VERIFY
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# TOKEN CREATE
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=10)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# REGISTER
@router.post("/register")
def register_user(
    employee: dict,
    db: Session = Depends(get_db)
):

    existing_user = db.query(models.Employee).filter(
        models.Employee.email == employee["email"]
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = models.Employee(
        emp_id=employee["emp_id"],
        name=employee["name"],
        email=employee["email"],
        department=employee["department"],
        password=hash_password(employee["password"]),
        role=employee.get("role", "employee")
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }


# LOGIN
@router.post("/login")
def login_user(
    login_data: dict,
    db: Session = Depends(get_db)
):

    emp_id = login_data.get("emp_id")
    password = login_data.get("password")
    role = login_data.get("role")

    user = db.query(models.Employee).filter(
        models.Employee.emp_id == emp_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Employee ID"
        )

    password_verified = verify_password(
        password,
        user.password
    )

    if not password_verified:
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    if user.role != role:
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
            "role": user.role,
            "department": user.department
        }
    }

# CURRENT USER
@router.get("/me")
def get_me(
    current_user: models.Employee = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "emp_id": current_user.emp_id,
        "name": current_user.name,
        "email": current_user.email,
        "role": current_user.role,
        "department": current_user.department
    }
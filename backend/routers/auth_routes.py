from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

import models

from database import get_db

from utils.security import (
    hash_password,
    verify_password
)

from utils.jwt_handler import (
    create_access_token
)

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)

@router.post("/login")
def login(
    data: dict,
    db: Session = Depends(get_db)
):

    emp_id = data.get("emp_id")
    password = data.get("password")

    user = db.query(models.Employee).filter(
        models.Employee.emp_id == emp_id
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

    # SUCCESS

    return {

        "message": "Login successful",

        "employee": {

            "id": user.id,
            "emp_id": user.emp_id,
            "name": user.emp_name,
            "role": user.role
        }
    }

@router.post("/register")
def register_user(
    data: dict,
    db: Session = Depends(get_db)
):

    emp_id = data.get("emp_id")

    existing_user = db.query(
        models.Employee
    ).filter(
        models.Employee.emp_id == emp_id
    ).first()

    # CHECK EXISTING USER

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Employee ID already exists"
        )

    # HASH PASSWORD

    hashed_password = hash_password(
        data.get("password")
    )

    # CREATE USER

    new_user = models.Employee(

        emp_id=data.get("emp_id"),
        emp_name=data.get("emp_name"),
        department=data.get("department"),
        designation=data.get("designation"),
        role=data.get("role"),
        password=hashed_password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {

        "message": "Employee Registered Successfully"
    }


@router.post("/change-password")
def change_password(
    data: dict,
    db: Session = Depends(get_db)
):

    employee_id = data.get(
        "employee_id"
    )

    old_password = data.get(
        "old_password"
    )

    new_password = data.get(
        "new_password"
    )

    user = db.query(
        models.Employee
    ).filter(
        models.Employee.emp_id == employee_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if not verify_password(
        old_password,
        user.password
    ):

        raise HTTPException(
            status_code=400,
            detail="Old password incorrect"
        )

    user.password = hash_password(
        new_password
    )

    db.commit()

    return {
        "message": "Password updated"
    }
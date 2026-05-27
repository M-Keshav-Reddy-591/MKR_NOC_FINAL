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

    role = data.get("role")

    user = db.query(
        models.Employee
    ).filter(
        models.Employee.emp_id == emp_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    if user.role != role:

        raise HTTPException(
            status_code=401,
            detail="Invalid role"
        )

    if not verify_password(
        password,
        user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    access_token = create_access_token(
        {
            "sub": user.emp_id
        }
    )

    return {

        "access_token": access_token,

        "role": user.role,

        "emp_id": user.emp_id,

        "emp_name": user.emp_name,

        "employee_id": user.id
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
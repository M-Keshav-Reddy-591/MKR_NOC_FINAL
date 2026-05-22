from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import SessionLocal

import models
import auth


router = APIRouter()


# ==========================================
# DATABASE
# ==========================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ==========================================
# GET ALL EMPLOYEES
# ==========================================

@router.get("/all")
def get_all_employees(

    db: Session = Depends(get_db),

    current_user: models.Employee = Depends(
        auth.get_current_user
    )
):

    return db.query(
        models.Employee
    ).all()
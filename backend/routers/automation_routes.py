from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

import auth
import models

from database import SessionLocal

from automation.auto_absent import (
    mark_absent_employees
)


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
# RUN AUTO ABSENT
# ==========================================

@router.post("/run-auto-absent")
def run_auto_absent(
    db: Session = Depends(get_db),
    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    result = mark_absent_employees(db)

    return result
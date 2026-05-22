from fastapi import APIRouter
from fastapi import Depends
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database import SessionLocal

import models
import schemas
import auth
from dependencies import get_current_user
import pandas as pd


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
# ASSIGN SHIFT
# ==========================================

@router.post("/assign-shift")
def assign_shift(

    shift_data: schemas.ShiftAssignmentCreate,

    db: Session = Depends(get_db),

    current_user: models.Employee = Depends(
        auth.get_current_user
    )
):

    if current_user.role != "admin":

        raise HTTPException(

            status_code=403,

            detail="Only Admin Allowed"
        )


    assignment = models.ShiftAssignment(

        employee_id=shift_data.employee_id,

        shift_id=shift_data.shift_id,

        shift_date=shift_data.shift_date
    )


    db.add(assignment)

    db.commit()

    db.refresh(assignment)


    return {

        "message":
        "Shift Assigned Successfully"
    }


# ==========================================
# GET EMPLOYEE SCHEDULE
# ==========================================

@router.get("/my-schedule")
def get_my_schedule(

    db: Session = Depends(get_db),

    current_user: models.Employee = Depends(
        auth.get_current_user
    )
):

    schedules = db.query(

        models.ShiftAssignment

    ).filter(

        models.ShiftAssignment.employee_id
        == current_user.id

    ).all()


    result = []


    for item in schedules:

        result.append({

            "date": item.shift_date,

            "shift":
            item.shift.shift_name,

            "start_time":
            item.shift.start_time,

            "end_time":
            item.shift.end_time
        })


    return result


# ==========================================
# CSV ROSTER UPLOAD
# ==========================================

@router.post("/upload-roster")
async def upload_roster(

    file: UploadFile = File(...),

    db: Session = Depends(get_db),

    current_user: models.Employee = Depends(
        auth.get_current_user
    )
):

    if current_user.role != "admin":

        raise HTTPException(

            status_code=403,

            detail="Only Admin Allowed"
        )


    df = pd.read_csv(file.file)


    for _, row in df.iterrows():

        employee = db.query(

            models.Employee

        ).filter(

            models.Employee.emp_id
            == row["emp_id"]

        ).first()


        shift = db.query(

            models.Shift

        ).filter(

            models.Shift.shift_name
            == row["shift_name"]

        ).first()


        if employee and shift:

            assignment = models.ShiftAssignment(

                employee_id=employee.id,

                shift_id=shift.id,

                shift_date=row["shift_date"]
            )

            db.add(assignment)


    db.commit()


    return {

        "message":
        "Roster Uploaded Successfully"
    }
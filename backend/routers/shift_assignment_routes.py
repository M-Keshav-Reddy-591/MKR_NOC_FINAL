from fastapi import APIRouter
from database import SessionLocal
import models
import schemas

router = APIRouter(
    prefix="/api/v1/shift-assignments",
    tags=["Shift Assignments"]
)

@router.post("/assign")

def assign_shift(
    shift_data: schemas.ShiftAssignSchema
):

    db = SessionLocal()

    assignment = models.ShiftAssignment(

        employee_id=shift_data.employee_id,
        shift_id=shift_data.shift_id,
        assigned_date=shift_data.assigned_date
    )

    db.add(assignment)

    db.commit()

    return {
        "message": "Shift assigned successfully"
    }


@router.get("/all")

def get_assignments():

    db = SessionLocal()

    return db.query(
        models.ShiftAssignment
    ).all()
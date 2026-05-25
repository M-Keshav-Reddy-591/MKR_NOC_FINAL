from fastapi import APIRouter
from database import SessionLocal
import models
import schemas

router = APIRouter(
    prefix="/api/v1/shifts",
    tags=["Shifts"]
)

@router.post("/create")

def create_shift(
    shift_data: schemas.ShiftSchema
):

    db = SessionLocal()

    shift = models.Shift(

        shift_name=shift_data.shift_name,
        start_time=shift_data.start_time,
        end_time=shift_data.end_time,
        description=shift_data.description
    )

    db.add(shift)

    db.commit()

    return {
        "message": "Shift created successfully"
    }


@router.get("/all")

def get_shifts():

    db = SessionLocal()

    return db.query(
        models.Shift
    ).all()
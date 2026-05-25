from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

import database
import models
import csv
import io

router = APIRouter(
    prefix="/api/v1/shifts",
    tags=["Shifts"]
)

@router.get("")
def get_shifts(
    db: Session = Depends(database.get_db)
):

    return db.query(models.Shift).all()


@router.post("")
def create_shift(
    shift_data: dict,
    db: Session = Depends(database.get_db)
):

    new_shift = models.Shift(
        shift_name=shift_data["shift_name"],
        start_time=shift_data["start_time"],
        end_time=shift_data["end_time"]
    )

    db.add(new_shift)

    db.commit()

    db.refresh(new_shift)

    return new_shift


@router.delete("/{shift_id}")
def delete_shift(
    shift_id: int,
    db: Session = Depends(database.get_db)
):

    shift = db.query(models.Shift).filter(
        models.Shift.id == shift_id
    ).first()

    if shift:

        db.delete(shift)

        db.commit()

    return {
        "message": "Shift Deleted"
    }


@router.post("/upload-csv")
async def upload_shift_csv(
    file: UploadFile = File(...),
    db: Session = Depends(database.get_db)
):

    content = await file.read()

    csv_reader = csv.DictReader(
        io.StringIO(content.decode("utf-8"))
    )

    for row in csv_reader:

        shift = models.Shift(
            shift_name=row["shift_name"],
            start_time=row["start_time"],
            end_time=row["end_time"]
        )

        db.add(shift)

    db.commit()

    return {
        "message": "CSV Uploaded Successfully"
    }
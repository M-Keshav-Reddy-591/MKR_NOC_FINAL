from fastapi import APIRouter, UploadFile, File
from database import SessionLocal
import models
import pandas as pd

router = APIRouter(
    prefix="/api/v1/csv",
    tags=["CSV Upload"]
)

@router.post("/upload-shifts")
async def upload_shift_csv(
    file: UploadFile = File(...)
):

    db = SessionLocal()

    df = pd.read_csv(file.file)

    for _, row in df.iterrows():

        shift = models.ShiftAssignment(

            employee_id=row["employee_id"],
            shift_name=row["shift_name"],
            start_time=row["start_time"],
            end_time=row["end_time"],
            shift_date=row["shift_date"]

        )

        db.add(shift)

    db.commit()

    return {
        "message": "CSV Uploaded Successfully"
    }
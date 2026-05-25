from fastapi import APIRouter, UploadFile, File
from database import SessionLocal
import models
import csv
import io

router = APIRouter(
    prefix="/api/v1/shift-upload",
    tags=["Shift Upload"]
)

@router.post("/")
async def upload_shift_csv(
    file: UploadFile = File(...)
):

    db = SessionLocal()

    content = await file.read()

    csv_data = csv.DictReader(
        io.StringIO(
            content.decode("utf-8")
        )
    )

    inserted = 0

    for row in csv_data:

        employee = db.query(
            models.Employee
        ).filter(
            models.Employee.emp_id ==
            row["emp_id"]
        ).first()

        if employee:

            shift = models.ShiftAssignment(

                employee_id=employee.id,

                shift_name=row["shift_name"],

                start_time=row["start_time"],

                end_time=row["end_time"],

                shift_date=row["shift_date"]

            )

            db.add(shift)

            inserted += 1

    db.commit()

    return {

        "message": "Roster Uploaded",
        "inserted": inserted

    }
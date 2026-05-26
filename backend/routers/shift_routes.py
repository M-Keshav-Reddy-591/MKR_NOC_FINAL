from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from database import get_db
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
# @router.post("/manual-assign")
# def manual_assign_shift(
#     data: dict,
#     db: Session = Depends(get_db)
# ):

#     new_shift = models.ShiftAssignment(

#         employee_id=data.get("employee_id"),

#         shift_name=data.get("shift_name"),

#         shift_date=data.get("shift_date"),

#         start_time="06:00:00",

#         end_time="14:00:00"

#     )

#     db.add(new_shift)

#     db.commit()

#     # HOLIDAY WORK LOG

#     if data.get("is_holiday"):

#         holiday = models.HolidayWorkLog(

#             employee_id=data.get("employee_id"),

#             shift_date=data.get("shift_date"),

#             shift_name=data.get("shift_name"),

#             note=data.get("holiday_note")

#         )

#         db.add(holiday)

#         db.commit()

#     return {
#         "message": "Shift assigned successfully"
#     }


from models import ManualShiftAssignment, HolidayWorkLog

router = APIRouter(prefix="/api/v1/shifts", tags=["Shift Assignment"])

@router.post("/manual-assign")
def manual_assign_shift(data: dict, db: Session = Depends(get_db)):
    new_shift = ManualShiftAssignment(
        employee_id=data.get("employee_id"),
        shift_date=data.get("shift_date"),
        shift_name=data.get("shift_name"),
        is_holiday=1 if data.get("is_holiday") else 0,
        holiday_note=data.get("holiday_note")
    )
    db.add(new_shift)
    db.commit()
    if data.get("is_holiday"):
        holiday = HolidayWorkLog(
            employee_id=data.get("employee_id"),
            shift_date=data.get("shift_date"),
            shift_name=data.get("shift_name"),
            note=data.get("holiday_note")
        )
        db.add(holiday)
        db.commit()
    return {"message": "Shift assigned successfully"}

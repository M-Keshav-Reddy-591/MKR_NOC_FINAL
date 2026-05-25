from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from database import SessionLocal
import models
import csv
import io

router = APIRouter(
    prefix="/api/v1/export",
    tags=["Export"]
)

@router.get("/attendance")
def export_attendance():

    db = SessionLocal()

    attendance = db.query(models.Attendance).all()

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow([
        "Employee ID",
        "Employee Name",
        "Date",
        "Status"
    ])

    for row in attendance:

        writer.writerow([
            row.emp_id,
            row.emp_name,
            row.date,
            row.status
        ])

    output.seek(0)

    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=attendance_report.csv"
        }
    )
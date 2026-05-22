import csv

import pandas as pd

from fastapi import APIRouter
from fastapi import Depends

from fastapi.responses import FileResponse

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
# EXPORT CSV
# ==========================================

@router.get("/export-csv")
def export_csv(

    db: Session = Depends(get_db),

    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    attendance = db.query(
        models.Attendance
    ).all()

    filename = "attendance_report.csv"

    with open(
        filename,
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([

            "Employee ID",

            "Shift Date",

            "Login Time",

            "Status"
        ])

        for record in attendance:

            writer.writerow([

                record.emp_id,

                record.shift_date,

                record.login_time,

                record.status
            ])

    return FileResponse(

        path=filename,

        filename=filename,

        media_type="text/csv"
    )


# ==========================================
# EXPORT EXCEL
# ==========================================

@router.get("/export-excel")
def export_excel(

    db: Session = Depends(get_db),

    current_user: models.Employee = Depends(
        auth.admin_required
    )
):

    attendance = db.query(
        models.Attendance
    ).all()

    data = []

    for record in attendance:

        data.append({

            "Employee ID": record.emp_id,

            "Shift Date": record.shift_date,

            "Login Time": record.login_time,

            "Status": record.status
        })

    df = pd.DataFrame(data)

    filename = "attendance_report.xlsx"

    df.to_excel(

        filename,

        index=False
    )

    return FileResponse(

        path=filename,

        filename=filename,

        media_type=
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
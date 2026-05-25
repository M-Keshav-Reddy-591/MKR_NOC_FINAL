from fastapi import APIRouter
from database import SessionLocal
import models
import schemas

router = APIRouter(
    prefix="/api/v1/leaves",
    tags=["Leaves"]
)

@router.post("/apply")

def apply_leave(
    leave_data: schemas.LeaveSchema
):

    db = SessionLocal()

    leave = models.Leave(

        employee_id=leave_data.employee_id,

        leave_type=leave_data.leave_type,

        start_date=leave_data.start_date,

        end_date=leave_data.end_date,

        reason=leave_data.reason
    )

    db.add(leave)

    db.commit()

    return {
        "message": "Leave applied successfully"
    }


@router.get("/all")

def get_all_leaves():

    db = SessionLocal()

    return db.query(
        models.Leave
    ).all()


@router.put("/approve/{leave_id}")

def approve_leave(leave_id: int):

    db = SessionLocal()

    leave = db.query(
        models.Leave
    ).filter(
        models.Leave.id == leave_id
    ).first()

    leave.status = "Approved"

    db.commit()

    return {
        "message": "Leave Approved"
    }


@router.put("/reject/{leave_id}")

def reject_leave(leave_id: int):

    db = SessionLocal()

    leave = db.query(
        models.Leave
    ).filter(
        models.Leave.id == leave_id
    ).first()

    leave.status = "Rejected"

    db.commit()

    return {
        "message": "Leave Rejected"
    }
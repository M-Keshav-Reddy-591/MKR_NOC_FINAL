
from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database import get_db

from models import Notification

router = APIRouter(
    prefix="/api/v1/notifications",
    tags=["Notifications"]
)


# =====================================================
# GET EMPLOYEE NOTIFICATIONS
# =====================================================

@router.get("/{employee_id}")
def get_notifications(
    employee_id: str,
    db: Session = Depends(get_db)
):

    notifications = db.query(
        Notification
    ).filter(
        Notification.employee_id == employee_id
    ).order_by(
        Notification.id.desc()
    ).all()

    result = []

    for item in notifications:

        result.append({

            "title": item.title,

            "message": item.message,

            "created_at": str(
                item.created_at
            )

        })

    return result


# =====================================================
# GET ADMIN NOTIFICATIONS
# =====================================================

@router.get("/admin/all")
def admin_notifications(
    db: Session = Depends(get_db)
):

    notifications = db.query(
        Notification
    ).filter(
        Notification.employee_id == "ADMIN"
    ).order_by(
        Notification.id.desc()
    ).all()

    result = []

    for item in notifications:

        result.append({

            "title": item.title,

            "message": item.message,

            "created_at": str(
                item.created_at
            )

        })

    return result


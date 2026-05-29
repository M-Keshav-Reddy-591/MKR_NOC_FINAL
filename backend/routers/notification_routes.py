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
# ADMIN NOTIFICATIONS
# =====================================================

@router.get("/admin/all")
def admin_notifications(
    db: Session = Depends(get_db)
):

    notifications = db.query(
        Notification
    ).order_by(
        Notification.id.desc()
    ).all()

    result = []

    for n in notifications:

        result.append({

            "employee_id": n.employee_id,

            "title": n.title,

            "message": n.message,

            "created_at": str(
                n.created_at
            ) if n.created_at else ""

        })

    return result

# =====================================================
# EMPLOYEE NOTIFICATIONS
# =====================================================

# @router.get("/{employee_id}")
# def employee_notifications(
#     employee_id: str,
#     db: Session = Depends(get_db)
# ):

#     notifications = db.query(
#         Notification
#     ).filter(

#         Notification.employee_id ==
#         employee_id

#     ).order_by(
#         Notification.id.desc()
#     ).all()

#     result = []

#     for n in notifications:

#         result.append({

#             "title": n.title,

#             "message": n.message,

#             "created_at": str(
#                 n.created_at
#             ) if n.created_at else "",

#             "is_read": n.is_read

#         })

#     return result


@router.get("/{employee_id}")
def employee_notifications(
    employee_id: str,
    db: Session = Depends(get_db)
):

    notifications = db.query(
        Notification
    ).filter(

        Notification.employee_id ==
        employee_id

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
            ) if item.created_at else "",

            "is_read": item.is_read
        })

    return result





# # =====================================================
# # ADMIN NOTIFICATIONS
# # =====================================================

# @router.get("/admin/all")
# def admin_notifications(
#     db: Session = Depends(get_db)
# ):

#     notifications = db.query(
#         Notification
#     ).order_by(
#         Notification.id.desc()
#     ).all()

#     result = []

#     for item in notifications:

#         result.append({

#             "employee_id": item.employee_id,

#             "title": item.title,

#             "message": item.message,

#             "created_at": str(
#                 item.created_at
#             ) if item.created_at else "",

#             "is_read": item.is_read
#         })

#     return result


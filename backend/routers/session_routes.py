from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from database import get_db

from models import BrowserSession

router = APIRouter(
    prefix="/api/v1/sessions",
    tags=["Browser Sessions"]
)


@router.get("/")
def get_sessions(
    db: Session = Depends(get_db)
):

    sessions = db.query(
        BrowserSession
    ).order_by(
        BrowserSession.login_time.desc()
    ).all()

    result = []

    for row in sessions:

        result.append({

            "employee_id":
            row.employee_id,

            "employee_name":
            row.employee_name,

            "ip_address":
            row.ip_address,

            "browser":
            row.browser_info,

            "login_time":
            str(row.login_time)

        })

    return result
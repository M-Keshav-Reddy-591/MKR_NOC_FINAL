from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request
)
from datetime import datetime
from sqlalchemy.orm import Session
from database import get_db
from models import (
    Employee,
    PasswordLog,
    Notification,
    BrowserSession
)
from utils.security import (
    hash_password,
    verify_password
)

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


# =========================================================
# REGISTER
# =========================================================

@router.post("/register")
def register_user(
    data: dict,
    db: Session = Depends(get_db)
):

    existing_user = db.query(
        Employee
    ).filter(
        Employee.emp_id == data.get("emp_id")
    ).first()

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Employee ID already exists"
        )

    hashed_password = hash_password(
        data.get("password")
    )

    new_user = Employee(

        emp_id=data.get("emp_id"),

        emp_name=data.get("emp_name"),

        department=data.get("department"),

        designation=data.get("designation"),

        phone_number=data.get("phone_number"),

        email=data.get("email"),

        role=data.get("role"),

        password=hashed_password
    )



    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "Employee Registered Successfully"
    }


# # =========================================================
# # LOGIN
# # =========================================================

# @router.post("/login")
# def login(
#     request: Request,
#     data: dict,
#     db: Session = Depends(get_db)
# ):

#     user = db.query(
#         Employee
#     ).filter(
#         Employee.emp_id == data["emp_id"]
#     ).first()

#     if not user:

#         raise HTTPException(
#             status_code=404,
#             detail="Employee not found"
#         )

#     if not verify_password(
#         data["password"],
#         user.password
#     ):

#         raise HTTPException(
#             status_code=401,
#             detail="Invalid password"
#         )

#     if user.role.lower() != data["role"].lower():

#         raise HTTPException(
#             status_code=401,
#             detail="Invalid role"
#         )
@router.post("/login")
def login(

    request: Request,

    data: dict,

    db: Session = Depends(get_db)

):

    user = db.query(
        Employee
    ).filter(
        Employee.emp_id == data["emp_id"]
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    if not verify_password(
        data["password"],
        user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    if user.role.lower() != data["role"].lower():

        raise HTTPException(
            status_code=401,
            detail="Invalid role"
        )

    user_agent = request.headers.get(
        "user-agent",
        "Unknown"
    )

    # Browser

    browser = "Unknown"

    if "Chrome" in user_agent:

        browser = "Chrome"

    elif "Firefox" in user_agent:

        browser = "Firefox"

    elif "Edge" in user_agent:

        browser = "Edge"

    # OS

    operating_system = "Unknown"

    if "Windows" in user_agent:

        operating_system = "Windows"

    elif "Linux" in user_agent:

        operating_system = "Linux"

    elif "Android" in user_agent:

        operating_system = "Android"

    # Device

    if "Mobile" in user_agent:

        device_type = "Mobile"

    else:

        device_type = "Desktop"

    session = BrowserSession(

        employee_id=user.emp_id,

        employee_name=user.emp_name,

        ip_address=ip_address,

        browser_info=browser,

        operating_system=operating_system,

        device_type=device_type,

        screen_resolution=data.get(
            "screen_resolution",
            ""
        ),

        timezone=data.get(
            "timezone",
            ""
        ),

        login_time=datetime.now(),

        last_seen=datetime.now()

    )

    db.add(session)

    db.commit()

    return {

        "message": "Login successful",

        "employee": {

            "emp_id": user.emp_id,

            "name": user.emp_name,

            "role": user.role

        }

    }

    # # ============================================
    # # BROWSER SESSION
    # # ============================================

    # ip_address = data.get(
    #         "client_ip",
    #         request.client.host
    #     )

    # browser_info = data.get(
    #     "browser_info",
    #     "Unknown"
    # )

    # session = BrowserSession(

    #     employee_id=user.emp_id,

    #     employee_name=user.emp_name,

    #     ip_address=ip_address,

    #     browser_info=browser_info,

    #     login_time=datetime.now(),

    #     last_seen=datetime.now()

    # )

    # db.add(session)

    # db.commit()
    
    # return {

    #     "message": "Login successful",

    #     "employee": {

    #         "emp_id": user.emp_id,

    #         "name": user.emp_name,

    #         "role": user.role,


    #     }

    # }


# =========================================================
# CHANGE PASSWORD
# =========================================================

@router.post("/change-password")
def change_password(
    data: dict,
    db: Session = Depends(get_db)
):

    user = db.query(
        Employee
    ).filter(
        Employee.emp_id == data["employee_id"]
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    if not verify_password(
        data["old_password"],
        user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Old password incorrect"
        )

    user.password = hash_password(
        data["new_password"]
    )

    log = PasswordLog(

        employee_id=user.emp_id,

        employee_name=user.emp_name,

        changed_by="employee"

    )

    db.add(log)

    # =====================================================
    # ADMIN NOTIFICATION
    # =====================================================

    admin_notification = Notification(

        employee_id="ADMIN",

        title="Password Changed",

        message=f"{user.emp_name} changed account password"

    )

    db.add(admin_notification)

    # =====================================================
    # EMPLOYEE NOTIFICATION
    # =====================================================

    employee_notification = Notification(

        employee_id=user.emp_id,

        title="Password Changed",

        message="Your password was changed successfully"

    )

    db.add(employee_notification)

    db.commit()

    return {
        "message": "Password changed successfully"
    }


# =========================================================
# ADMIN RESET PASSWORD
# =========================================================

@router.post("/admin-reset-password")
def admin_reset_password(
    data: dict,
    db: Session = Depends(get_db)
):

    user = db.query(
        Employee
    ).filter(
        Employee.emp_id == data["emp_id"]
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    user.password = hash_password(
        data["new_password"]
    )

    log = PasswordLog(

        employee_id=user.emp_id,

        employee_name=user.emp_name,

        changed_by="admin"

    )

    db.add(log)

    employee_notification = Notification(

        employee_id=user.emp_id,

        title="Password Reset",

        message="Admin reset your password"

    )

    db.add(employee_notification)

    db.commit()

    return {
        "message": "Password reset successfully"
    }


# =========================================================
# PASSWORD LOGS
# =========================================================

@router.get("/password-logs")
def password_logs(
    db: Session = Depends(get_db)
):

    logs = db.query(
        PasswordLog
    ).order_by(
        PasswordLog.id.desc()
    ).all()

    result = []

    for log in logs:

        result.append({

            "employee_id": log.employee_id,

            "employee_name": log.employee_name,

            "changed_by": log.changed_by,

            "changed_at": str(
                log.changed_at
            )

        })

    return result




from datetime import datetime
from datetime import timedelta

from jose import JWTError
from jose import jwt

from passlib.context import CryptContext

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

import models

from database import SessionLocal


# ==========================================
# JWT CONFIG
# ==========================================

from core.config import SECRET_KEY
from core.config import ALGORITHM
from core.config import ACCESS_TOKEN_EXPIRE_MINUTES


# ==========================================
# PASSWORD HASHING
# ==========================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# ==========================================
# OAUTH2
# ==========================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


# ==========================================
# DATABASE
# ==========================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


from passlib.context import CryptContext


pwd_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"
)


# ==========================================
# HASH PASSWORD
# ==========================================

def hash_password(password: str):

    return pwd_context.hash(password)


# ==========================================
# VERIFY PASSWORD
# ==========================================

def verify_password(

    plain_password,

    hashed_password
):

    return pwd_context.verify(

        plain_password,

        hashed_password
    )


# ==========================================
# CREATE ACCESS TOKEN
# ==========================================

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# ==========================================
# GET CURRENT USER
# ==========================================

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={
            "WWW-Authenticate": "Bearer"
        }
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        emp_id: str = payload.get("sub")

        if emp_id is None:

            raise credentials_exception

    except JWTError:

        raise credentials_exception

    user = db.query(
        models.Employee
    ).filter(
        models.Employee.emp_id == emp_id
    ).first()

    if user is None:

        raise credentials_exception

    return user


# ==========================================
# ADMIN CHECK
# ==========================================

def admin_required(
    current_user: models.Employee = Depends(
        get_current_user
    )
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user


# ==========================================
# EMPLOYEE CHECK
# ==========================================

def employee_required(
    current_user: models.Employee = Depends(
        get_current_user
    )
):

    if current_user.role not in [
        "employee",
        "admin"
    ]:

        raise HTTPException(
            status_code=403,
            detail="Employee access required"
        )

    return current_user
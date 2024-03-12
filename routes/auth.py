from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from config.db import authentication_DB
from passlib.context import CryptContext
from datetime import datetime, timedelta
from models.todos import User
from typing import Optional


router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


SECRET_KEY = "9759423hihfgwiyt3yt347yy9ifn3y83y489yht8"  # Replace with a secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# function to get the user data from the authentication_DB.
def get_user(username: str):
    try:
        user_data = authentication_DB.find_one({"username": username})
        if user_data:
            return User(**user_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return None


# function to authenticate the user coming with their username and the password.
def authenticate_user(username: str, password: str):
    try:
        user = get_user(username)
        if user and verify_password(password, user.password):
            return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return False

# for creating the access token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    try:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# post method for logging for access token
@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        user = authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=401,
                detail="Incorrect username or password, Please enter correct username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
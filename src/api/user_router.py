from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.database import get_session
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService
from src.schemas.user_schemas import UserCreate, UserResponse, UserUpdate, UserLogin
from src.core.security import create_access_token, get_password_hash, verify_password
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/users", tags=["Users"])

def get_user_repository(db: Session = Depends(get_session)):
    return UserRepository(db)

def get_user_service(repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository)

@router.get("/", response_model=list[UserResponse])
def get_all_users(service: UserService = Depends(get_user_service)):
    return service.get_all_users()

@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    user_data = user.model_dump()
    user_data["password"] = get_password_hash(user_data["password"])
    return service.create_user(user_data)

@router.delete("/{user_id}")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    success = service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}

@router.patch("/{user_id}", response_model=UserResponse)
def update_user_data(user_id: int, user_data: UserUpdate, service: UserService = Depends(get_user_service)):
    if user_data.password:
        user_data.password = get_password_hash(user_data.password)
    return service.update_user(user_id, user_data)



@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), service: UserService = Depends(get_user_service)):
    db_user = service.get_user_by_email(form_data.username)
    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": str(db_user.id)})

    return {
        "access_token": token,
        "token_type": "bearer",
    }

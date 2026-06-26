from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.database import get_session
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService
from src.schemas.user_schemas import UserCreate, UserResponse, UserUpdate

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
    return service.create_user(user)

@router.delete("/{user_id}")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    success = service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}

@router.patch("/{user_id}")
def update_user_data(user_id: int, user_data: UserUpdate, service: UserService = Depends(get_user_service)):
    return service.update_user(user_id, user_data)

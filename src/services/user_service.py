from src.repositories.user_repository import UserRepository
from fastapi import HTTPException

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_all_users(self):
        return self.repository.get_all()

    def get_user_by_id(self, user_id: int):
        return self.repository.get_by_id(user_id)
    
    def get_user_by_email(self, user_id: int):
        return self.repository.get_by_email(user_id)

    def create_user(self, user_data: dict):
        return self.repository.create(user_data)

    def delete_user(self, user_id: int):
        return self.repository.delete(user_id)

    def update_user(self, user_id: int, user_data: dict):
        user = self.repository.get_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return self.repository.update(user, user_data)

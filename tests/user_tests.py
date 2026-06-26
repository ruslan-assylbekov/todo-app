from datetime import UTC, datetime
from unittest.mock import MagicMock

from fastapi.testclient import TestClient

from src.main import app
from src.api.user_router import get_user_service
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService


def make_user():
    return {
        "email": "ruslan@example.com",
        "firstname": "Ruslan",
        "lastname": "Assylbekov",
    }


def test_user_service_gets_user_from_repository():
    repository = MagicMock()
    repository.get_by_id.return_value = make_user()
    service = UserService(repository)

    result = service.get_user_by_id(1)

    repository.get_by_id.assert_called_once_with(1)
    assert result["firstname"] == "Ruslan"


def test_user_service_creates_user_through_repository():
    repository = MagicMock()
    user_data = {
        "email": "ruslan@example.com",
        "password": "pass",
        "firstname": "Ruslan",
        "lastname": "Assylbekov",
    }
    repository.create.return_value = make_user()
    service = UserService(repository)

    result = service.create_user(user_data)

    repository.create.assert_called_once_with(user_data)
    assert result["email"] == "ruslan@example.com"


def test_user_repository_create_uses_session_without_real_database():
    db = MagicMock()
    repo = UserRepository(db)
    user_data = {
        "email": "ruslan@example.com",
        "password": "pass",
        "firstname": "Ruslan",
        "lastname": "Assylbekov",
    }

    result = repo.create(user_data)

    db.add.assert_called_once_with(result)
    db.commit.assert_called_once()
    db.refresh.assert_called_once_with(result)
    assert result.firstname == "Ruslan"

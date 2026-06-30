import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException
from src.services.user_service import UserService
from src.schemas.user_schemas import UserUpdate


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


def test_user_service_updates_user_through_repository():
    repository = MagicMock()
    existing_user = MagicMock()
    update_data = UserUpdate(firstname="Updated")

    repository.get_by_id.return_value = existing_user
    repository.update.return_value = existing_user

    service = UserService(repository)

    result = service.update_user(1, update_data)

    repository.get_by_id.assert_called_once_with(1)
    repository.update.assert_called_once_with(existing_user, {"firstname": "Updated"})
    assert result == existing_user


def test_user_service_update_raises_404_when_user_not_found():
    repository = MagicMock()
    repository.get_by_id.return_value = None

    service = UserService(repository)

    with pytest.raises(HTTPException) as exc_info:
        service.update_user(999, UserUpdate(firstname="Updated"))

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "User not found"
    repository.update.assert_not_called()
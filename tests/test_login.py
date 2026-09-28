import pytest
import requests
from data import INVALID_LOGIN_DATA, AUTH_LOGIN
import allure
from constants import (
    TWO_HUNDRED,
    FOUR_HUNDRED_ONE,
    ERROR_TEXT 
)


@allure.title("Логин пользователя")
class TestLogin:

    @allure.title("вход под существующим пользователем")
    def test_login_existing_user(self, new_user):
        response = requests.post(
            AUTH_LOGIN,
            json={"email": new_user["email"], "password": new_user["password"]}
        )
        assert response.status_code == TWO_HUNDRED
        assert response.json()["success"] is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()
        assert response.json()["user"]["email"] == new_user["email"]

    @allure.title("вход с неверным логином и паролем")
    @pytest.mark.parametrize("credentials", INVALID_LOGIN_DATA)
    def test_login_invalid_credentials(self, credentials):
        response = requests.post(
            AUTH_LOGIN,
            json=credentials
        )
        assert response.status_code == FOUR_HUNDRED_ONE
        assert response.json()["success"] is False
        assert response.json()["message"] == ERROR_TEXT 
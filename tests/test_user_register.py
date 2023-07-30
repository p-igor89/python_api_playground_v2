from datetime import datetime

import allure
import requests

from src.assertions import Assertions
from src.base_case import BaseCase


@allure.epic("User registration cases")
class TestUserRegister(BaseCase):

    @allure.description("This test successfully create user")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("This test create user with existing email")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email=email)

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_status_code(response, 400)

        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected content {response.content}"

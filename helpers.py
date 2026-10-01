import random
import string
import allure
from data import BASE_URL, DEFAULT_EMAIL, DEFAULT_PASSWORD


@allure.title("Генерируем случайную строку")
def random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

@allure.title("Генерируем случайны email")
def random_email():
    return f"{random_string()}@{DEFAULT_EMAIL.split('@')[1]}" 
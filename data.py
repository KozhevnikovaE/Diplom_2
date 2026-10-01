MISSING_FIELDS_DATA = [
    {"email": "", "password": "password123", "name": "test"},
    {"email": "test@yandex.ru", "password": "", "name": "test"},
    {"email": "test@yandex.ru", "password": "password123", "name": ""},
    {"email": "test@yandex.ru", "password": "password123"},
    {"email": "test@yandex.ru", "name": "test"},
    {"password": "password123", "name": "test"},
]

INVALID_LOGIN_DATA = [
    {"email": "wrong@example.com", "password": "password123"},
    {"email": "test@yandex.ru", "password": "wrongpassword"},
    {"email": "wrong@example.com", "password": "wrongpassword"},
]

TEST_PASSWORD = "password123"

TEST_EMAIL = "jane@mail.ru"

INVALID_INGREDIENT_HASH = "невалидный_хеш"


BASE_URL = "https://stellarburgers.education-services.ru/api"
DEFAULT_EMAIL = "test@example.com" 
DEFAULT_PASSWORD = "testpassword123"

AUTH_REGISTER = f"{BASE_URL}/auth/register"
AUTH_LOGIN = f"{BASE_URL}/auth/login"
ORDERS_CREATE = f"{BASE_URL}/orders"

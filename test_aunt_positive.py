import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Фикстура для инициализации и закрытия драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=226bce07-3bd5-42cb-a720-08ac6683331a&theme=light&auth_type")
    yield driver
    driver.quit()

def test_login(driver):
    time.sleep(4)  # Ожидаем загрузку страницы авторизации

    # Ввод логина
    login_input = driver.find_element(By.ID, "username")
    login_input.send_keys("sergun2099@gmail.com")

    # Ввод пароля
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("Testersega2099")

    # Нажатие на кнопку входа
    login_button = driver.find_element(By.ID, "kc-login")
    login_button.click()

    time.sleep(2)  # Ожидаем реакцию системы на авторизацию

    # Проверяем отсутствие сообщений об ошибке
    error_messages = driver.find_elements(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]')

    assert len(error_messages) == 0
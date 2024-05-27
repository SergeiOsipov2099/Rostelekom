import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Fixture for initializing and closing the driver.
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=226bce07-3bd5-42cb-a720-08ac6683331a&theme=light&auth_type")
    yield driver
    driver.quit()

def test_login_failure(driver):
    time.sleep(4)  # Waiting for the login page to load.
    # Entering login
    login_input = driver.find_element(By.ID, "username")
    login_input.send_keys("sergun2099@gmail.com")

    # Entering an incorrect password.
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("WrongPassword123")

    #Clicking on the login button.
    login_button = driver.find_element(By.ID, "kc-login")
    login_button.click()

    time.sleep(2)  # Waiting for the system's response to the login attempt.
    # Checking for error messages
    error_messages = driver.find_elements(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]')

    assert len(error_messages) > 0, "Authorization error was not detected"

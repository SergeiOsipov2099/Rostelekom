import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=8d996248-fb36-4f95-97bc-4d02d24f033a&theme&auth_type")  # Replace URL with the actual one
    yield driver
    driver.quit()

@pytest.mark.parametrize("test_name", [
    "A",  # One Latin character
    "Б",  # One Cyrillic character
    "1",  # One digit
    "@" * 31,  # String of special characters exceeding the maximum length
    "Тест123",  # Mix of letters and digits
    "Тест-Тест-Тест",  # String with dashes
    "VeryLongName" * 10  # String exceeding the maximum length
])
def test_name_input_validation_negative(driver, test_name):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kc-register"]'))).click()

    name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]'))
    )
    name_input.send_keys(test_name)

    # Clicking on the next field after entering the name
    next_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]'))
    )
    next_input.click()

    # Checking for the presence of an error message
    error_message = driver.find_elements(By.XPATH,
                                         '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')

    assert len(error_message) > 0, f"Error message did not appear for invalid name '{test_name}'"

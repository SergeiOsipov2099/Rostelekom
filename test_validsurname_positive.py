import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=8d996248-fb36-4f95-97bc-4d02d24f033a&theme&auth_type ")  # Replace URL with the actual one
    yield driver
    driver.quit()

@pytest.mark.parametrize("test_name", [
    "Aa",  # Minimum allowed length
    "Abc",  # Boundary values
    "B" * 30,  # Maximum allowed length
    "B" * 29,  # Boundary values
    "KkLlMmNn",  # Name of 8 letters
    "HhJjKkLlMm",  # Name of 10 letters
    "XxYyZz",  # Name of rarely used letters
    "Gg" + "H" * 27 + "Ii",  # Name of repeating and unique letters
])
def test_name_input_validation(driver, test_name):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kc-register"]'))).click()

    sourname_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]'))
    )
    sourname_input.send_keys(test_name)

    # Clicking on the next field after entering the name
    next_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]'))
    )
    next_input.click()

    # Checking for error message
    is_valid_length = 2 <= len(test_name) <= 30
    error_message = driver.find_elements(By.XPATH,
                                         '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]')

    if is_valid_length:
        assert len(error_message) == 0, f"Error message appeared for name '{test_name}'"
    else:
        assert len(error_message) > 0, f"Error message did not appear for invalid name '{test_name}'"

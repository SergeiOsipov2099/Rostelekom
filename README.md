# Rostelekom
Rostelekom_autotests
# Testing a webpage on the site b2c.passport.rt.ru

This repository contains a set of automated tests to verify the functionality of the login webpage and user data validation during registration on the site b2c.passport.rt.ru.

## Description of tests

- `test_aunt_positive.py`: Checks the process of successful user login with correct credentials.
- `test_aunt_negative.py`: Checks the handling of incorrect login attempts, expecting an error message to appear.
- `test_validname_positive.py`: Checks the validation of the username input with correct data.
- `test_validname_negative.py`: Checks the validation of the username input with incorrect data, expecting an error message to appear.
- `test_validsurname_positive.py`: Checks the validation of the user's surname input with correct data.
- `test_validsurname_negative.py`: Checks the validation of the user's surname input with incorrect data, expecting an error message to appear.

## Installation and configuration

To run the tests, you will need:

Python 3
Selenium library
WebDriver for the browser you plan to use
Make sure the WebDriver is in your system's PATH or specify the path to it directly in the tests.

Running Tests
To run all tests, execute the following command in the terminal:
pytest path_to_tests/



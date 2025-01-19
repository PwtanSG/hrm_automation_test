# Introduction
Web functional automation test using Selenium WebDriver with Python

## Testcases
/testcases/test_login.py
### test_can_login_logout
Test user can login successfully with valid credential  \
Test user can logout successfully from avatar dropdown logout 

### test_no_username_input_login 
Test user unable to login successfully without username  \
Validate validation message

### test_no_password_input_login
Test user unable to login successfully without password  \
Validate validation message

### test_no_inputs_login
Test user unable to login successfully without username and password  \
Validate validation message

### test_invalid_credential_login
Test user unable to login successfully with invalid credential  \
Validate error message

## script usage
pytest -v testcases/test_login.py

## Demo video
[https://www.youtube.com/watch?v=XtnMgxRbjAc]

### reference
https://docs.pytest.org/en/stable/contents.html \
https://selenium-python.readthedocs.io/ \
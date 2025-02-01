# Introduction
Web functional automation test using Selenium WebDriver with Python

## Testcases
/testcases/test_login.py
### test_can_login_logout
Test user can login successfully with valid credential  \
Test user can logout successfully from avatar dropdown logout 

### test_no_input_login_validation 
Test user unable to login successfully without username  \
Test user unable to login successfully without password  \
Test user unable to login successfully without username and password  \
Validate that validation error message(s) prompted

### test_invalid_credential_login
Test user unable to login successfully with invalid credential  \
Validate error message

### test_co_website_link
Test company website hyperlink \
Verify that browser open a tab that shows company website 

### test_forget_password_link
Test "forget password" link \
Verify that page redirect to reset password request page \

/testcases/test_login.py
### test_main_menu_search_clear
Test and check search menu functionalities \

### test_main_menu_list
Test and check all menu exist on menu list \ 

### test_main_menu_items
Test click each of the menu item and check the corresponding landing page

## script usage
pytest -v testcases/test_login.py \
pytest -v -s -k test_invalid_credential_login \
pytest -v testcases/test_main_menu.py \


## Demo video
[https://www.youtube.com/watch?v=XtnMgxRbjAc]

### reference
https://docs.pytest.org/en/stable/contents.html \
https://selenium-python.readthedocs.io/ \
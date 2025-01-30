import os
import time
import pytest
from pages.login_page import LoginPage
from dotenv import load_dotenv

login_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
auth_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
reset_password_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode"
co_website_url = "https://www.orangehrm.com/"
co_website_title = "Human Resources Management Software | OrangeHRM"
reset_password_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset"
password_reset_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode"
load_dotenv()
valid_username = os.getenv('VALID_USERNAME')
valid_password = os.getenv('VALID_PASSWORD')
invalid_username = "admin1"
invalid_password = "abc1234"


def test_can_login_logout(chrome_driver):
    # Log in test
    login_page = LoginPage(chrome_driver)
    # Log in
    login_page.login_application(login_page_url, valid_username, valid_password)
    # assert page redirect to Admin page after login
    login_success = login_page.assert_url(auth_page_url)
    login_page.page_scroll()

    # Log out test
    login_page.click_user_profile_icon()
    # verify successful logout clicking logout link from user profile dropdown menu
    select_menu_logout = login_page.select_user_profile_dropdown_menu("Logout")
    logout_success = login_page.assert_url(login_page_url)

    # assert test results
    assert login_success and logout_success and select_menu_logout


@pytest.mark.parametrize("test_label_, username_, password_, no_of_validation_msg_, validation_msg_",
                         [("no username login", "", valid_password, 1, "Required"),
                          ("no password login", valid_username, "", 1, "Required"),
                          ("no username/password login", "", "", 2, "Required")])
def test_no_input_login_validation(chrome_driver, test_label_, username_, password_, no_of_validation_msg_,
                                   validation_msg_):
    login_page = LoginPage(chrome_driver)
    # login without either username or password or without both inputs
    login_page.login_application(login_page_url, username_, password_)
    # check for validation error
    validation_errors = login_page.wait_find_tag_elements_xpath_by_text('span', validation_msg_)
    time.sleep(2)
    # check login is unsuccessful abd page remain in login page
    assert login_page.assert_url(login_page_url) and len(validation_errors) == no_of_validation_msg_


@pytest.mark.parametrize("test_label_, username_, password_", [("Wrong password", valid_username, invalid_password),
                                                               ("Wrong username", invalid_username, valid_password)])
def test_invalid_credential_login(chrome_driver, test_label_, username_, password_):
    login_page = LoginPage(chrome_driver)
    # login with invalid credentials
    login_page.login_application(login_page_url, username_, password_)
    # check for validation error
    assert_validation_error = login_page.find_error_invalid_credentials()
    time.sleep(2)
    login_page.take_screenshot()
    # check login is unsuccessful abd page remain in login page
    assert login_page.assert_url(login_page_url) and assert_validation_error


def test_co_website_link(chrome_driver):
    login_page = LoginPage(chrome_driver)
    # navigate to login page
    login_page.open_page(login_page_url)
    # find company website link and click
    link_element = login_page.get_co_website_link()
    link_element.click()
    # switch to the child page
    time.sleep(2)
    login_page.switch_to_child_browser_window()
    time.sleep(2)
    # assert test result
    co_website_success = login_page.assert_url(co_website_url)
    title_check = login_page.wait_for_title_is(co_website_title)
    assert co_website_success and title_check


def test_forget_password_link(chrome_driver):
    login_page = LoginPage(chrome_driver)
    # navigate to login page
    login_page.open_page(login_page_url)
    # find forget password link and click
    test_forget_password_link_element = login_page.get_forget_password_link()
    test_forget_password_link_element.click()
    time.sleep(2)
    # assert test result
    assert login_page.assert_url(password_reset_url)

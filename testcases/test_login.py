import time
import pytest
from pages.login_page import LoginPage

login_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
auth_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
reset_password_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode"
co_website_url = "https://www.orangehrm.com/"
co_website_title = "Human Resources Management Software | OrangeHRM"
# https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset


def test_can_login_logout(chrome_driver):
    # Log out test
    login_page = LoginPage(chrome_driver)
    # open browser and go to login page
    login_page.open_page(login_page_url)
    # fill in username and password
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    # click login button
    login_page.click_login()
    # check url after login
    login_success = login_page.assert_url(auth_page_url)
    login_page.page_scroll()

    # Log out test
    # verify successful logout clicking logout link from user profile dropdown menu
    login_page.click_user_profile_icon()
    select_menu_logout = login_page.select_user_profile_dropdown_menu("Logout")
    logout_success = login_page.assert_url(login_page_url)

    # assert test results
    assert login_success and logout_success and select_menu_logout


@pytest.mark.parametrize("test_label_, username_, password_, no_of_validation_msg_, validation_msg_",
                         [("no username login", "", "admin123", 1, "Required"), ("no password login", "Admin", "", 1, "Required"),
                          ("no username/password login", "", "", 2, "Required")])
def test_no_input_login_validation(chrome_driver, test_label_, username_, password_, no_of_validation_msg_,
                                   validation_msg_):
    login_page = LoginPage(chrome_driver)
    # go to login page
    login_page.open_page(login_page_url)
    # login without either username or password or without both inputs
    login_page.enter_username(username_)
    login_page.enter_password(password_)
    # click login
    login_page.click_login()
    # check for validation error
    validation_errors = login_page.wait_find_tag_elements_xpath_by_text('span', validation_msg_)
    time.sleep(2)
    # check login is unsuccessful abd page remain in login page
    assert login_page.assert_url(login_page_url) and len(validation_errors) == no_of_validation_msg_


def test_invalid_credential_login(chrome_driver):
    login_page = LoginPage(chrome_driver)
    # go to login page
    login_page.open_page(login_page_url)
    # input invalid login credentials
    login_page.enter_username("Admin")
    login_page.enter_password("admin1234")
    # click login button
    login_page.click_login()
    # check for validation error
    validation_error = login_page.find_error_invalid_credentials()
    time.sleep(2)
    # check login is unsuccessful abd page remain in login page
    assert login_page.assert_url(login_page_url) and validation_error


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
    co_website_success = login_page.assert_url(co_website_url)
    title_check = login_page.wait_for_title_is(co_website_title)
    assert co_website_success and title_check


# def test_hyperlinks(chrome_driver):
#     login_page = LoginPage(chrome_driver)
#     login_page.open_page(login_page_url)
#     login_page.get_hyperlinks()

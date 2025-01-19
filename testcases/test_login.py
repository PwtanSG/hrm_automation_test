import time

from pages.login_page import LoginPage

login_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
auth_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"


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
    login_success = login_page.check_url(auth_page_url)
    login_page.page_scroll()

    # Log out test
    login_page.click_user_profile_icon()
    select_menu_logout = login_page.select_user_profile_dropdown_menu("Logout")
    logout_success = login_page.check_url(login_page_url)

    # assert test results
    assert login_success and logout_success and select_menu_logout


def test_no_username_inputs_login(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.open_page(login_page_url)
    login_page.enter_username("")
    login_page.enter_password("admin123")
    login_page.click_login()
    validation_errors = login_page.wait_find_tag_elements_xpath_by_text('span', 'Required')
    time.sleep(2)
    assert login_page.get_current_url() == login_page_url and len(validation_errors) == 1


def test_no_password_inputs_login(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.open_page(login_page_url)
    login_page.enter_username("Admin")
    login_page.enter_password("")
    login_page.click_login()
    validation_errors = login_page.wait_find_tag_elements_xpath_by_text('span', 'Required')
    time.sleep(2)
    assert login_page.get_current_url() == login_page_url and len(validation_errors) == 1


def test_no_inputs_login(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.open_page(login_page_url)
    login_page.enter_username("")
    login_page.enter_password("")
    login_page.click_login()
    validation_errors = login_page.wait_find_tag_elements_xpath_by_text('span', 'Required')
    time.sleep(2)
    assert login_page.get_current_url() == login_page_url and len(validation_errors) == 2


def test_invalid_credential_login(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.open_page(login_page_url)
    # time.sleep(2)
    login_page.enter_username("Admin")
    login_page.enter_password("admin1234")
    login_page.click_login()
    validation_error = login_page.find_error_invalid_credentials()
    time.sleep(2)
    assert login_page.get_current_url() == login_page_url and validation_error





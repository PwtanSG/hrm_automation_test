import time

from pages.login_page import LoginPage
from pages.main_menu_page import MainMenuPage
from pages.employee_list_page import EmployeePage


def test_goto_employee_list(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.login_application(login_page.login_page_url, login_page.valid_username, login_page.valid_password)
    main_menu_page = MainMenuPage(chrome_driver)
    main_menu_page.goto_menu_item("PIM")
    employee_list_page = EmployeePage(chrome_driver)
    time.sleep(2)
    count_element = employee_list_page.get_count_element()
    print(count_element.text)
    employee_list_page.enter_name_input_box("ahmed")
    time.sleep(2)
    employee_list_page.click_search_button()
    time.sleep(2)
    count_element = employee_list_page.get_count_element()
    print(count_element.text)

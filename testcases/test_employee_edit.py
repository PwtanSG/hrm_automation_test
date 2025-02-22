import time

from pages.employee_edit_page import EmployeeEditPage
from pages.employee_list_page import EmployeeListPage
from pages.login_page import LoginPage
from pages.main_menu_page import MainMenuPage


def test_employee_record_edit(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.login_application(login_page.login_page_url, login_page.valid_username, login_page.valid_password)
    main_menu_page = MainMenuPage(chrome_driver)
    emp_lp = EmployeeListPage(chrome_driver)
    main_menu_page.goto_menu_item(emp_lp.main_menu_name_employee_page)
    emp_lp.click_top_nav_menu_item(emp_lp.top_nav_employee_list)
    test_emp_id = emp_lp.get_first_search_result_eid()
    if test_emp_id:
        emp_lp.click_edit_emp_button()
        time.sleep(3)
    time.sleep(3)
    emp_edit_page = EmployeeEditPage(chrome_driver)
    emp_edit_page.select_nationality("American")
    emp_edit_page.get_dob_calendar_elements()


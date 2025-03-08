import time

from pages.employee_edit_page import EmployeeEditPage
from pages.employee_list_page import EmployeeListPage
from pages.login_page import LoginPage
from pages.main_menu_page import MainMenuPage
from utilities.utils import Utils


def test_employee_record_edit(chrome_driver):
    test_data = {
        "Nationality": "American",
        "Gender": "Male",
        "Date of birth": ''
    }
    login_page = LoginPage(chrome_driver)
    login_page.login_application(login_page.login_page_url, login_page.valid_username, login_page.valid_password)
    main_menu_page = MainMenuPage(chrome_driver)
    emp_lp = EmployeeListPage(chrome_driver)
    main_menu_page.goto_menu_item(emp_lp.main_menu_name_employee_page)
    emp_lp.click_top_nav_menu_item(emp_lp.top_nav_employee_list)

    test_emp_id = emp_lp.get_first_search_result_eid()
    if test_emp_id:
        emp_lp.click_edit_emp_button()
        time.sleep(2)
    time.sleep(2)

    # select nationality
    emp_edit_page = EmployeeEditPage(chrome_driver)
    test_data['Nationality'] = emp_edit_page.change_nationality()
    emp_edit_page.select_nationality(test_data['Nationality'])

    # select dob field
    emp_edit_page.click_date_of_birth_field()
    emp_edit_page.click_dob_left_arrow(5)
    ut = Utils()
    test_data['Date of birth'] = emp_edit_page.click_dob_date(ut.get_today_date('day'))

    # toggle gender
    test_data['Gender'] = emp_edit_page.toggle_gender()

    # click save personal details
    emp_edit_page.click_save_personal_details()

    # retrieve edited record for verifications
    main_menu_page.goto_menu_item(emp_lp.main_menu_name_employee_page)
    results = emp_lp.search_by_employee_id(test_emp_id)
    time.sleep(3)
    if len(results) == 1:
        emp_lp.click_edit_emp_button()
        time.sleep(2)
        assert emp_edit_page.assert_edited_record(test_data)
    else:
        print(f'Record not found : {test_emp_id}')
        assert False

import time

from faker import Faker

from pages.employee_list_page import EmployeeListPage
from pages.employee_add_page import EmployeeAddPage
from pages.login_page import LoginPage
from pages.main_menu_page import MainMenuPage
from utilities.utils import Utils


def test_employee_add(chrome_driver):
    lp = LoginPage(chrome_driver)
    lp.login_application(lp.login_page_url, lp.valid_username, lp.valid_password)
    main_menu = MainMenuPage(chrome_driver)
    employee_lp = EmployeeListPage(chrome_driver)
    employee_add_page = EmployeeAddPage(chrome_driver)
    main_menu.goto_menu_item(main_menu.full_menu_items[1])
    employee_add_page.click_top_nav_menu_item(employee_add_page.top_nav_employee_add)

    fake = Faker()
    emp_first_name = fake.first_name()
    emp_middle_name = fake.first_name()
    emp_last_name = fake.last_name()
    employee_add_page.enter_first_name(emp_first_name)
    employee_add_page.enter_middle_name(emp_middle_name)
    employee_add_page.enter_last_name(emp_last_name)

    ut = Utils()
    gen_digits_4 = ut.gen_emp_id()
    eid = employee_add_page.get_employee_id_value()
    new_emp_id = eid + gen_digits_4
    # employee_add_page.clear_input_box(employee_add_page.employee_id)
    time.sleep(1)
    employee_add_page.enter_employee_id(gen_digits_4)
    time.sleep(1)

    # click save btn
    employee_add_page.click_save_button()
    time.sleep(2)

    # verify added record
    employee_add_page.click_top_nav_menu_item(employee_lp.top_nav_employee_list)
    employee_lp.search_by_employee_id(new_emp_id)
    employee_lp.click_search_button()
    time.sleep(2)
    result_list = employee_lp.get_all_search_results()
    new_rec_found = employee_lp.assert_search_result_by_id(result_list, new_emp_id, emp_first_name + ' ' +
                                                           emp_middle_name, emp_last_name)
    # remove added emp record
    if new_rec_found:
        employee_lp.delete_employee_record_by_id(new_emp_id)
    assert new_rec_found

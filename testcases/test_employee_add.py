import time

from pages.employee_list_page import EmployeeListPage
from pages.employee_add_page import EmployeeAddPage
from pages.login_page import LoginPage
from pages.main_menu_page import MainMenuPage


def test_employee_add(chrome_driver):
    lp = LoginPage(chrome_driver)
    lp.login_application(lp.login_page_url, lp.valid_username, lp.valid_password)
    main_menu = MainMenuPage(chrome_driver)
    employee_lp = EmployeeListPage(chrome_driver)
    employee_add_page = EmployeeAddPage(chrome_driver)
    main_menu.goto_menu_item(main_menu.full_menu_items[1])
    employee_add_page.click_top_nav_menu_item(employee_add_page.top_nav_employee_add)
    employee_add_page.enter_first_name('Donald')
    employee_add_page.enter_middle_name('J')
    employee_add_page.enter_last_name('Trumpet')
    new_eid = employee_add_page.get_employee_id_value()
    print(new_eid)
    employee_add_page.enter_employee_id('T')
    time.sleep(1)
    employee_add_page.click_save_button()
    time.sleep(3)
    employee_add_page.click_top_nav_menu_item(employee_lp.top_nav_employee_list)
    employee_lp.search_by_employee_id(new_eid + 'T')
    employee_lp.click_search_button()
    time.sleep(2)
    result_list = employee_lp.get_all_search_results()
    employee_lp.assert_search_result_by_id(result_list, new_eid + 'T', 'Donald J', 'Trumpet')



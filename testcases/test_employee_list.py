import time

import pytest

from pages.login_page import LoginPage
from pages.main_menu_page import MainMenuPage
from pages.employee_list_page import EmployeePage


def test_goto_employee_list(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.login_application(login_page.login_page_url, login_page.valid_username, login_page.valid_password)
    main_menu_page = MainMenuPage(chrome_driver)
    employee_list_page = EmployeePage(chrome_driver)
    main_menu_page.goto_menu_item(employee_list_page.main_menu_name_employee_page)
    time.sleep(2)
    count_element = employee_list_page.get_count_element()
    print(count_element.text)
    employee_list_page.click_top_nav_menu_item(employee_list_page.top_nav_menu_list[0])
    employee_list_page.assert_url(employee_list_page.employee_page_url)


@pytest.mark.parametrize("job_title_", ["HR Manager", "QA Engineer"])
def test_search_employee_list_by_job_title(chrome_driver, job_title_):
    login_page = LoginPage(chrome_driver)
    login_page.login_application(login_page.login_page_url, login_page.valid_username, login_page.valid_password)
    main_menu_page = MainMenuPage(chrome_driver)
    employee_list_page = EmployeePage(chrome_driver)
    main_menu_page.goto_menu_item(employee_list_page.main_menu_name_employee_page)
    employee_list_page.click_top_nav_menu_item(employee_list_page.top_nav_menu_list[0])
    time.sleep(2)
    results = employee_list_page.filter_by_dropdown_job_title(job_title_)
    # print(results)
    time.sleep(2)
    if not results:
        assert len(results) == employee_list_page.get_search_result_count()
    else:
        assert all(results) and len(results) == employee_list_page.get_search_result_count()


# def test_employee_list_search_by_name(chrome_driver):
#     login_page = LoginPage(chrome_driver)
#     login_page.login_application(login_page.login_page_url, login_page.valid_username, login_page.valid_password)
#     main_menu_page = MainMenuPage(chrome_driver)
#     employee_list_page = EmployeePage(chrome_driver)
#     main_menu_page.goto_menu_item(employee_list_page.main_menu_name_employee_page)
#     time.sleep(2)
#     count_element = employee_list_page.get_count_element()
#     print(count_element.text)
#     # employee_list_page.enter_name_input_box("ahmed")
#     # time.sleep(2)
#     # employee_list_page.click_search_button()
#     # time.sleep(2)
#     # count_element = employee_list_page.get_count_element()
#     # print(count_element.text)

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
    # count_element = employee_list_page.get_count_element()
    employee_list_page.click_top_nav_menu_item(employee_list_page.top_nav_employee_list)
    employee_list_page.assert_url(employee_list_page.employee_page_url)


@pytest.mark.parametrize("job_title_", ["HR Manager", "QA Lead"])
def test_search_employee_list_by_job_title(chrome_driver, job_title_):
    login_page = LoginPage(chrome_driver)
    login_page.login_application(login_page.login_page_url, login_page.valid_username, login_page.valid_password)
    main_menu_page = MainMenuPage(chrome_driver)
    employee_list_page = EmployeePage(chrome_driver)
    main_menu_page.goto_menu_item(employee_list_page.main_menu_name_employee_page)
    employee_list_page.click_top_nav_menu_item(employee_list_page.top_nav_employee_list)
    time.sleep(2)
    employee_list_page.filter_by_dropdown_job_title(job_title_)
    employee_list_page.click_search_button()
    time.sleep(2)
    search_results_list = employee_list_page.get_all_search_results()
    assert employee_list_page.assert_search_result_job_title(search_results_list, job_title_)


def test_employee_list_search_by_name(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.login_application(login_page.login_page_url, login_page.valid_username, login_page.valid_password)
    main_menu_page = MainMenuPage(chrome_driver)
    employee_list_page = EmployeePage(chrome_driver)
    main_menu_page.goto_menu_item(employee_list_page.main_menu_name_employee_page)
    search_name_text = employee_list_page.get_current_user_name('first_name')
    employee_list_page.enter_name_input_box(search_name_text)
    time.sleep(2)
    employee_list_page.click_search_button()
    time.sleep(2)
    search_results_list = employee_list_page.get_all_search_results()
    check_last_name_col = employee_list_page.assert_search_results_name(search_results_list, search_name_text)
    check_first_name_col = employee_list_page.assert_search_results_name(search_results_list, search_name_text)
    assert check_last_name_col or check_first_name_col

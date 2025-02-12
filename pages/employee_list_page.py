import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class EmployeePage(BaseDriver):
    # locators
    top_nav_bar_menu_items = (By.XPATH, "//a[@href='#']")
    input_textbox_elements = (By.XPATH, "//input[contains(@placeholder,'Type for hints')]")
    job_title_filter_menu = (By.XPATH, "//div[@role='listbox']")
    dropdown_elements_arrow = (By.XPATH, "//div[@class ='oxd-select-text--after']")
    search_button = (By.XPATH, "//button[@type='submit']")
    reset_button = (By.XPATH, "//button[@type='reset']")
    result_rows = (By.XPATH, "//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']")
    employee_found_count = (By.XPATH, "//div//span[@class='oxd-text oxd-text--span']")
    current_user_avatar = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    # toast_msg_element = (By.XPATH, "//div[@class='oxd-toast oxd-toast--info oxd-toast-container--toast']")
    # toast_msg_element = (By.XPATH, "//[@class='oxd-toast-start']")

    main_menu_name_employee_page = 'PIM'
    employee_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
    top_nav_employee_list = 'Employee List'

    def __init__(self, driver):
        BaseDriver.__init__(driver)
        self.driver = driver

    def click_top_nav_menu_item(self, menu_item_name_):
        # if menu_item_name_ not in self.top_nav_menu_list:
        #     return print('top nav menu item not found')
        menu_items = self.wait_for_presence_of_elements_located(self.top_nav_bar_menu_items)
        ut = Utils()
        menu_item = ut.find_element_by_text_from_list(menu_item_name_, menu_items)
        menu_item.click()
        time.sleep(3)

    def get_count_element(self):
        return self.wait_for_presence_of_element_located(self.employee_found_count)

    def get_search_result_count(self):
        count = 0
        search_count_element = self.wait_for_presence_of_element_located(self.employee_found_count)
        search_result = search_count_element.text
        if search_result == 'No Records Found':
            return 0
        else:
            return int(search_result[1])

    def enter_name_input_box(self, text_):
        elements = self.wait_for_presence_of_elements_located(self.input_textbox_elements)
        elements[0].send_keys(text_)

    def get_dropdown_element(self, value_):
        # 0 Employment Status, 1 include, 2 Job Title, 3 Sub Unit
        elements = self.wait_for_presence_of_elements_located(self.dropdown_elements_arrow)
        return elements[value_]

    def filter_by_dropdown_job_title(self, job_title_):
        job_title_filter = self.get_dropdown_element(2)
        job_title_filter.click()
        filter_menu = self.wait_for_presence_of_element_located(self.job_title_filter_menu)
        filter_menu_items = filter_menu.find_elements(By.XPATH, '*')
        for menu_item in filter_menu_items:
            if menu_item.text == job_title_:
                menu_item.click()
                break
        self.click_search_button()
        result_rows = self.wait_for_presence_of_elements_located(self.result_rows)
        return result_rows

    def assert_search_result_job_title(self, result_rows, job_title_):
        # 0 Employment Status, 1 include, 2 Job Title, 3 Sub Unit
        results = []
        for row in result_rows:
            column_elements = row.find_elements(By.XPATH, '*')
            if column_elements[4].text == job_title_:
                results.append(True)
                # print(column_elements[1].text + ' ' + column_elements[2].text + ' : ' + column_elements[4].text)
            else:
                print(column_elements[1].text + ' ' + column_elements[2].text + ' : ' + column_elements[4].text +
                      ' incorrect job title')
                results.append(False)

        if not result_rows:
            return len(result_rows) == self.get_search_result_count()
        else:
            return all(result_rows) and len(result_rows) == self.get_search_result_count()

    def get_current_user_name(self):
        avatar_element = self.wait_for_presence_of_element_located(self.current_user_avatar)
        return avatar_element.text

    def click_search_button(self):
        self.wait_for_element_to_be_clickable(self.search_button)

    def toast_message(self):
        toast_element = self.wait_for_presence_of_element_located(self.toast_msg_element)
        print(toast_element)


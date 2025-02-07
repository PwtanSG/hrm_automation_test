from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class EmployeePage(BaseDriver):
    # locators
    employee_found_count = (By.XPATH, "//div//span[@class='oxd-text oxd-text--span']")
    search_button = (By.XPATH, "//button[@type='submit']")
    reset_button = (By.XPATH, "//button[@type='reset']")
    dropdown_elements_arrow = (By.XPATH, "//div[@class ='oxd-select-text--after']")
    job_title_filter_menu = (By.XPATH, "//div[@role='listbox']")
    input_textbox_elements = (By.XPATH, "//input[contains(@placeholder,'Type for hints')]")
    result_rows = (By.XPATH, "//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']")

    main_menu_name_employee_page = 'PIM'
    employee_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"

    def __init__(self, driver):
        BaseDriver.__init__(driver)
        self.driver = driver

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
        # 0 Employment Status, 1 include, 2 Job Title, 3 Sub Unit
        results = []
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
        for row in result_rows:
            column_elements = row.find_elements(By.XPATH, '*')
            if column_elements[4].text == job_title_:
                results.append(True)
                # print(column_elements[1].text + ' ' + column_elements[2].text + ' : ' + column_elements[4].text)
            else:
                print(column_elements[1].text + ' ' + column_elements[2].text + ' : ' + column_elements[4].text +
                      ' incorrect job title')
                results.append(False)
        return results

    def click_search_button(self):
        self.wait_for_element_to_be_clickable(self.search_button)

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class EmployeePage(BaseDriver):
    # locators
    employee_found_count = (By.XPATH, "//div//span[@class='oxd-text oxd-text--span']")
    search_button = (By.XPATH, "//button[@type='submit']")
    reset_button = (By.XPATH, "//button[@type='reset']")
    dropdown_elements_arrow = (By.XPATH, "oxd-select-text--after")
    input_textbox_elements = (By.XPATH, "//input[contains(@placeholder,'Type for hints')]")

    def __init__(self, driver):
        BaseDriver.__init__(driver)
        self.driver = driver

    def get_count_element(self):
        return self.wait_for_presence_of_element_located(self.employee_found_count)

    def enter_name_input_box(self, text_):
        elements = self.wait_for_presence_of_elements_located(self.input_textbox_elements)
        elements[0].send_keys(text_)

    def click_search_button(self):
        self.wait_for_element_to_be_clickable(self.search_button)

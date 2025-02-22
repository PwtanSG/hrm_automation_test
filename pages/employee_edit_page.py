import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class EmployeeEditPage(BaseDriver):

    # locator
    nationality_dropdown = (By.XPATH, "(//div[@class='oxd-select-text--after'])[1]")
    dropdown_elements_arrow = (By.XPATH, "//div[@class='oxd-select-text--after']")
    nationality_menu = (By.XPATH, "//div[@role='listbox']")
    license_expiry_date_label = (By.XPATH, "//label[text()='License Expiry Date']")
    date_of_birth_dropdown = (By.XPATH, "(//div[@class='oxd-date-input'])[2]")
    dob_calendar_elements = (By.XPATH, "//div[@class='oxd-date-input-calendar']")
    gender_male = (By.XPATH, "//label[text()='Female']")

    def __init__(self, driver):
        BaseDriver.__init__(driver)
        self.driver = driver

    def get_dropdown_element(self, element_label_):
        # [0] 1.nationality, [1] 2.Marital status, [2] 3.blood type
        labels = ['Nationality', 'Marital Status', 'Blood Type']
        elements = self.wait_for_presence_of_elements_located(self.dropdown_elements_arrow)
        return elements[labels.index(element_label_)]

    def select_by_dropdown(self, element_label_, item_label_text_):
        selected_dropdown_ele = self.get_dropdown_element(element_label_)
        select = self.wait_for_presence_of_element_located(self.nationality_dropdown)
        select.click()
        time.sleep(1)
        dropdown_menu = self.wait_for_presence_of_element_located(self.nationality_menu)
        menu_items = dropdown_menu.find_elements(By.XPATH, '*')
        for menu_item in menu_items:
            if menu_item.text == item_label_text_:
                menu_item.click()
                break

    def select_nationality(self, nationality_):
        self.scroll_to_element(self.license_expiry_date_label)
        time.sleep(3)
        self.select_by_dropdown("Nationality", nationality_)
        time.sleep(3)

    def click_date_of_birth_field(self):
        element = self.wait_for_presence_of_element_located(self.date_of_birth_dropdown)
        print(type(element))
        element.click()
        time.sleep(2)

    def get_dob_calendar_elements(self):
        self.click_date_of_birth_field()
        elements = self.wait_for_presence_of_elements_located(self.dob_calendar_elements)
        print(len(elements))
        time.sleep(2)

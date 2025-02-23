import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class EmployeeEditPage(BaseDriver):

    # locator
    nationality_dropdown = (By.XPATH, "(//div[@class='oxd-select-text--after'])[1]")
    dropdown_elements_arrow = (By.XPATH, "//div[@class='oxd-select-text--after']")
    nationality_menu = (By.XPATH, "//div[@role='listbox']")
    license_expiry_date_label = (By.XPATH, "//label[text()='License Expiry Date']")
    date_of_birth_dropdown = (By.XPATH, "(//div[@class='oxd-date-input'])[2]")
    dob_calendar_elements = (By.XPATH, "//div[@class='oxd-date-input-calendar']")
    dob_selected_yyyy_dd_mm = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")
    calendar_date_element = (
        By.XPATH, "//div[contains(@class, 'oxd-calendar-date-wrapper')]//div[contains(@class, 'oxd-calendar-date')]")
    calendar_left_arrow = (
        By.XPATH, "//div[@class='oxd-calendar-header']//button//i[@class='oxd-icon bi-chevron-left']")
    gender_male = (By.CSS_SELECTOR, "input[type='radio'][value='1']")
    gender_female = (By.XPATH, ".//input[@value='2']")
    gender_elements = (By.XPATH, "//input[@type='radio']")
    personal_details_save_btn = (By.XPATH, "(//button[@type='submit'])[1]")

    def __init__(self, driver):
        BaseDriver.__init__(driver)
        self.driver = driver

    def get_dropdown_element(self, element_label_):
        # [0] 1.nationality, [1] 2.Marital status, [2] 3.blood type
        labels = ['Nationality', 'Marital Status', 'Blood Type']
        elements = self.wait_for_presence_of_elements_located(self.dropdown_elements_arrow)
        return elements[labels.index(element_label_)]

    def select_by_dropdown(self, element_label_, item_label_text_):
        self.get_dropdown_element(element_label_)
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
        time.sleep(2)

    def click_date_of_birth_field(self):
        element = self.wait_for_presence_of_element_located(self.date_of_birth_dropdown)
        element.click()
        time.sleep(1)

    def click_dob_field(self):
        self.click_date_of_birth_field()
        time.sleep(0.5)

    def get_dob_calendar_elements(self):
        elements = self.wait_for_presence_of_elements_located(self.dob_calendar_elements)
        items = elements[0].find_elements(By.XPATH, '*')
        print(items[0].get_attribute('innerHTML'))
        # time.sleep(2)
        return items[0]

    def click_dob_date(self, date_):
        calendar_elements_ = self.get_dob_calendar_elements()
        date_elements = calendar_elements_.find_elements(*self.calendar_date_element)
        ut = Utils()
        date_element = ut.find_element_by_text_from_list(date_, date_elements)
        date_element.click()
        time.sleep(3)
        dob_yyyy_dd_mm_field = self.wait_for_presence_of_element_located(self.dob_selected_yyyy_dd_mm)
        return dob_yyyy_dd_mm_field.get_attribute('value')

    def click_dob_left_arrow(self, no_of_click_=1):
        calendar_elements_ = self.get_dob_calendar_elements()
        dob_left_arrow = calendar_elements_.find_element(*self.calendar_left_arrow)
        while no_of_click_:
            dob_left_arrow.click()
            time.sleep(0.5)
            no_of_click_ -= 1
        time.sleep(1)

    def assert_dob_field(self, yyyy_dd_mm_):
        dob_yyyy_dd_mm_field = self.wait_for_presence_of_element_located(self.dob_selected_yyyy_dd_mm)
        return dob_yyyy_dd_mm_field.get_attribute('value') == yyyy_dd_mm_

    def select_gender(self, gender_=None):

        gender_elements = self.wait_for_presence_of_elements_located(self.gender_elements)
        for ele in gender_elements:
            gender_label = ele.find_element(By.XPATH, '..')
            if gender_label.text == gender_:
                self.driver.execute_script("arguments[0].click();", ele)
                time.sleep(2)
        time.sleep(1)

    def get_selected_gender(self):
        gender_elements = self.wait_for_presence_of_elements_located(self.gender_elements)
        for ele in gender_elements:
            print(ele.get_attribute("checked"))
            print(ele.is_selected())
            if ele.is_selected():
                gender_label = ele.find_element(By.XPATH, '..')
                return gender_label.text

    def assert_gender_option(self, gender_):
        return self.get_selected_gender() == gender_

    def click_save_personal_details(self):
        personal_details_save = self.wait_for_presence_of_element_located(self.personal_details_save_btn)
        personal_details_save.click()
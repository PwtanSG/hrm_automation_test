import time

from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By

from utilities.utils import Utils


class EmployeeAddPage(BaseDriver):

    # element locators
    first_name = (By.NAME, "firstName")
    middle_name = (By.NAME, "middleName")
    last_name = (By.NAME, "lastName")
    employee_id = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    menu_search_eid_input = (By.XPATH, "//input[@class='oxd-input oxd-input--active']")
    cancel_button = (By.XPATH, "//button[text()=' Cancel ']")
    # save_button = (By.XPATH, "//button[text()=' Save ']")
    save_button = (By.XPATH, "//button[@type='submit']")
    top_nav_bar_menu_items = (By.XPATH, "//a[@href='#']")
    create_login_option = (By.XPATH, "//input[@type='checkbox']")

    #  variables
    top_nav_employee_add = 'Add Employee'

    def __init__(self, driver):
        BaseDriver.__init__(driver)
        self.driver = driver

    def enter_first_name(self, fn_text_):
        fn_input_box = self.wait_for_presence_of_element_located(self.first_name)
        fn_input_box.send_keys(fn_text_)

    def enter_middle_name(self, mn_text_):
        mn_input_box = self.wait_for_presence_of_element_located(self.middle_name)
        mn_input_box.send_keys(mn_text_)

    def enter_last_name(self, ln_text_):
        ln_input_box = self.wait_for_presence_of_element_located(self.last_name)
        ln_input_box.send_keys(ln_text_)

    def enter_employee_id(self, id_):
        eid_input_box = self.wait_for_presence_of_element_located(self.employee_id)
        eid_input_box.send_keys(id_)

    def enter_eid(self, id_):
        input_boxes = self.wait_for_presence_of_elements_located(self.menu_search_eid_input)
        print(len(input_boxes))
        for input_ele in input_boxes:
            if not input_ele.get_attribute('placeholder'):
                print(input.ele)
                input.ele.send_keys(id_)

    def click_save_button(self):
        button_ele = self.wait_for_presence_of_element_located(self.save_button)
        # button_ele = self.wait_for_element_to_be_clickable(self.save_button)
        button_ele.click()

    def click_top_nav_menu_item(self, menu_item_name_):
        menu_items = self.wait_for_presence_of_elements_located(self.top_nav_bar_menu_items)
        ut = Utils()
        menu_item = ut.find_element_by_text_from_list(menu_item_name_, menu_items)
        menu_item.click()
        time.sleep(3)

    def get_employee_id_value(self):
        input_box_ele = self.wait_for_presence_of_element_located(self.employee_id)
        return input_box_ele.get_attribute('value')

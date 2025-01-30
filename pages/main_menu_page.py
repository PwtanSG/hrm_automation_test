import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class MainMenuPage(BaseDriver):

    # locators
    body = (By.TAG_NAME, "body")
    search_textbox = (By.XPATH, "//input[@placeholder='Search']")
    menu_items = (By.XPATH, "//li[@class='oxd-main-menu-item-wrapper']")

    full_menu_items = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard',
                       'Directory', 'Maintenance', 'Claim', 'Buzz']

    def __init__(self, driver):
        BaseDriver.__init__(driver)
        self.driver = driver

    def enter_search_box(self, search_text_):
        menu_search_textbox = self.wait_for_presence_of_element_located(self.search_textbox)
        if menu_search_textbox:
            menu_search_textbox.send_keys(search_text_)

    def clear_search_box(self):
        menu_search_textbox = self.wait_for_presence_of_element_located(self.search_textbox)
        if menu_search_textbox:
            menu_search_textbox.click()
            search_text = menu_search_textbox.get_attribute('value')
            search_text_length = len(search_text)
            i = 0
            while i < search_text_length:
                menu_search_textbox.send_keys(self.keyboard_backspace())
                time.sleep(0.3)
                i = i + 1

    def get_menu_items_list(self):
        menu_list = []
        menu_items = self.wait_for_presence_of_elements_located(self.menu_items)
        # print(len(menu_items))
        for item in menu_items:
            children = item.find_elements(By.XPATH, '*')
            if len(children) == 1:
                grand_children = children[0].find_elements(By.XPATH, '*')
                for element in grand_children:
                    if element.tag_name == 'span':
                        menu_list.append(element.text)
        return menu_list

    def assert_menu_list(self, expected_menu_list_):
        return self.get_menu_items_list() == expected_menu_list_

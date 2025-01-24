import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import BaseDriver
from utilities.utils import Utils
from datetime import datetime
import os
import time
from os import path
import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BaseDriver):

    TIMEOUT_CONST = 10

    def __init__(self, driver):
        BaseDriver.__init__(driver)
        self.driver = driver
        self.body = (By.TAG_NAME, "body")
        self.username_textbox = (By.NAME, "username")
        self.password_textbox = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.error_invalid_credential = (By.XPATH, "//p[text()='Invalid credentials']")
        self.user_profile_icon = (By.CLASS_NAME, "oxd-userdropdown-name")
        # self.user_profile_icon = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
        self.user_profile_dropdown_menu = (By.XPATH, "//a[@class='oxd-userdropdown-link']")
        self.co_website_link = (By.LINK_TEXT, "OrangeHRM, Inc")
        self.hyperlinks = (By.TAG_NAME, "a")
        # self.hyperlinks = (By.XPATH, "//a[@text='OrangeHRM, Inc']")

    def keyboard_press(self, keyname):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)

    def enter_username(self, username):
        username_textbox = self.wait_for_presence_of_element_located(self.username_textbox)
        if username_textbox:
            username_textbox.send_keys(username)

    def enter_password(self, password):
        password_textbox = self.wait_for_presence_of_element_located(self.password_textbox)
        if password_textbox:
            password_textbox.send_keys(password)

    def click_login(self):
        self.wait_for_element_to_be_clickable(self.login_button)

    def click_user_profile_icon(self):
        user_profile_icon = self.wait_for_presence_of_element_located(self.user_profile_icon)
        result = False
        if user_profile_icon:
            user_profile_icon.click()
            result = True
        return result

    def select_user_profile_dropdown_menu(self, menu_label):
        click_avatar = self.click_user_profile_icon()
        time.sleep(1)

        if click_avatar:
            element_list = self.wait_for_presence_of_elements_located(self.user_profile_dropdown_menu)
            ut = Utils()
            logout_element = ut.find_element_by_text_from_list(menu_label, element_list)
            if logout_element:
                logout_element.click()
                return True
            print('Element not found : ' + menu_label)

    def get_current_url(self):
        # wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
        # wait.until(EC.url_matches(expected_url))
        get_url = self.driver.current_url
        return str(get_url)

    def assert_url(self, url_):
        return self.wait_url_matches(url_)

    def find_error_invalid_credentials(self):
        error_msg_element = self.wait_for_presence_of_element_located(self.error_invalid_credential)
        return True if error_msg_element else False

    def get_co_website_link(self):
        return self.wait_for_presence_of_element_located(self.co_website_link)

    def get_hyperlinks(self):
        links = self.wait_for_presence_of_elements_located(self.hyperlinks)
        # links = self.driver.find_elements(By.XPATH, '//a')

    def find_element(self):
        try:
            self.driver.find_element(By.XPATH, "//input[@name='username']")
            return True
        except NoSuchElementException:
            print('NoSuchElementException')
            return False

    def switch_to_child_browser_window(self):
        # get current window handle
        parent_window = self.driver.current_window_handle

        # get first child window
        wd = self.driver.window_handles

        for w in wd:
            # switch focus to child window
            if w != parent_window:
                self.driver.switch_to.window(w)
                break
        time.sleep(1)


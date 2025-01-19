import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


class BaseDriver:

    TIMEOUT_CONST = 10

    def __int__(self, driver):
        self.driver = driver

    def get_page_length(self):
        return self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight")

    def page_scroll(self):
        time.sleep(2)
        page_length = self.get_page_length()
        match = False
        while not match:
            last_count = page_length
            time.sleep(3)
            page_length = self.get_page_length()
            if last_count == page_length:
                match = True
        time.sleep(2)

    def open_page(self, url_):
        self.driver.get(url_)
        wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
        try:
            wait.until(EC.url_to_be(url_))
            self.driver.fullscreen_window()
            return True
        except TimeoutException:
            print('Timeout : ' + sys._getframe().f_code.co_name + ' Line:' + str(sys._getframe().f_lineno))
            return False

    def wait_for_presence_of_element_located(self, locator_):
        element = ''
        wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
        try:
            element = wait.until(EC.presence_of_element_located(locator_))
            # return element
        except TimeoutException:
            print('Timeout : ' + sys._getframe().f_code.co_name + ' Line:' + str(sys._getframe().f_lineno))
        return element

    def wait_for_presence_of_elements_located(self, locator_):
        wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
        elements = []
        try:
            elements = wait.until(EC.presence_of_all_elements_located(self.user_profile_dropdown_menu))
            # print(len(menu_elements))
        except TimeoutException:
            print('Timeout : ' + sys._getframe().f_code.co_name + ' Line:' + str(sys._getframe().f_lineno))
        return elements

    def wait_for_element_to_be_clickable(self, locator_):
        wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
        clickable_element = ''
        try:
            clickable_element = wait.until(EC.element_to_be_clickable(locator_)).click()
            self.driver.fullscreen_window()
        except TimeoutException:
            print('Timeout : ' + sys._getframe().f_code.co_name + ' Line:' + str(sys._getframe().f_lineno))
        return clickable_element

    def wait_find_tag_elements_xpath_by_text(self, tag_, text_):
        wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
        elements_ = []
        try:
            # wait.until(EC.presence_of_element_located((By.XPATH, "//" + tag + "[text()='" + text + "']")))
            elements_ = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//" + tag_ + "[text()='" + text_ + "']")))
        except TimeoutException:
            print("Timeout finding element")

        return elements_

    def wait_for_visibility_of_element_located(self, tag_):
        wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
        try:
            time.sleep(1)
            element = wait.until(EC.visibility_of_element_located(tag_))
            return element
        except TimeoutException:
            print('Timeout : ' + sys._getframe().f_code.co_name + ' Line:' + str(sys._getframe().f_lineno))
            return ''

import os
import time
import sys
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BaseDriver:
    TIMEOUT_CONST = 10

    def __int__(self, driver):
        self.driver = driver

    def maximize_browser_window(self):
        return self.driver.maximize_window()

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

    def get_page_length(self):
        return self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight")

    def get_current_url(self):
        return self.driver.current_url

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
            elements = wait.until(EC.presence_of_all_elements_located(locator_))
            # print(len(elements))
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

    def wait_for_visibility_of_element_located(self, locator_):
        wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
        try:
            time.sleep(1)
            element = wait.until(EC.visibility_of_element_located(locator_))
            return element
        except TimeoutException:
            print('Timeout : ' + sys._getframe().f_code.co_name + ' Line:' + str(sys._getframe().f_lineno))
            return ''

    def wait_for_title_is(self, title_):
        wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
        result = False
        try:
            result = wait.until(EC.title_is(title_))
        except TimeoutException:
            print('Timeout : ' + sys._getframe().f_code.co_name + ' Line:' + str(sys._getframe().f_lineno))
        return result

    def assert_url(self, url_):
        wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
        try:
            result = wait.until(EC.url_matches(url_))
            # result = wait.until(EC.url_to_be(url_))
            if not result:
                print("Url not matches")
                # self.take_screenshot()
            time.sleep(2)
            return result
        except TimeoutException:
            print('Timeout : ' + sys._getframe().f_code.co_name + ' Line:' + str(sys._getframe().f_lineno) + ' ' + url_)
            return False

    def wait_for_url_changes(self, url_):
        wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
        try:
            result = wait.until(EC.url_changes(url_))
            print(result)
            return result
        except TimeoutException:
            print('Timeout : ' + sys._getframe().f_code.co_name + ' Line:' + str(sys._getframe().f_lineno))
            return False

    def take_screenshot(self):
        file_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(file_dir, exist_ok=True)

        today = datetime.now()
        image_name = today.strftime("%Y%m%d%H%M%S")
        wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
        try:
            time.sleep(1)
            element = wait.until(EC.visibility_of_element_located(self.body))
            file_path = os.path.join(file_dir, f"test_{image_name}.png")
            element.screenshot(file_path)
            # self.driver.get_screenshot_as_file(f"test_{image_name}.png")
            return True
        except TimeoutException:
            print('Timeout : ' + sys._getframe().f_code.co_name + ' Line:' + str(sys._getframe().f_lineno))
            return False

    def clear_input_box(self, locator_):
        input_box_element = self.wait_for_presence_of_element_located(locator_)
        if input_box_element:
            input_box_element.click()
            content = input_box_element.get_attribute('value')
            content_length = len(content)
            i = 0
            while i < content_length:
                input_box_element.send_keys(self.keyboard_backspace())
                time.sleep(0.3)
                i += 1

    def keyboard_press(self, keyname):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)

    @staticmethod
    def keyboard_backspace():
        return Keys.BACKSPACE

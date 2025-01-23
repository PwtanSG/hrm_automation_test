import os
import time
from os import path
import sys
from datetime import datetime
from base.base_driver import BaseDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Utils:

    # def take_screenshot(self):
    #     file_dir = path.join(os.getcwd(), "reports")
    #     os.makedirs(file_dir, exist_ok=True)
    #
    #     today = datetime.now()
    #     image_name = today.strftime("%Y%m%d%H%M%S")
    #     wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
    #     try:
    #         time.sleep(1)
    #         element = wait.until(EC.visibility_of_element_located(self.body))
    #         file_path = path.join(file_dir, f"test_{image_name}.png")
    #         element.screenshot(file_path)
    #         # self.driver.get_screenshot_as_file(f"test_{image_name}.png")
    #         return True
    #     except TimeoutException:
    #         print('Timeout : ' + sys._getframe().f_code.co_name + ' Line:' + str(sys._getframe().f_lineno))
    #         return False

    @staticmethod
    def find_element_by_text_from_list(element_text_, element_list_):
        for element in element_list_:
            if element.text == element_text_:
                return element
        return ''

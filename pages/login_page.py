import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from base.base_driver import BaseDriver


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
        username_textbox = BaseDriver.wait_for_presence_of_element_located(self, self.username_textbox)
        if username_textbox:
            username_textbox.send_keys(username)

    def enter_password(self, password):
        password_textbox = BaseDriver.wait_for_presence_of_element_located(self, self.password_textbox)
        if password_textbox:
            password_textbox.send_keys(password)

    def click_login(self):
        BaseDriver.wait_for_element_to_be_clickable(self, self.login_button)

    def click_user_profile_icon(self):
        user_profile_icon = BaseDriver.wait_for_presence_of_element_located(self, self.user_profile_icon)
        result = False
        if user_profile_icon:
            user_profile_icon.click()
            result = True
        return result

    def select_user_profile_dropdown_menu(self, menu_label):
        click_avatar = self.click_user_profile_icon()
        time.sleep(1)
        if click_avatar:
            element_list = BaseDriver.wait_for_presence_of_elements_located(self, self.user_profile_dropdown_menu)
            for menu_item in element_list:
                if menu_item.text == menu_label:
                    menu_item.click()
                    return True
            print('Menu not found : ' + menu_label)

    def get_current_url(self):
        # wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
        # wait.until(EC.url_matches(expected_url))
        get_url = self.driver.current_url
        return str(get_url)

    def check_url(self, url_):
        wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
        try:
            result = wait.until(EC.url_to_be(url_))
            if not result:
                print("Url not matches")
            time.sleep(2)
            # self.take_screenshot()
            return result
        except TimeoutException:
            print('Timeout : ' + sys._getframe().f_code.co_name + ' Line:' + str(sys._getframe().f_lineno))
            return False

    def find_error_invalid_credentials(self):
        error_msg_element = BaseDriver.wait_for_presence_of_element_located(self, self.error_invalid_credential)
        return True if error_msg_element else False

    def get_co_website_link(self):
        return BaseDriver.wait_for_presence_of_element_located(self, self.co_website_link)

    def get_hyperlinks(self):
        links = BaseDriver.wait_for_presence_of_elements_located(self, self.hyperlinks)
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
        # print("Child window title: " + self.driver.title)

    # def take_screenshot(self):
    #     file_dir = path.join(os.getcwd(), "reports")
    #     os.makedirs(file_dir, exist_ok=True)
    #
    #     wait = WebDriverWait(self.driver, self.TIMEOUT_CONST)
    #     today = datetime.now()
    #     image_name = today.strftime("%Y%m%d%H%M%S")
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

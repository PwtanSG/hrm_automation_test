import os
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from base.base_driver import BaseDriver
from utilities.utils import Utils
from dotenv import load_dotenv


class LoginPage(BaseDriver):

    TIMEOUT_CONST = 10

    # locators
    body = (By.TAG_NAME, "body")
    username_textbox = (By.NAME, "username")
    password_textbox = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    error_invalid_credential = (By.XPATH, "//p[text()='Invalid credentials']")
    user_profile_icon = (By.CLASS_NAME, "oxd-userdropdown-name")
    user_profile_dropdown_menu = (By.XPATH, "//a[@class='oxd-userdropdown-link']")
    co_website_link = (By.LINK_TEXT, "OrangeHRM, Inc")
    forget_password_link = (By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.orangehrm-login-forgot-header")
    hyperlinks = (By.TAG_NAME, "a")
    # hyperlinks = (By.XPATH, "//a[@text='OrangeHRM, Inc']")

    # application admin login credentials
    load_dotenv()
    valid_username = os.getenv('VALID_USERNAME')
    valid_password = os.getenv('VALID_PASSWORD')
    login_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, driver):
        BaseDriver.__init__(driver)
        self.driver = driver

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

    def find_error_invalid_credentials(self):
        error_msg_element = self.wait_for_presence_of_element_located(self.error_invalid_credential)
        return True if error_msg_element else False

    def get_co_website_link(self):
        return self.wait_for_presence_of_element_located(self.co_website_link)

    def get_forget_password_link(self):
        return self.wait_for_presence_of_element_located(self.forget_password_link)

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

    def login_application(self, login_page_url_, username_, password_):
        # open browser and go to login page
        self.open_page(login_page_url_)
        # fill in username and password
        self.enter_username(username_)
        self.enter_password(password_)
        # click login button
        self.click_login()

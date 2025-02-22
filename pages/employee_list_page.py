import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.main_menu_page import MainMenuPage
from utilities.utils import Utils


class EmployeeListPage(BaseDriver):
    # locators
    top_nav_bar_menu_items = (By.XPATH, "//a[@href='#']")
    input_textbox_elements = (By.XPATH, "//input[contains(@placeholder,'Type for hints')]")
    input_box_employee_id = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    job_title_filter_menu = (By.XPATH, "//div[@role='listbox']")
    dropdown_elements_arrow = (By.XPATH, "//div[@class ='oxd-select-text--after']")
    search_button = (By.XPATH, "//button[@type='submit']")
    reset_button = (By.XPATH, "//button[@type='reset']")
    result_rows = (By.XPATH, "//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']")
    employee_found_count = (By.XPATH, "//div//span[@class='oxd-text oxd-text--span']")
    current_user_avatar = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    record_trash = (By.XPATH, "//button//i[@class='oxd-icon bi-trash']")
    record_edit = (By.XPATH, "//button//i[@class='oxd-icon bi-pencil-fill']")
    delete_modal = (By.XPATH, "//div[@class='orangehrm-modal-footer']")
    modal_delete_button = (By.XPATH, "//i[@class='oxd-icon bi-trash oxd-button-icon']")
    modal_cancel_button = (By.XPATH, "//button[text()=' No, Cancel ']")
    # modal_delete_button = (By.XPATH, "//div[@class='orangehrm-modal-footer']//button[2]")
    # toast_msg_element = (By.XPATH, "//div[@class='oxd-toast oxd-toast--info oxd-toast-container--toast']")
    # toast_msg_element = (By.XPATH, "//[@class='oxd-toast-start']")

    main_menu_name_employee_page = 'PIM'
    employee_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
    top_nav_employee_list = 'Employee List'
    result_columns = ['', 'id', 'First (& Middle) Name', 'Last Name', 'Job Title', 'Employment Status', 'Sub Unit',
                      'Supervisor', 'Actions']

    def __init__(self, driver):
        BaseDriver.__init__(driver)
        self.driver = driver

    def click_top_nav_menu_item(self, menu_item_name_):
        menu_items = self.wait_for_presence_of_elements_located(self.top_nav_bar_menu_items)
        ut = Utils()
        menu_item = ut.find_element_by_text_from_list(menu_item_name_, menu_items)
        menu_item.click()
        time.sleep(3)

    def get_count_element(self):
        return self.wait_for_presence_of_element_located(self.employee_found_count)

    def get_search_result_count(self):
        search_count_element = self.wait_for_presence_of_element_located(self.employee_found_count)
        search_result = search_count_element.text
        if search_result != 'No Records Found':
            # (1) Record Found return value
            return int(search_result[1])
        return 0

    def enter_name_input_box(self, text_):
        elements = self.wait_for_presence_of_elements_located(self.input_textbox_elements)
        elements[0].send_keys(text_)

    def get_dropdown_element(self, value_):
        # 0 Employment Status, 1 include, 2 Job Title, 3 Sub Unit
        elements = self.wait_for_presence_of_elements_located(self.dropdown_elements_arrow)
        return elements[value_]

    def filter_by_dropdown_job_title(self, job_title_):
        job_title_filter = self.get_dropdown_element(2)
        job_title_filter.click()
        filter_menu = self.wait_for_presence_of_element_located(self.job_title_filter_menu)
        filter_menu_items = filter_menu.find_elements(By.XPATH, '*')
        for menu_item in filter_menu_items:
            if menu_item.text == job_title_:
                menu_item.click()
                break

    def click_delete_employee_record(self):
        delete_icon = self.wait_for_presence_of_element_located(self.record_trash)
        delete_icon.click()

    def get_all_search_results(self):
        return self.wait_for_presence_of_elements_located(self.result_rows)

    def assert_search_result_job_title(self, result_rows, job_title_):
        # 0 Employment Status, 1 include, 2 Job Title, 3 Sub Unit
        results = []
        for row in result_rows:
            column_elements = row.find_elements(By.XPATH, '*')
            if column_elements[4].text == job_title_:
                results.append(True)
            else:
                print(column_elements[1].text + ' ' + column_elements[2].text + ' : ' + column_elements[4].text +
                      ' incorrect job title')
                results.append(False)

        if not result_rows:
            return len(result_rows) == self.get_search_result_count()
        else:
            return all(result_rows) and len(result_rows) == self.get_search_result_count()

    def get_current_user_name(self, return_name_option_='full_name'):
        avatar_element = self.wait_for_presence_of_element_located(self.current_user_avatar)
        full_name = avatar_element.text
        match return_name_option_:
            case 'last_name':
                name = full_name.split()
                return name[-1]
            case 'first_name':
                name = full_name.split()
                return name[0]
            case _:
                return full_name

    def assert_search_results_name(self, result_rows, value_):
        results = []
        first_name_col_ = 2
        last_name_col_ = 3
        for row in result_rows:
            column_elements = row.find_elements(By.XPATH, '*')
            if value_ in column_elements[first_name_col_].text or value_ in column_elements[last_name_col_].text:
                results.append(True)
            else:
                print('Failed:' + column_elements[first_name_col_].text + ' ' + column_elements[last_name_col_].text +
                      ' : incorrect' + ' ' + value_)
                results.append(False)

        if not result_rows:
            return len(result_rows) == self.get_search_result_count()
        else:
            return all(result_rows) and len(result_rows) == self.get_search_result_count()

    def click_search_button(self):
        self.wait_for_element_to_be_clickable(self.search_button)

    def search_by_employee_id(self, employee_id_):
        reset_btn = self.wait_for_presence_of_element_located(self.reset_button)
        input_box_element = self.wait_for_presence_of_element_located(self.input_box_employee_id)
        if input_box_element.get_attribute('value'):
            reset_btn.click()
        time.sleep(1)
        input_box_element.send_keys(employee_id_)
        time.sleep(1)
        self.click_search_button()
        time.sleep(1)
        if not self.get_search_result_count():
            return []
        return self.get_all_search_results()

    def get_first_search_result_eid(self):
        self.wait_for_presence_of_element_located(self.reset_button).click()
        self.click_search_button()
        if self.get_search_result_count():
            search_results = self.get_all_search_results()
            first_rec = search_results[0]
            column_elements = first_rec.find_elements(By.XPATH, '*')
            col_eid = column_elements[1]
            return col_eid.text
        return '0'

    @staticmethod
    def assert_search_result_by_id(result_list_, employee_id_, first_middle_name_=None, last_name_=None):
        """
        validate employee record by employee id and validate record matches employee id, name(optional)
        :param result_list_:
        :param employee_id_: required
        :param first_middle_name_: optional
        :param last_name_: optional
        :return: True if found
        """
        if len(result_list_) == 1:
            search_result = result_list_[0]
            column_elements = search_result.find_elements(By.XPATH, '*')
            col_eid = column_elements[1]
            col_first_middle_name = column_elements[2]
            col_last_name = column_elements[3]

            # validate with employee id ONLY
            if not first_middle_name_ or not last_name_:
                if col_eid.text == employee_id_:
                    return True
                return False

            # validate with employee id and name
            if col_eid.text == employee_id_ and col_first_middle_name.text == first_middle_name_ and \
                    col_last_name.text == last_name_:
                return True
            else:
                print(col_eid.text + ' ' + col_first_middle_name.text + ' : ' + col_last_name.text)
                return False
        print('No records found.')
        return False

    def toast_message(self):
        toast_element = self.wait_for_presence_of_element_located(self.toast_msg_element)
        print(toast_element)

    def click_modal_delete_button(self):
        modal_footer = self.wait_for_visibility_of_element_located(self.delete_modal)
        delete_button_ele = modal_footer.find_element(*self.modal_delete_button)
        # cancel_button_ele = modal_footer.find_element(*self.modal_cancel_button)
        time.sleep(1)
        delete_button_ele.click()
        time.sleep(1)

    def delete_employee_record_by_id(self, employee_id):
        self.click_top_nav_menu_item(self.top_nav_employee_list)
        time.sleep(1)
        search_results_list = self.search_by_employee_id(employee_id)
        if not search_results_list:
            print('Fail Employee id : ' + employee_id + " not found")
            return False
        record_found = self.assert_search_result_by_id(search_results_list, employee_id)
        if record_found:
            self.click_delete_employee_record()
            time.sleep(1)
            self.click_modal_delete_button()
            return True
        return False

    def click_edit_emp_button(self):
        edit_button = self.wait_for_presence_of_element_located(self.record_edit)
        edit_button.click()
        self.maximize_browser_window()

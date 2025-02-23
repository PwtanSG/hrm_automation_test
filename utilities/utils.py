import random
import string
from datetime import datetime


class Utils:

    @staticmethod
    def find_element_by_text_from_list(element_text_, element_list_):
        for element in element_list_:
            if element.text == element_text_:
                return element
        return ''

    @staticmethod
    def gen_emp_id(prefix=None, digit_len=4):
        # digits = string.digits
        # eid = ''.join(random.choice(digits) for _ in range(digit_len))
        eid = ''.join(str(random.randrange(1, 10)) for _ in range(digit_len))
        return eid if not prefix else prefix + eid

    @staticmethod
    def get_today_date(return_option=None):
        if not return_option:
            return datetime.today().strftime('%Y-%m-%d')

        return_option = return_option.lower()
        match return_option:
            case 'year':
                return datetime.today().strftime('%Y')
            case 'month':
                return datetime.today().strftime('%m')
            case 'day':
                return datetime.today().strftime('%d')
            case _:
                print(f'unknown return_option : {return_option}')
                return datetime.today().strftime('%Y-%m-%d')

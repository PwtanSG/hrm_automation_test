
class Utils:

    @staticmethod
    def find_element_by_text_from_list(element_text_, element_list_):
        for element in element_list_:
            if element.text == element_text_:
                return element
        return ''

import time
import pytest
from pages.login_page import LoginPage
from pages.main_menu_page import MainMenuPage


@pytest.mark.parametrize("test_label_, search_text_, expected_menu_list_",
                         [("Test search Found 1", "adm", ['Admin']),
                          ("Test search Found 2", "L", ['Leave', 'Claim']),
                          ("Test unsuccessful search", "Timr", [])])
def test_main_menu_search_clear(chrome_driver, test_label_, search_text_, expected_menu_list_):
    login_page = LoginPage(chrome_driver)
    login_page.login_application(login_page.login_page_url, login_page.valid_username, login_page.valid_password)
    main_menu_page = MainMenuPage(chrome_driver)
    # side_menu_page.take_screenshot()
    time.sleep(1)
    # search menu item
    main_menu_page.enter_search_box(search_text_)
    time.sleep(1)
    assert_menu_item_found = main_menu_page.assert_menu_list(expected_menu_list_)

    # clear search box
    main_menu_page.clear_search_box()
    time.sleep(1)
    assert_full_menu_items = main_menu_page.assert_menu_list(main_menu_page.full_menu_items)
    # assert test
    assert assert_menu_item_found and assert_full_menu_items


def test_main_menu_list(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.login_application(login_page.login_page_url, login_page.valid_username, login_page.valid_password)
    main_menu_page = MainMenuPage(chrome_driver)
    time.sleep(2)
    assert main_menu_page.assert_menu_list(main_menu_page.full_menu_items)

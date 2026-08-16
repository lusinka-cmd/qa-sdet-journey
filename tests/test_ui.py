import pytest

from pages.saucedemo_page import SauceDemoLoginPage


@pytest.mark.ui
def test_valid_user_can_open_inventory(page):
    login_page = SauceDemoLoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    login_page.verify_inventory_is_displayed()


@pytest.mark.ui
def test_invalid_user_sees_login_error(page):
    login_page = SauceDemoLoginPage(page)

    login_page.open()
    login_page.login("invalid_user", "wrong_password")

    login_page.verify_login_error()

# tests/test_main_page_navigation.py
import allure
import pytest
from pages.main_page import MainPage


class TestNavigation:

    @allure.title("Проверка перехода к блоку 'О нас'")
    def test_about_us_link_block(self, page):
        main_page = MainPage(page)
        main_page.open()
        main_page.about_us_link.click()
        with allure.step("Проверяем наличие якоря в URL"):
            assert "#about" in page.url
        assert main_page.about_us_anchor.is_visible()

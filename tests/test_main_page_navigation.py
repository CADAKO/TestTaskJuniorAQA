# tests/test_main_page_navigation.py
import allure
import pytest
from pages.main_page import MainPage


class TestNavigation:

    @allure.title("Проверка перехода к блоку 'О нас'")
    def test_about_us_link_block(self, page: MainPage):
        main_page = MainPage(page)
        main_page.open()
        main_page.about_us_link.click()
        with allure.step("Проверяем наличие якоря в URL"):
            assert "#about" in page.url
        assert main_page.about_us_anchor.is_visible()

    @allure.title("Проверка перехода к блоку 'Контакты'")
    def test_contacts_link_block(self, page: MainPage):
        main_page = MainPage(page)
        main_page.open()
        main_page.contacts_link.click()
        with allure.step("Проверяем наличие якоря в URL"):
            assert "#contact" in page.url
        assert main_page.contacts_anchor.is_visible()

    @allure.title("Проверка перехода к блоку 'Вакансии'")
    def test_specializations_link_block(self, page: MainPage):
        main_page = MainPage(page)
        main_page.open()
        main_page.specializations_link.click()
        with allure.step("Проверяем наличие якоря в URL"):
            assert "#specializations" in page.url
        assert main_page.specializations_anchor.is_visible()

    @allure.title("Проверка перехода к блоку 'Отзывы'")
    def test_feedback_link_block(self, page: MainPage):
        main_page = MainPage(page)
        main_page.open()
        main_page.feedback_link.click()
        with allure.step("Проверяем наличие якоря в URL"):
            assert "#testimonials" in page.url
        assert main_page.feedback_anchor.is_visible()

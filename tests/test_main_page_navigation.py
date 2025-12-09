# tests/test_main_page_navigation.py
import allure
import pytest
from pages.main_page import MainPage
from playwright.sync_api import Page, Locator


class TestNavigation:
    @pytest.mark.parametrize(
        "link_text, anchor, anchor_text",
        [('О нас', '#about', 'О компании'),
         ('Контакты', '#contact', 'Контактная информация'),
         ('Вакансии', '#specializations', 'Кого мы ищем'),
         ('Отзывы', '#testimonials', 'Отзывы специалистов')]
    )
    @allure.title("Проверка перехода к блоку {link_text}")
    def test_navigation_to_block(self, page: Page, link_text: str,
                                 anchor: str, anchor_text: str):
        main_page = MainPage(page)
        with allure.step(f'Открываем страницу {main_page.BASE_URL}'):
            main_page.open()
        with allure.step(f"Кликаем по ссылке '{link_text}'"):
            page.get_by_role(role='link', name=link_text, exact=True).click()
        with allure.step("Проверяем наличие якоря в URL"):
            assert anchor in page.url
        with allure.step("Проверяем видимость целевого блока"):
            assert page.get_by_text(anchor_text).is_visible()

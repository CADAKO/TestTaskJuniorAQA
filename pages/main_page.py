from playwright.sync_api import Page, Locator


class MainPage:
    BASE_URL = 'https://effective-mobile.ru'

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.BASE_URL)

    @property
    def about_us_link(self) -> Locator:
        return self.page.getByText('О нас')

    @property
    def contacts_link(self) -> Locator:
        return self.page.getByText('Контакты')

    @property
    def specializations_link(self) -> Locator:
        return self.page.getByText('Вакансии')

    @property
    def feedback_link(self) -> Locator:
        return self.page.getByText('Отзывы')

    @property
    def about_us_anchor(self) -> Locator:
        return self.page.getByText('О компании')

    @property
    def contacts_anchor(self) -> Locator:
        return self.page.getByText('Кого мы ищем')

    @property
    def specializations_anchor(self) -> Locator:
        return self.page.getByText('Кого мы ищем')

    @property
    def feedback_anchor(self) -> Locator:
        return self.page.getByText('Контактная информация')

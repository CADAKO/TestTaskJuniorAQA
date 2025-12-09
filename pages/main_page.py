from playwright.sync_api import Page, Locator


class MainPage:
    BASE_URL = 'https://effective-mobile.ru'

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.BASE_URL)

    @property
    def about_us_link(self) -> Locator:
        return self.page.get_by_role(role='link', name='О нас', exact=True)

    @property
    def contacts_link(self) -> Locator:
        return self.page.get_by_role(role='link', name='Контакты', exact=True)

    @property
    def specializations_link(self) -> Locator:
        return self.page.get_by_role(role='link', name='Вакансии', exact=True)

    @property
    def feedback_link(self) -> Locator:
        return self.page.get_by_role(role='link', name='Отзывы', exact=True)

    @property
    def about_us_anchor(self) -> Locator:
        return self.page.get_by_text('О компании')

    @property
    def contacts_anchor(self) -> Locator:
        return self.page.get_by_text('Контактная информация')

    @property
    def specializations_anchor(self) -> Locator:
        return self.page.get_by_text('Кого мы ищем')

    @property
    def feedback_anchor(self) -> Locator:
        return self.page.get_by_text('Отзывы специалистов')

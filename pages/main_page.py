from playwright.sync_api import Page, Locator


class MainPage:
    BASE_URL = 'https://effective-mobile.ru'

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.BASE_URL)


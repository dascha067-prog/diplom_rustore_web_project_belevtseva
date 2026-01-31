import allure
from selene import browser, be, have
from selenium.webdriver.common.keys import Keys

from pages.app_page import AppPage


class SearchPage:
    search_input = browser.element('[data-testid="search_input"]')

    app_cards = browser.all('//a[contains(@href, "/catalog/app/")]')

    def should_have_input(self):
        with allure.step("Убедиться, что поле поиска отображается"):
            self.search_input.should(be.visible)
        return self

    def type_query(self, query: str):
        with allure.step(f"Ввести поисковый запрос: {query}"):
            self.search_input.should(be.visible).click()
            self.search_input.set_value(query)
        return self

    def should_have_query(self, query: str):
        with allure.step(f"Проверить, что в поле поиска указан запрос: {query}"):
            self.search_input.should(have.value_containing(query))
        return self

    def submit(self):
        with allure.step("Запустить поиск"):
            self.search_input.should(be.visible).send_keys(Keys.ENTER)
        return self

    def should_have_results(self):
        with allure.step("Проверить, что результаты поиска отображаются"):
            self.app_cards.should(have.size_greater_than(0))
        return self

    def open_first_result(self):
        with allure.step("Открыть первую карточку из результатов"):
            self.app_cards.first.should(be.visible).click()
        return AppPage()

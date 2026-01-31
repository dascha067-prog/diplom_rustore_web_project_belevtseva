# import allure
# from selene import browser, be, have
# from selenium.webdriver.common.keys import Keys
#
# from pages.app_page import AppPage
#
#
# class SearchPage:
#     search_input = browser.element('[data-testid="search_input"]')
#     find_button = browser.element('//a[contains(.,"Найти")]')
#
#     app_cards = browser.all('a[href*="/catalog/app/"]')
#
#     @allure.step("Убедиться, что поле поиска отображается")
#     def should_have_input(self):
#         self.search_input.should(be.visible)
#         return self
#
#     @allure.step("Ввести поисковый запрос: {query}")
#     def type_query(self, query: str):
#         self.search_input.should(be.visible).click()
#         self.search_input.set_value(query)
#         return self
#
#     @allure.step("Проверить, что в поле поиска указан запрос: {query}")
#     def should_have_query(self, query: str):
#         self.search_input.should(have.value_containing(query))
#         return self
#
#     @allure.step("Запустить поиск")
#     def submit(self):
#         if self.find_button.matching(be.visible):
#             self.find_button.click()
#         else:
#             self.search_input.should(be.visible).send_keys(Keys.ENTER)
#         return self
#
#     @allure.step("Проверить, что отображаются подсказки поиска")
#     def should_have_suggestions(self):
#         self.suggest_options.should(have.size_greater_than(0))
#         return self
#
#     @allure.step("Проверить, что результаты поиска отображаются")
#     def should_have_results(self):
#         self.app_cards.should(have.size_greater_than(0))
#         return self
#
#     @allure.step("Открыть первую карточку из результатов")
#     def open_first_result(self):
#         self.app_cards.should(have.size_greater_than(0))
#         self.app_cards.first.should(be.clickable).click()
#         return AppPage()
#
#     @allure.step("Очистить поле поиска")
#     def clear_query(self):
#         self.search_input.should(be.visible).click()
#         self.search_input.send_keys(Keys.CONTROL, "a")
#         self.search_input.send_keys(Keys.BACKSPACE)
#         self.search_input.should(have.value(""))
#         return self

import allure
from selene import browser, be, have
from selenium.webdriver.common.keys import Keys

from pages.app_page import AppPage


class SearchPage:
    search_input = browser.element('[data-testid="search_input"]')

    # результаты: просто ссылки на карточки приложений
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

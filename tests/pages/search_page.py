import allure
from selene import browser, be, have
from selenium.webdriver.common.keys import Keys


class SearchPage:
    search_input = browser.element('[data-testid="search_input"]')

    find_button = browser.element('//a[contains(., "Найти")]')

    suggest_options = browser.all('a[class*="SuggestOption_option"]')
    app_cards = browser.all('[data-testid="apps_list"] a[href*="/catalog/app/"]')

    class SearchPage:
        search_input = browser.element('[data-testid="search_input"]')

        find_button = browser.element('//a[contains(., "Найти")]')

        suggest_options = browser.all('a[class*="SuggestOption_option"]')
        app_cards = browser.all('[data-testid="apps_list"] a[href*="/catalog/app/"]')

    @allure.step("Убедиться, что поле поиска отображается")
    def should_have_input(self):
        self.search_input.should(be.visible)
        return self

    @allure.step("Ввести поисковый запрос: {query}")
    def type_query(self, query: str):
        self.search_input.should(be.visible).click()
        self.search_input.set_value(query)
        return self

    @allure.step("Проверить, что в поле поиска указан запрос: {query}")
    def should_have_query(self, query: str):
        self.search_input.should(have.value_containing(query))
        return self

    @allure.step("Запустить поиск")
    def submit(self):
        # 1) Пробуем клик по кнопке "Найти"
        if self.find_button.matching(be.visible):
            self.find_button.click()
            return self

        # 2) Если кнопки нет — fallback на Enter
        self.search_input.should(be.visible).send_keys(Keys.ENTER)
        return self

    @allure.step("Проверить, что отображаются подсказки поиска")
    def should_have_suggestions(self):
        self.suggest_options.should(have.size_greater_than(0))
        return self

    @allure.step("Проверить, что результаты поиска отображаются")
    def should_have_results(self):

        if self.suggest_options.matching(have.size_greater_than(0)):
            return self

        self.app_cards.should(have.size_greater_than(0))
        return self

    @allure.step("Проверить, что результатов поиска нет")
    def should_have_no_results(self):

        self.suggest_options.should(have.size(0))
        self.app_cards.should(have.size(0))
        return self

    @allure.step("Очистить поле поиска")
    def clear_query(self):
        self.search_input.should(be.visible).click()
        self.search_input.send_keys(Keys.CONTROL, 'a')
        self.search_input.send_keys(Keys.BACKSPACE)
        self.search_input.should(have.value(""))
        return self

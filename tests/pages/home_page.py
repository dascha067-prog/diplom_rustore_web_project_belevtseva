import allure
from selene import browser, be


class HomePage:
    logo = browser.element('[data-testid="header_logo"]')
    search_button = browser.element('[data-testid="header_search_button"]')

    def open(self):
        with allure.step("Открыть главную страницу RuStore"):
            browser.open("/")
        return self

    def should_be_opened(self):
        with allure.step("Проверить, что главная страница открылась"):
            browser.should(lambda br: "rustore.ru" in br.driver.current_url)
        return self

    def should_have_logo(self):
        with allure.step("Проверить, что логотип отображается"):
            self.logo.should(be.visible)
        return self

    def should_have_search_button(self):
        with allure.step("Проверить, что кнопка 'Найти' отображается и кликабельна"):
            self.search_button.should(be.visible).should(be.clickable)
        return self

    def open_search(self):
        with allure.step("Открыть поиск (клик по кнопке 'Найти')"):
            self.search_button.should(be.clickable).click()
        return self

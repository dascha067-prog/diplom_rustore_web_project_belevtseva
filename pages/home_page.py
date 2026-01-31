import allure
from selene import browser, be

from pages.search_page import SearchPage


class HomePage:
    # верхнее меню по тексту
    apps_menu = browser.element('//a[normalize-space()="Приложения"]')
    games_menu = browser.element('//a[normalize-space()="Игры"]')
    kiosk_menu = browser.element('//a[normalize-space()="Киоск"]')
    blog_menu = browser.element('//a[normalize-space()="Блог"]')
    devs_menu = browser.element('//a[contains(normalize-space(),"Разработ")]')
    help_menu = browser.element('//a[normalize-space()="Помощь"]')

    search_button = browser.element('[data-testid="header_search_button"]')

    def open(self):
        with allure.step("Открыть главную страницу RuStore"):
            browser.open("https://www.rustore.ru/")
        return self

    def should_have_top_menu(self):
        with allure.step("Проверить, что пункты меню отображаются"):
            self.apps_menu.should(be.visible)
            self.games_menu.should(be.visible)
            self.kiosk_menu.should(be.visible)
            self.blog_menu.should(be.visible)
            self.devs_menu.should(be.visible)
            self.help_menu.should(be.visible)
        return self

    def open_search(self):
        with allure.step("Нажать кнопку 'Найти'"):
            self.search_button.should(be.visible).should(be.clickable).click()
        return SearchPage()

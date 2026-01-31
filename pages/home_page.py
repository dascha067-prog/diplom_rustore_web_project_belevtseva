# import allure
# from selene import browser, be
# from pages.search_page import SearchPage
#
#
# class HomePage:
#     logo = browser.element('[data-testid="header_logo"] img')
#     search_button = browser.element('[data-testid="header_search_button"]')
#
#     def open(self):
#         with allure.step("Открыть главную страницу RuStore"):
#             browser.open("/")
#         return self
#
#     def should_be_opened(self):
#         with allure.step("Проверить, что главная страница загрузилась (URL + ключевые элементы)"):
#             browser.should(lambda br: "rustore.ru" in br.driver.current_url)
#             self.logo.should(be.visible)
#             self.search_button.should(be.visible)
#         return self
#
#     def should_have_logo(self):
#         with allure.step("Проверить, что логотип отображается и изображение загружено"):
#             self.logo.should(be.visible)
#
#             browser.should(
#                 lambda br: bool(
#                     br.driver.execute_script(
#                         "const img = arguments[0]; return img && (img.currentSrc || img.src) ? (img.currentSrc || img.src) : '';",
#                         self.logo()
#                     )
#                 )
#             )
#
#             real_src = browser.driver.execute_script(
#                 "const img = arguments[0]; return img.currentSrc || img.src || '';",
#                 self.logo()
#             )
#             assert real_src, "У логотипа пустой src/currentSrc"
#
#             loaded = browser.driver.execute_script(
#                 "const img = arguments[0]; return img.complete && img.naturalWidth > 0;",
#                 self.logo()
#             )
#             assert loaded, "Картинка логотипа не загрузилась (битая/не отрисована)"
#         return self
#
#     def should_have_search_button(self):
#         with allure.step("Проверить, что кнопка 'Найти' отображается и кликабельна"):
#             self.search_button.should(be.visible).should(be.clickable)
#         return self
#
#     def open_search(self):
#         with allure.step("Открыть поиск (клик по кнопке 'Найти')"):
#             self.search_button.should(be.visible).should(be.clickable).click()
#         return SearchPage()

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
            browser.open("/")
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

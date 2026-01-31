import allure
from selene import browser, be, have


class InstallPage:
    page_title = browser.element("h1")
    download_button = browser.element(
        '//a[contains(., "Скачать RuStore")] | //button[contains(., "Скачать RuStore")]'
    )

    def should_be_opened(self):
        with allure.step("Проверить, что открылась страница установки RuStore"):
            self.page_title.should(be.visible)
            self.page_title.should(have.text_containing("Как установить"))
        return self

    def download_rustore(self):
        with allure.step("Нажать 'Скачать RuStore'"):
            self.download_button.should(be.visible).should(be.clickable).click()
        return self

import allure
from selene import browser, be, query


class AppPage:
    title = browser.element('h1')

    # Кнопка "Установить с помощью RuStore" (стабильный data-testid)
    install_with_rustore = browser.element('[data-testid="deepLinkButton"]')

    # QR flow
    qr_button = browser.element('[data-testid="qr-button"]')
    qr_modal = browser.element('[data-testid="qr-tooltip"]')
    qr_text = browser.element('//*[contains(text(),"Наведите камеру")]')
    qr_image = browser.element('//*[contains(text(),"Наведите камеру")]/preceding::img[1]')
    close_qr = qr_modal.element('button[aria-label="Закрыть"], button[aria-label="Close"], button')  # запасной

    def should_be_opened(self):
        with allure.step("Проверить, что открылась страница приложения"):
            self.title.should(be.visible)
            title_text = self.title.get(query.text).strip()
            assert title_text != "", "Заголовок страницы приложения пустой"
        return self

    def should_have_install_button(self):
        with allure.step("Проверить, что кнопка 'Установить с помощью RuStore' отображается и кликабельна"):
            self.install_with_rustore.should(be.visible).should(be.clickable)
        return self

    def open_qr_modal(self):
        with allure.step("Открыть QR-код для установки приложения"):
            self.qr_button.should(be.visible).should(be.clickable).click()
        return self

    def should_have_qr_modal(self):
        with allure.step("Проверить, что отображается QR-модальное окно"):
            self.qr_text.should(be.visible)
            self.qr_image.should(be.visible)

            src = self.qr_image.get(query.attribute('src')) or ""
            assert src.strip() != "", "У QR-картинки пустой src"
        return self

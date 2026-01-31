import allure
import pytest

from pages.home_page import HomePage


@allure.epic("RuStore Web UI")
@allure.feature("Main flow")
@allure.tag("ui", "web")
@pytest.mark.ui
class TestRuStoreFlow:

    @allure.title("Главная: пункты меню отображаются")
    def test_top_menu_items_visible(self):
        HomePage().open().should_have_top_menu()

    @allure.title("Поиск: открытие поля поиска по кнопке 'Найти'")
    def test_open_search(self):
        HomePage().open().open_search().should_have_input()

    @allure.title("Поиск: ввод запроса telegram")
    def test_type_query_telegram(self):
        query = "telegram"
        HomePage().open().open_search().should_have_input().type_query(query).should_have_query(query)

    @allure.title("Поиск: по запросу telegram отображаются результаты")
    def test_search_telegram_has_results(self):
        query = "telegram"
        (
            HomePage()
            .open()
            .open_search()
            .should_have_input()
            .type_query(query)
            .submit()
            .should_have_results()
        )

    @allure.title("Поиск: открыть первую карточку из результатов")
    def test_open_first_search_result(self):
        query = "telegram"
        app_page = (
            HomePage()
            .open()
            .open_search()
            .should_have_input()
            .type_query(query)
            .submit()
            .should_have_results()
            .open_first_result()
        )
        app_page.should_be_opened()

    @allure.title("Приложение: кнопка 'Установить с помощью RuStore' отображается и кликабельна")
    def test_app_has_install_with_rustore_button(self):
        query_text = "telegram"

        app_page = (
            HomePage()
            .open()
            .open_search()
            .should_have_input()
            .type_query(query_text)
            .submit()
            .should_have_results()
            .open_first_result()
            .should_be_opened()
        )

        app_page.should_have_install_button()

    @allure.title("Приложение: отображается QR-код для установки через RuStore")
    def test_app_qr_install_flow(self):
        query_text = "telegram"

        (
            HomePage()
            .open()
            .open_search()
            .should_have_input()
            .type_query(query_text)
            .submit()
            .should_have_results()
            .open_first_result()
            .should_be_opened()
            .open_qr_modal()
            .should_have_qr_modal()
        )

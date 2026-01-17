import allure
import pytest

from tests.pages.home_page import HomePage


@allure.epic("RuStore Web UI")
@allure.feature("Search")
@allure.label("layer", "ui")
@allure.label("layer", "web")
@allure.tag("ui")
@pytest.mark.ui
class TestHomePage:

    @allure.story("Проверка открытия главной страницы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_home_page(self):
        HomePage().open().should_be_opened().should_have_logo()

    @allure.story("Проверка наличия кнопки найти")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_button_visible(self):
        HomePage().open().should_have_search_button()

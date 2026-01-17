import allure
import pytest

from tests.pages.home_page import HomePage
from tests.pages.search_page import SearchPage


@allure.epic("RuStore Web UI")
@allure.feature("Search")
@allure.label("layer", "ui")
@allure.label("layer", "web")
@allure.tag("ui")
@pytest.mark.ui
class TestSearch:
    @allure.title("Открытие поля поиска")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("search", "open")
    def test_open_search_input(self):
        HomePage().open().open_search()
        SearchPage().should_have_input()

    @allure.title("Ввод запроса: telegram")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("search", "input")
    def test_type_query_telegram(self):
        query = "telegram"
        HomePage().open().open_search()
        SearchPage().should_have_input().type_query(query).should_have_query(query)

    @allure.title("Поиск по запросу: telegram возвращает результаты")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("search", "results", "positive")
    def test_search_telegram_has_results(self):
        query = "telegram"
        HomePage().open().open_search()
        SearchPage().should_have_input().type_query(query).submit().should_have_results()

    @allure.title("Пустой поиск показывает подсказки")
    @allure.severity(allure.severity_level.MINOR)
    @allure.tag("search", "empty")
    def test_empty_search(self):
        HomePage().open().open_search()
        SearchPage().should_have_input().submit().should_have_suggestions()

    @allure.title("Поиск по несуществующему запросу не возвращает результатов")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("search", "negative", "not_found")
    def test_search_non_existing_query(self):
        query = "qwerty123456_not_found"
        HomePage().open().open_search()
        SearchPage().should_have_input().type_query(query).submit().should_have_no_results()

    @allure.title("Очистка поля поиска")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("search", "clear")
    def test_clear_search_input(self):
        query = "telegram"
        HomePage().open().open_search()
        SearchPage().should_have_input().type_query(query).clear_query()

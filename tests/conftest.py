import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import allure_attach


def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default=None)


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    load_dotenv()

    base_url = request.config.getoption("--base-url") or os.getenv("BASE_URL", "https://www.rustore.ru")
    browser_version = os.getenv("BROWSER_VERSION")

    window_width = int(os.getenv("WINDOW_WIDTH", 1920))
    window_height = int(os.getenv("WINDOW_HEIGHT", 1080))

    selenoid_url = os.getenv("SELENOID_URL")

    options = Options()
    options.set_capability("browserName", "chrome")

    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

    if browser_version:
        options.set_capability("browserVersion", browser_version)

    options.add_argument(f"--window-size={window_width},{window_height}")

    driver = None
    session_id = None

    if selenoid_url:
        options.set_capability(
            "selenoid:options",
            {
                "enableVNC": True,
                "enableVideo": True,
                "enableLog": True,
            },
        )

        driver = webdriver.Remote(
            command_executor=selenoid_url,
            options=options,
        )
        session_id = driver.session_id
    else:
        driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.base_url = base_url
    browser.config.timeout = 15

    yield

    allure_attach.add_screenshot(driver)
    allure_attach.add_logs(driver)
    allure_attach.add_html(driver)

    if selenoid_url and session_id:
        selenoid_base_url = os.getenv("SELENOID_BASE_URL", "http://localhost:4444")
        allure_attach.add_video(session_id, selenoid_base_url)

    driver.quit()

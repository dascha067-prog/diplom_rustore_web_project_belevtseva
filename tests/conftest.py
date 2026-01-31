import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import allure_attach

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    user = os.getenv("SELENOID_USER")
    password = os.getenv("SELENOID_PASS")
    host = os.getenv("SELENOID_HOST")
    browser_version = os.getenv("BROWSER_VERSION")

    selenoid_url = f"https://{user}:{password}@{host}/wd/hub"

    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", browser_version)
    options.set_capability("selenoid:options", {"enableVNC": True, "enableVideo": True})

    driver = webdriver.Remote(command_executor=selenoid_url, options=options)

    browser.config.driver = driver
    browser.config.base_url = os.getenv("BASE_URL")
    browser.config.window_width = int(os.getenv("WINDOW_WIDTH", 1920))
    browser.config.window_height = int(os.getenv("WINDOW_HEIGHT", 1080))
    browser.config.timeout = 10

    yield

    allure_attach.add_screenshot(driver)
    allure_attach.add_logs(driver)
    allure_attach.add_html(driver)
    allure_attach.add_video(driver.session_id, host)

    driver.quit()

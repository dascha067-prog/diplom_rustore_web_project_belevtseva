import os

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = "https://www.rustore.ru"
    browser.config.timeout = 10

    selenoid_url = os.getenv("SELENOID_URL")

    if selenoid_url:
        options = Options()
        options.add_argument("--disable-dev-shm-usage")

        browser.config.driver = webdriver.Remote(
            command_executor=selenoid_url,
            options=options
        )
    else:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        browser.config.driver = webdriver.Chrome(options=options)

    yield

    browser.quit()

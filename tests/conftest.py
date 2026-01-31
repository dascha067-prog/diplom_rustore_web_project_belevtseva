# import os
#
# import pytest
# from selene import browser
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# @pytest.fixture(scope="function", autouse=True)
# def browser_management():
#     browser.config.base_url = "https://www.rustore.ru"
#     browser.config.timeout = 10
#
#     selenoid_url = os.getenv("SELENOID_URL")
#
#     if selenoid_url:
#         options = Options()
#         options.add_argument("--disable-dev-shm-usage")
#
#         browser.config.driver = webdriver.Remote(
#             command_executor=selenoid_url,
#             options=options
#         )
#     else:
#         options = Options()
#         options.add_argument("--headless=new")
#         options.add_argument("--disable-gpu")
#         options.add_argument("--window-size=1920,1080")
#
#         browser.config.driver = webdriver.Chrome(options=options)
#
#     yield
#
#     browser.quit()

# import os
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from dotenv import load_dotenv
# from utils import allure_attach
#
# # Загружаем .env
# load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
#
#
# @pytest.fixture(scope='function')
# def setup_browser():
#     user = os.getenv("SELENOID_USER")
#     password = os.getenv("SELENOID_PASS")
#     host = os.getenv("SELENOID_HOST")
#     browser_version = os.getenv("BROWSER_VERSION")
#
#     selenoid_url = f"https://{user}:{password}@{host}/wd/hub"
#
#     options = Options()
#     options.set_capability("browserName", "chrome")
#     options.set_capability("browserVersion", browser_version)
#     options.set_capability("selenoid:options", {
#         "enableVNC": True,
#         "enableVideo": True
#     })
#
#     driver = webdriver.Remote(
#         command_executor=selenoid_url,
#         options=options
#     )
#
#     yield driver
#
#     # Allure Attachments
#     allure_attach.add_screenshot(driver)
#     allure_attach.add_logs(driver)
#     allure_attach.add_html(driver)
#     allure_attach.add_video(driver)
#
#     driver.quit()
# import os
#
# import pytest
# from dotenv import load_dotenv
# from selene import browser
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# from utils import allure_attach
#
# # Загружаем .env (Jenkins его создаёт сам)
# load_dotenv()
#
#
# @pytest.fixture(scope='function', autouse=True)
# def setup_browser():
#     user = os.getenv("SELENOID_USER")
#     password = os.getenv("SELENOID_PASS")
#     host = os.getenv("SELENOID_HOST")
#     browser_version = os.getenv("BROWSER_VERSION")
#
#     selenoid_url = f"https://{user}:{password}@{host}/wd/hub"
#
#     options = Options()
#     options.set_capability("browserName", "chrome")
#     options.set_capability("browserVersion", browser_version)
#     options.set_capability(
#         "selenoid:options",
#         {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     )
#
#     driver = webdriver.Remote(
#         command_executor=selenoid_url,
#         options=options
#     )
#
#     browser.config.driver = driver
#     browser.config.base_url = os.getenv("BASE_URL")
#     browser.config.window_width = int(os.getenv("WINDOW_WIDTH", 1920))
#     browser.config.window_height = int(os.getenv("WINDOW_HEIGHT", 1080))
#     browser.config.timeout = 10
#
#     yield
#
#     allure_attach.add_screenshot(driver)
#     allure_attach.add_logs(driver)
#     allure_attach.add_html(driver)
#     allure_attach.add_video(driver)
#
#     driver.quit()


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

    # attachments — передаём именно WebDriver
    allure_attach.add_screenshot(driver)
    allure_attach.add_logs(driver)
    allure_attach.add_html(driver)
    allure_attach.add_video(driver.session_id, host)

    driver.quit()

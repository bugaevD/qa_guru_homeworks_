import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=options)
    yield driver

    driver.quit()


def test_selenium_web(driver):
    url = "https://www.selenium.dev/"
    driver.get(url)
    assert driver.title == "Selenium"
    assert driver.current_url == url


def test_google(driver):
    url = "https://www.google.com/"
    driver.get(url)
    assert driver.title == "Google"
    assert driver.current_url == url


def test_github(driver):
    url = "https://github.com/"
    driver.get(url)
    assert driver.title == "GitHub · Change is constant. GitHub keeps you ahead. · GitHub · GitHub"
    assert driver.current_url == url

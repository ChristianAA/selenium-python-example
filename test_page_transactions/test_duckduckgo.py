import pytest
from test_page_transactions.pages import home_page
from selenium import webdriver
from guara import it
from guara import setup
from guara.transaction import Application


@pytest.fixture
def setup_app():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    app = Application(webdriver.Chrome(options=options))
    app.at(
        setup.OpenApp,
        url="https://duckduckgo.com/",
    ).asserts(it.Contains, "DuckDuckGo")
    yield app
    app.at(setup.CloseApp)


def test_search_selenium(setup_app):
    duckduckgo: Application = setup_app
    duckduckgo.at(home_page.Search, for_text="Selenium").asserts(it.IsEqualTo, "All")

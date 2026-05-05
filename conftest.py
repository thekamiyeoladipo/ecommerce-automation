import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
        

@pytest.fixture(scope="session")
def test_email():
    return os.getenv("TEST_EMAIL")

@pytest.fixture(scope="session")
def test_password():
    return os.getenv("TEST_PASSWORD")
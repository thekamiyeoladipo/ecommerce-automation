import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture(scope="session")
def test_email():
    return os.getenv("TEST_EMAIL")

@pytest.fixture(scope="session")
def test_password():
    return os.getenv("TEST_PASSWORD")

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.set_default_timeout(15000)

        # Block ads and trackers
        def block_ads(route, request):
            blocked_domains = [
                "doubleclick.net",
                "googlesyndication.com",
                "googletagmanager.com",
                "googletagservices.com",
                "google-analytics.com",
                "adservice.google.com",
            ]
            if any(domain in request.url for domain in blocked_domains):
                route.abort()
            else:
                route.continue_()

        context.route("**/*", block_ads)

        page = context.new_page()
        yield page
        context.close()
        browser.close()
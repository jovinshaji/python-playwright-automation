# conftest.py
import pytest
from pages.signup_page import SignupPage

# `page` fixture is provided by pytest-playwright
@pytest.fixture
def signup_page(page):
    """Return an instance of SignupPage that uses the Playwright page fixture."""
    return SignupPage(page)

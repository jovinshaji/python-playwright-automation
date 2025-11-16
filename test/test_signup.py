import pytest
from playwright.sync_api import Page
from pages.signup_page import SignupPage

@pytest.fixture
def signup(page: Page) -> SignupPage:
    return SignupPage(page)

def test_has_title_and_fill_step1(signup: SignupPage):
    signup.goto_signin()
    signup.assert_signin_title()
    signup.goto_signup()
    #generated_email = 
    signup.fill_step1_with_unique_credentials()

    #assert SignupPage.locator(signup.email_input).input_value() == generated_email

def test_get_started_link(signup: SignupPage):
    signup.goto_signin()
    '''signup.assert_signin_title()
    signup.goto_signin()
    signup.fill_step1_with_unique_credentials()

    signup.page.goto("https://playwright.dev/")
'''


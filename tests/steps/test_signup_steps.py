# tests/steps/test_signup_steps.py

from pytest_bdd import scenarios, given, when, then, parsers
from pages.signup_page import SignupPage

# automatically discover scenarios in this file's feature directory
scenarios('../features/signup.feature')

@given("I am on the sign in page")
def i_am_on_signin_page(signup_page: SignupPage):
    signup_page.goto_signin()
    signup_page.assert_signin_title()

@when("I navigate to sign up")
def i_navigate_to_signup(signup_page: SignupPage):
    signup_page.goto_signup()

@when("I fill step1 with unique credentials")
def i_fill_step1_with_unique_credentials(signup_page: SignupPage, request):
    # store email in pytest request.config or request.node for later assertion
    #generated_email = 
    signup_page.fill_step1_with_unique_credentials()
    # attach to the request.node so Then step can access it
    #request.node.generated_email = generated_email
#last test
@then("the email field should contain the generated email")
def email_field_contains_generated_email(signup_page: SignupPage, request):
    generated_email = getattr(request.node, "generated_email", None)
    assert generated_email is not None, "Generated email missing from context"
    # assert the page input has the value
    value = signup_page.page.locator(signup_page.email_input).input_value()
    assert value == generated_email, f"Email input value {value} != expected {generated_email}"

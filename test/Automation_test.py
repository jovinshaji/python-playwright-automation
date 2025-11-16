import time
import pytest
from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError

# Helper function to navigate to the company info page (Step 3 of sign-up)
def go_to_company_info_page(page: Page):
    page.goto("https://circula-qa-challenge.vercel.app/users/sign_in")

    # Wait a short time for page elements to load
    page.wait_for_timeout(300)

    # Handle cookie consent popup if visible
    accept_button = page.get_by_test_id("uc-accept-all-button")
    try:
        accept_button.wait_for(state="visible", timeout=4000)
        accept_button.click()
    except PlaywrightTimeoutError:
        # Popup did not appear, proceed normally
        pass

    # Navigate to sign-up page
    page.click('a[href="/users/sign_up"]')

    # Fill Step 1 details with a unique email and password
    timestamp = int(time.time() * 1000)
    email = f"QATest{timestamp}@test.com"
    page.locator("//input[@id='textfield-:Rqikmm:']").fill(email)
    page.locator("//input[@id='textfield-:R3aikmm:']").fill("testpassword1")
    page.wait_for_timeout(3000)  # Optional wait for elements to load

    # If cookie popup appears again, accept it
    try:
        if accept_button.is_visible():
            accept_button.click()
    except Exception:
        # If element is detached or not present, ignore
        pass

    # Agree to terms and optionally subscribe
    page.locator('label:has-text("I agree to the") input[type="checkbox"]').check(force=True)
    page.locator("label").filter(has_text="I'm happy to get occasional").click()

    # Submit Step 1 form
    page.locator("//button[normalize-space()='Try for free']").click()

    # Fill Step 2 details (contact info)
    page.locator("//input[@id='textfield-:r0:']").fill("Jovinsha")
    page.locator("//input[@id='textfield-:r1:']").fill("Shaji")
    page.locator('input[name="phoneNumber"]').fill("123456789")

    # Proceed to Step 3 (Company info)
    page.locator("//button[normalize-space()='Next step']").click()


# Helper to fill company name and prepare country dropdown
def enter_details_till_country_dropdown(page: Page):
    page.get_by_role("textbox", name="Company name").fill("QA test")

    dropdown_input = page._

import re
import time
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://circula-qa-challenge.vercel.app/users/sign_in")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Signin - Circula"))

     # Navigate to sign-up page
    page.click('a[href="/users/sign_up"]')

      # Fill Step 1 details with a unique email and password
    timestamp = int(time.time() * 1000)
    email = f"QATest{timestamp}@test.com"
    page.locator("//input[@id='textfield-:Rqikmm:']").fill(email)
    page.locator("//input[@id='textfield-:R3aikmm:']").fill("testpassword1")
    page.wait_for_timeout(3000)  # Optional wait for elements to load

def test_get_started_link(page: Page):
    test_has_title(page)
    page.goto("https://playwright.dev/")
"""
    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

    """
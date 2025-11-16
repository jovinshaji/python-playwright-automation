import re
import time 
from playwright.sync_api import Page, expect

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.sign_in_url = "https://circula-qa-challenge.vercel.app/users/sign_in"
        self.sign_up_url = 'a[href="/users/sign_up"]'
        self.email_input = "//input[@id='textfield-:Rqikmm:']"
        self.password_input = "//input[@id='textfield-:R3aikmm:']"

    def goto_signin(self):
        self.page.goto(self.sign_in_url)

    def assert_signin_title(self):
        expect(self.page).to_have_title(re.compile("Signin - Circula"))

    def goto_signup(self):
         self.page.click(self.sign_up_url)

    def fill_step1_with_unique_credentials(self, password: str = "testpassword1"):
        timestamp = int(time.time() * 1000)
        email = f"QATest{timestamp}@test.com"
        self.page.locator(self.email_input).fill(email)
        self.page.locator(self.password_input).fill(password)
        self.page.wait_for_timeout(1000)
        return email
    
    

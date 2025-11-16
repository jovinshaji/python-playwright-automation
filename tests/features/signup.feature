Feature: Signup flow
  As a user
  I want to fill signup step 1 with unique credentials
  So that I can continue with registration

  Scenario: Fill signup step 1
    Given I am on the sign in page
    When I navigate to sign up
    And I fill step1 with unique credentials
    Then the email field should contain the generated email
# features/register.feature

Feature: User Registration
  As a new user, I want to register on the website

  Scenario: Successful registration
    Given I am on the registration page
    When I enter valid registration details
    Then I should be registered and redirected to the login page

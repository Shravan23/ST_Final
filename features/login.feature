Feature: Login
  As a user, I want to log in to the website

  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials
    Then I should be redirected to the profile page

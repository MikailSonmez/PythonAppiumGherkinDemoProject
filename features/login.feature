Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given I am on the login screen
    When I enter valid credentials
    Then I should see the dashboard screen
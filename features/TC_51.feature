@tc_51
Feature: Verify Navigation to Landing Page

  Scenario: Verify the navigation to the landing page
    Given I am on the application page
    When I navigate back to the landing page
    Then I should successfully return to the landing page

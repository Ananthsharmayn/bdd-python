@tc_36
Feature: Validate behavior for entering a LinkedIn profile URL

  Scenario: Verify behavior for entering a valid LinkedIn profile URL
    Given I am on the application page
    When I wait for the LinkedIn input field to be visible
    And I enter a valid LinkedIn profile URL in the input field
    Then I should verify that the entered LinkedIn URL is accepted
    And I close the browser

@tc_34
Feature: Validate email input field behavior for a valid email address

  Scenario: Verify behavior for entering a valid email address
    Given I am on the application page
    When I wait for the email field to be clickable
    And I enter a valid email address in the email field
    Then I should verify that the entered email address is accepted
    And I close the browser




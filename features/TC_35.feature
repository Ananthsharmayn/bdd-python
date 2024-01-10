@tc_35
Feature: Validate email input field behavior for a valid email address

  Scenario: Verify behavior for entering a valid email address
    Given I am on the application page
    When I wait for the email field to be clickable
    And I clear the email input field
    And I enter an invalid email address in the email field
    And I click outside the email input box to trigger validation
    Then I should wait for the error message to appear
    And I should verify that the invalid email address is not accepted
    And I close the browser



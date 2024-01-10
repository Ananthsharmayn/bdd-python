@tc_31
Feature: Validating phone number input field

  Scenario: Verify validation for a valid phone number
    Given I am on the Career landing page
    When I wait for the job listings to load
    And I scroll to the job lists section and view them
    And I click the "Apply" button for a job
    Then I enter a valid phone number
    Then I should see the validation for the phone number input field
    And I close the browser


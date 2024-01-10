@tc_32
Feature: Validate phone number input field limitation

  Scenario: Verify the limitation of the phone number input field
    Given I am on the Career landing page
    When I wait for the job listings to load
    And I scroll to the job lists section and view them
    And I click the "Apply" button for a job
    Then I enter a valid phone number
    Then I should observe the phone number input value is truncated to 10 digits
    And I close the browser


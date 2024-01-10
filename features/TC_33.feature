@tc_33
Feature: Validate input field behavior for invalid phone numbers

  Scenario: Verify behavior for entering invalid phone numbers
    Given I am on the Career landing page
    When I wait for the job listings to load
    And I scroll to the job lists section and view them
    And I click the "Apply" button for a job
    When I enter invalid phone numbers in the phone number field
    Then I should observe the field value becomes empty after invalid input
    And I close the browser


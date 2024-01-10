@tc_28
Feature: Check if the input fields does not accept any empty input

  Scenario: Verify that all the input fields should not accept empty input
    Given I am on the Career landing page
    When I wait for the job listings to load
    And I scroll to the job lists section and view them
    And I click the "Apply" button for a job
    Then I enter all the fields
    Then I should see the alert message displayed
    And I close the browser

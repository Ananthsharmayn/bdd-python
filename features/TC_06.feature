@tc_06
Feature: Check if all the jobs are displayed in All departments

  Scenario: Verify the display of jobs in All departments
    Given I am on the Career landing page
    When I wait for the job listings to load
    And I scroll to the job lists section and view them
    Then I should see all the job listings in the "All Departments" category
    And I close the browser

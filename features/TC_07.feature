@tc_07
Feature: Check if clicking the "Apply" button opens a new page

  Scenario: Verify the opening of a new page when the "Apply" button is clicked
    Given I am on the Career landing page
    When I wait for the job listings to load
    And I scroll to the job lists section and view them
    And I click the "Apply" button for a job
    Then I should see a new page for filling job application details
    And I close the browser

@tc_64
Feature: Verify Elements on Job Description Page

  Scenario: Verify elements on the job description page
    Given I am on the Career landing page
    When I wait for the job listings to load
    And I scroll to the job lists section and view them
    And I click the "Apply" button for a job
    Then I should see a new page for filling job application details
    And I should see the job form
    And I should see the job title
    And I should see the job experience
    And I should see the job description

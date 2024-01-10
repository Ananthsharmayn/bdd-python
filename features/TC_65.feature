@tc_65
Feature: Verify 'Read More' Button Functionality

  Scenario: Clicking 'Read More' button expands job description
    Given I am on the Career landing page
    When I scroll to the job lists section and view them
    And I click the "Apply" button for a job
    Then I should see a new page for filling job application details
    Then I should see the job description page
    When I click the "Read More" button
    Then the job description should expand

@tc_56
Feature: Verify job listings under the 'Design team' department

  Scenario: Check if jobs from the 'Design team' are displayed
    Given I am on the Career landing page
    When I click on the "Discover Jobs" link
    Then I should land on the job discovery page
    Then I select the "Design team" department from the dropdown
    And I should see jobs listed under the "Design team" department

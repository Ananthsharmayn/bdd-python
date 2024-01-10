@tc_55
Feature: Verify job listings on the Career landing page

  Scenario: Check if job listings are displayed by default
    Given I am on the Career landing page
    When I click on the "Discover Jobs" link
    Then I should land on the job discovery page
    Then I should see the list of jobs

@tc_58
Feature: View Jobs in the Software Department

  Scenario: Check job listings in the Software Department
    Given I am on the Career landing page
    When I click on the "Discover Jobs" link
    Then I should land on the job discovery page
    Then I select the "Software Department" from the departments dropdown
    And I should see job listings displayed for the "Software Department"
@tc_57
Feature: Verify Hardware Department Jobs

  Scenario: View jobs in the Hardware Department
    Given I am on the Career landing page
    When I click on the "Discover Jobs" link
    Then I should land on the job discovery page
    Then I select the "Hardware Department" from the departments dropdown
    And I should see jobs listed under the "Hardware Department"

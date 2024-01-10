@tc_52 
Feature: Verify elements on the job discovery page

  Scenario: Verify elements on the job discovery page
    Given I am on the Career landing page
    When I click on the "Discover Jobs" link
    Then I should land on the job discovery page
    And I should see the available departments
    And I should see the search option
    And I should see the "Apply" buttons

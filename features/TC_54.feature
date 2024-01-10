@tc_54
Feature: Search for an invalid job query and verify no job listings are displayed

  Scenario: Search for an invalid job query and verify no job listings
    Given I am on the Career landing page
    When I click on the "Discover Jobs" link
    Then I should land on the job discovery page
    And I should see the search option
    When I search for an invalid job query "InvalidJobQuery123"
    Then I should not find any job listings

@tc_53
Feature: Search for a job and verify its presence in the search results

  Scenario: Search for a job and verify its presence
    Given I am on the Career landing page
    When I click on the "Discover Jobs" link
    Then I should land on the job discovery page
    And I should see the search option
    When I search for a job with keyword "Ruby Developer"
    Then I should find the job "Ruby Developer" in the search results

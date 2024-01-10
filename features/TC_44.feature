@tc_44 
Feature: Search with Unlikely Keyword

  Scenario: Searching with an unlikely keyword
    Given I am on the Career landing page
    When I enter an unlikely keyword in the search input field
    Then I should see the 'Uh oh! No results found' message indicating no jobs were found
    And I close the browser

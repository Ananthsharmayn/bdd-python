@tc_45 
Feature: Search for Invalid Keyword

  Scenario: Search for an invalid keyword
    Given I am on the Career landing page
    When I enter an invalid keyword in the search input field
    Then I should see the 'No results found' message
    And I close the browser

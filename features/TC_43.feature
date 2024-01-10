@tc_43 
Feature: Search for job listings on the website

  Scenario: Perform a job search
    Given I am on the Career landing page
    When I search for the keyword "developer"
    Then I should see job listings displayed
    And I close the browser

@tc_05
Feature: Check if all the texts are displayed with job titles

  Scenario: Verify the presence of various job-related texts
    Given I am on the Career landing page
    Then I should see all the following texts with job titles
    And I close the browser
    
      | Level          |
      | Experience      |
      | Address         |
      | Job Type        |

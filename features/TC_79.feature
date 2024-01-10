@tc_79
Feature: Verify text content on the Career landing page

  Scenario: Verify text content
    Given I am on the Career landing page
    Then I wait for the web page to fully load
    And I verify each texts
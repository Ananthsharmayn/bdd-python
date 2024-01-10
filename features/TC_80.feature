@tc_80
Feature: Verify text content on the Career landing page

  Scenario: Verify text content and description
    Given I am on the Career landing page
    Then I wait for the web page to fully load
    And I verify the expected text
    And I verify the description text
    And I close the browser

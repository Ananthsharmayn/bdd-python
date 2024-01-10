@tc_04
Feature: Check if "Latest Openings" text is displayed

  Scenario: Verify the display of "Latest Openings" text
    Given I am on the Career landing page
    Then I should see the "Latest Openings" text displayed
    And I close the browser

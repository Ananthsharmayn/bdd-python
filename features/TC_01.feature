@tc_01
Feature: Check if all the latest openings are displayed

Scenario: Verify the display of the latest job openings
    Given I am on the Career landing page
    When I wait for the job listings to load
    Then I should see all the latest job openings
    And I close the browser



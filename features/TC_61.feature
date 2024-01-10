@tc_61
Feature: Verify Show Description on Hover

  Scenario: Verify the display of "Show Description" on hovering over a job title
    Given I am on the Career landing page
    When I click on the "Discover Jobs" link
    Then I should land on the job discovery page
    # Then I should see the "Ruby Developer" job title displayed
    When I hover over the "Ruby Developer" job title
    Then I should see the "Show Description" option displayed

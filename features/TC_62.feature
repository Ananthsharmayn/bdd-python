@tc_62
Feature: Verify Job Description Window

  Scenario: Verify the display of elements in the job description window
    Given I am on the Career landing page
    When I click on the "Discover Jobs" link
    When I hover over the "Ruby Developer" job title
    And I click on the "Show Description" link
    Then I should see the job description window
    And I should see the job description text
    And I should see the job meta data
    And I should see the apply button

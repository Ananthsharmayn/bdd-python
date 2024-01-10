@tc_63 
Feature: Navigate to Job Apply Page

  Scenario: Navigating to the job apply page from the job description
    Given I am on the Career landing page
    When I click on the "Discover Jobs" link
    When I hover over the "Ruby Developer" job title
    And I click on the "Show Description" link
    Then I should see the job description window
    And I should see the job description text
    And I should see the job meta data
    And I should see the apply button
    When I click on the "Apply" button within the description window
    Then I should navigate to the job apply page
@tc_60
Feature: Verify How We Hire Text and Elements

  Scenario: Check the presence of "How We Hire at Simple!!!!" text and related elements
    Given I am on the Career landing page
    Then I should see the "How We Hire at Simple!!!!" text displayed
    And all elements below "How We Hire at Simple!!!!" should be visible

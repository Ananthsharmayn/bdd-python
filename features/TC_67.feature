@tc_67 
Feature: Verify presence of footer elements

  Scenario: Check for a specific element in the footer
    Given I am on the Career landing page
    When I scroll down to view the footer
    Then I should verify the presence of "Sign in" in the footer

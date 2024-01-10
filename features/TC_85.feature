@tc_85 
Feature: Fill Job Application and Verify How We Hire Button

  Scenario: Fill job application and verify How We Hire button functionality
    Given I am on the application page
    When I fill in the application form with valid details
    And I click the submit button
    And I wait for the application success page to load
    And I click the How We Hire button
    Then I should verify the functionality of the How We Hire button

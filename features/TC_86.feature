@tc_86 
Feature: Verify Job Title on Job Application and Application Success Page

  Scenario: Verify Job Title Consistency
    Given I am on the application page
    When I fill in the application form with valid details
    Then I should verify the job title consistency on the application success page

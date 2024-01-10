@tc_84
Feature: Verify Job Application Submission Without Details

  Scenario: Fill and submit job application without providing details
    Given I am on the application page
    When I fill in the application form without details
    Then I should see an alert indicating the error
    And I should not see the application success message

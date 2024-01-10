@tc_83
Feature: Fill Job Application Form and Verify Submission

  Scenario: Fill and submit a job application
    Given I am on the application page
    When I fill in the application form with valid details
    And I upload a resume
    And I submit the application
    Then I should see a success message confirming the submission


@tc_81 
Feature: Job Application Form Validation

  Scenario: Applying for a job and checking the application form
    Given I am on the Career landing page
    When I scroll to the job lists section and view them
    And I click the "Apply" button for a job
    Then I should see a new page for filling job application details
    And I check if all input fields are empty
    And I check if the submit button color is grey

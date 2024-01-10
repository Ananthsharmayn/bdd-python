@tc_29
Feature: Verify input fields do not accept invalid input

  Scenario: Verify the validation of name input field
    Given I am on the Career landing page
    When I wait for the job listings to load
    And I scroll to the job lists section and view them
    And I click the "Apply" button for a job
    Then I enter a valid name with alphabetic characters only
    Then I should see the validation for the name input field
    And I close the browser

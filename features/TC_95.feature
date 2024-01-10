@tc_95 
Feature: TC_95 - Verify the Apply link for a HR Specialist job in the HR Department

  Scenario Outline: Verify that a new page is opened when the apply link of a job is clicked
    Given I am on the Career landing page
    When I scroll to the job lists section and view them
    And I click on the dropdown and select "<department>"
    Then I should see job items listed under the "<department>"
    And I click the Apply button for the "<field_name>" job
    Then I should see a new page for filling job application details

    Examples:
      | field_name        | department|
      | HR Specialist  | HR department |

@tc_19
Feature: TC_19 - Check "Apply" button functionality for UI/UX Designer job in Design team

  Scenario Outline: Verify "Apply" button functionality for UI/UX Designer job
    Given I am on the Career landing page
    When I scroll to the job lists section and view them    
    And I click on the dropdown and select "Design team"
    Then I should see job items listed under the "Design team"
    And I click the Apply button for the "<job role>" job
    Then I should see a new page for filling job application details
    And I close the browser

    Examples:
      | job role      |
      | UI/UX Designer |
@tc_11 
Feature: TC_11 - Check "Apply" button functionality for Web Developer job in Software Department

  Scenario Outline: Verify "Apply" button functionality for Web Developer job
    Given I am on the Career landing page
    When I scroll to the job lists section and view them
    And I click on the dropdown and select "Software Department"
    Then I should see job items listed under the "Software Department"
    And I click the Apply button for the "<job role>" job
    Then I should see a new page for filling job application details
    And I close the browser

    Examples:
      | job role      |
      | Web Developer |

@tc_15
Feature: TC_15 - Check if there are job items under the HR Department

  Scenario Outline: Verify the presence of job items under the HR Department
    Given I am on the Career landing page
    When I scroll to the job lists section and view them    
    And I click on the dropdown and select "<department>"
    Then I should see job items listed under the "<department>"
    And I close the browser

   Examples:
      | department     |
      | HR department  |
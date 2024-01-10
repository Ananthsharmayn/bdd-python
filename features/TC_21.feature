@tc_21
Feature: TC_21 - Check if there are job items under the Hardware Department

  Scenario Outline: Verify the presence of job items under the Hardware Department
    Given I am on the Career landing page
    When I scroll to the job lists section and view them
    And I click on the dropdown and select "<department>"
    Then I should see job items listed under the "<department>"
    And I close the browser

   Examples:
      | department     |
      | Hardware Department  |
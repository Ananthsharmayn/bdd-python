@tc_22
Feature: TC_22 - Check "Apply" button functionality for Vehicle designer job in Hardware Department

  Scenario Outline: Verify "Apply" button functionality for Vehicle designer job
    Given I am on the Career landing page
    When I scroll to the job lists section and view them
    And I click on the dropdown and select "Hardware Department"
    Then I should see job items listed under the "Hardware Department"
    And I click the Apply button for the "<job role>" job
    Then I should see a new page for filling job application details
    And I close the browser

    Examples:
      | job role      |
      | Vehicle designer |
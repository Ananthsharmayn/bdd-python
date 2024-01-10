@tc_40
Feature: Clicking the 'Submit' button on the application page

  Scenario: Clicking the 'Submit' button
    Given I am on the application page
    When I wait for the 'Submit' button to be clickable
    And I click the 'Submit' button
    Then I should receive a confirmation of successful click
    And I close the browser

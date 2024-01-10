@tc_42 
Feature: Verify the behavior of the submission process

  Scenario: Submit without filling the required fields
    Given I am on the application page
    When I click the "Submit" button without filling the required fields
    Then I should see an alert message indicating missing fields
    And I close the browser

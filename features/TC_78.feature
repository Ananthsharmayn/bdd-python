@tc_78
Feature: Verify texts on the web page

  Scenario: Verify specific texts on the web page
    Given I am on the Career landing page
    Then I wait for the web page to fully load
    And I verify each text
@tc_38
Feature: Uploading a file on the application page

  Scenario: Uploading a document file
    Given I am on the application page
    When I wait for the file upload element to be visible
    And I upload a document file
    Then I should see a success message confirming the file upload
    And I close the browser

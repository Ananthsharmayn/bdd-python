@tc_49
Feature: Copy Job Listing Link

  Scenario: Verify the copying of the job listing link
    Given I am on the application page
    When I click the "Copy" button
    Then I should see the "Link Copied!" message
    And the message should contain the job listing link

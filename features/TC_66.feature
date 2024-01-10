@tc_66 
Feature: Verify navigation and text on new job application page

  Scenario: Clicking the Apply button navigates to a new page with expected text
    Given I am on the Career landing page
    When I scroll to the job lists section and view them
    And I click the "Apply" button for a job
    Then I should see a new page for filling job application details
    # And I should see the expected texts on the new page

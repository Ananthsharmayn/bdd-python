@tc_96
Feature: Verify fields displayed after clicking the Apply button for HR Specialist

  Scenario Outline: Verify fields displayed after clicking Apply button for "<Field Name>"
    Given I am on the Career landing page
    When I scroll to the job lists section and view them
    And I click on the dropdown and select "HR department"
    And I wait for the job listings to load
    Then I click the Apply button for the "HR Specialist" job
    Then I should see a new page for filling job application details
    And I should see "<Field Name>" displayed

    Examples:
      | Field Name         |
      | HR Specialist     |
      # | Department         |
      # | Full Name:         |
      # | Phone Number:      |
      # | Email ID:          |
      # | LinkedIn Profile:  |
      # | Resume/ CV         |
      # | Submit             |

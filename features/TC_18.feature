@tc_18
Feature: Verify fields displayed after clicking the Apply button for figma handler

  Scenario Outline: Verify fields displayed after clicking Apply button for "<Field Name>"
    Given I am on the Career landing page
    When I wait for the job listings to load
    And I scroll to the job lists section and view them    
    And I click on the dropdown and select "Design team"
    And I wait for the job listings to load    
    Then I click the Apply button for the "figma handler" job
    Then I should see a new page for filling job application details
    And I should see "<Field Name>" displayed
    And I close the browser

    Examples:
      | Field Name         |
      | Figma handler      |
      # | Department         |
      # | Full Name:         |
      # | Phone Number:      |
      # | Email ID:          |
      # | LinkedIn Profile:  |
      # | Resume/ CV         |
      # | Submit             |

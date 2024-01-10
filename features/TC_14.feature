@tc_14
Feature: Verify fields displayed after clicking the Apply button for Python Developer

  Scenario Outline: Verify fields displayed after clicking Apply button for "<Field Name>"
    Given I am on the Career landing page
    When I scroll to the job lists section and view them    
    And I click on the dropdown and select "Software Department"
    And I wait for the job listings to load
    Then I click the Apply button for the "Python Developer" job
    Then I should see a new page for filling job application details
    And I should see "<Field Name>" displayed
    And I close the browser

    Examples:
      | Field Name         |
      | Python Developer   |
      # | Department         |
      # | Full Name:         |
      # | Phone Number:      |
      # | Email ID:          |
      # | LinkedIn Profile:  |
      # | Resume/ CV         |
      # | Submit             |

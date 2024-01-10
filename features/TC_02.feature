@tc_02
Feature: Check if logo and Careers text are displayed

    Scenario: Verify the display of the logo and text
        Given I am on the Career landing page
        When I wait for the logo and text to be displayed
        Then I should see the logo and text displayed
        And I close the browser
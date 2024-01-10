# @tc_47
# Feature: Check Dropdown Menu Options

#   Scenario: Verify all department options in the dropdown menu
#     Given I am on the Career landing page
#     When I wait for the job listings to load
#     When I open the "AllDepartments" dropdown menu
#     Then I should see the following department options:
#       | AllDepartments      |
#       | All Departments     |
#       | Design team          |
#       | Hardware Department  |
#       | Software Department  |
#       | HR department        |

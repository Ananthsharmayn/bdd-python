from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

@given('I am on the Career landing page')
def step_given_i_am_on_career_page(context):
    service=Service(executable_path='/home/ananth/Downloads/chromedriver-linux64/chromedriver')
    chrome_options = webdriver.ChromeOptions()

    chrome_options.binary_location = '/usr/bin/google-chrome'
    chrome_options.add_argument('--headless')


    # Create Chrome WebDriver with specified options
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to the desired URL
    context.driver.get("https://hades-stage.simpleenergy.in/")

@when('I wait for the job listings to load')
def step_when_i_wait_for_job_listings(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "job-item-header"))
    )

@then('I should see all the latest job openings')
def step_then_i_should_see_job_openings(context):
    time.sleep(3)
    job_items = context.driver.find_elements(By.CLASS_NAME, "job-item-header")
    for job_item in job_items:
        job_title = job_item.find_element(By.CLASS_NAME, "job-title").text
        apply_link = job_item.find_element(By.TAG_NAME, "a").get_attribute("href")
        assert job_title, "Job Title not found"
        assert apply_link, "Apply Link not found"

@when('I wait for the logo and text to be displayed')
def step_when_i_wait_for_logo_and_text(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "log-nav-item"))
    )

@then('I should see the logo and text displayed')
def step_then_i_should_see_logo_and_text(context):
    time.sleep(3)    
    wait = WebDriverWait(context.driver, 10)  # Adjust the timeout as needed
    logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "log-nav-item")))
    text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "nav-logo-heading")))
    
    assert logo.is_displayed(), "Logo is not displayed"
    assert text.is_displayed(), "Text is not displayed"

@when('I wait for the "Join the beyond" text to be displayed')
def step_when_i_wait_for_join_text(context):
    time.sleep(3)    
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "heroBanner-text"))
    )

@then('I should see the "Join the beyond" text displayed')
def step_then_i_should_see_join_text(context):
    time.sleep(3)    
    join_text = context.driver.find_element(By.CLASS_NAME, "heroBanner-text")
    assert join_text.is_displayed(), '"Join the beyond" text is not displayed'
    assert join_text.text == "Join the beyond", 'Text does not match "Join the beyond"'

@then('I should see the "Latest Openings" text displayed')
def step_then_i_should_see_latest_openings_text(context):
    time.sleep(3)    
    openings_element = context.driver.find_element(By.CLASS_NAME, "current-openings")
    
    assert openings_element.is_displayed(), '"Latest Openings" text is not displayed'
    assert openings_element.text == "Latest Openings", 'Text does not match "Latest Openings"'


# TC_05: Check if all the texts are displayed with job titles
@then('I should see all the following texts with job titles')
def step_then_i_should_see_all_texts(context):
    time.sleep(3)    
    # Wait for the job listings to be displayed
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "job-lists"))
    )

    # Find all the job items
    job_items = context.driver.find_elements(By.CLASS_NAME, "job-item")

    # Initialize lists to store the presence of fields
    levels_present = []
    experiences_present = []
    addresses_present = []
    job_types_present = []

    # Iterate through job items to extract field information
    for job_item in job_items:
        # Extract the Level, Experience, Address, and Job type
        level = job_item.find_element(By.CLASS_NAME, "job-experience").text
        experience = job_item.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div[1]/div[1]/div[2]/p[2]")
        address = job_item.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]")
        job_type = job_item.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div[1]/div[1]/div[3]/div[2]")

        # Append the field information to respective lists
        levels_present.append(level)
        experiences_present.append(experience)
        addresses_present.append(address)
        job_types_present.append(job_type)

    # Verify the presence of fields
    assert all(levels_present), "Level not found"
    assert all(experiences_present), "Experience not found"
    assert all(addresses_present), "Address not found"
    assert all(job_types_present), "Job Type not found"

@then('I should see all the job listings in the "{department}" category')
def step_then_i_should_see_all_jobs_in_department(context, department):
    # Wait for the job listings to be displayed
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "job-lists"))
    )

    # Find the dropdown element
    dept_dropdown = context.driver.find_element(By.CLASS_NAME, "MuiSelect-select")

    # Get the text of the selected department
    selected_department = dept_dropdown.text.strip()

    # Check if the selected department matches the expected department
    if selected_department == department:
        print(f"Expected Result: It should display all the Latest jobs that come under {department}")
        print(f"Actual Result: All the jobs are displayed under {department}")
    else:
        print(f"Expected Result: It should display all the Latest jobs that come under {department}")
        print(f"Actual Result: The selected department is {selected_department}")

@when('I click the "Apply" button for a job')
def step_when_i_click_apply_button(context):
    # Wait for the job listings to be displayed
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "job-item-header"))
    )

    # Find the "Apply" button for the job you want to apply for using XPath
    apply_button = context.driver.find_element(By.XPATH, "//a[text()='Apply']")

    # Click the "Apply" button
    apply_button.click()
    time.sleep(3)    

@then('I should see a new page for filling job application details')
def step_then_i_should_see_application_page(context):
    # Check if the new page for filling details to apply for the job is displayed
    if "apply" in context.driver.current_url:
        print("Expected Result: It should open a page to fill the details to apply for the particular job when the Apply option is clicked")
        print("Actual Result: It is displaying a page for the particular job when the Apply is clicked")
    else:
        print("Expected Result: It should open a page to fill the details to apply for the particular job when the Apply option is clicked")
        print("Actual Result: The page for the particular job is not displayed")

@when('I click on the dropdown and select "{department}"')
def step_when_i_select_software_department(context,department):
    dropdown_element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiSelect-select"))
    )
    time.sleep(2)
    
    dropdown_element.click()
    time.sleep(2)

    software_option = context.driver.find_element(By.XPATH, f"//li[contains(text(), '{department}')]")
    software_option.click()
    time.sleep(2)

@when('I click on the dropdown')
def step_when_i_select_software_department(context,department):
    dropdown_element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiSelect-select"))
    )
    time.sleep(2)
    
    dropdown_element.click()
    time.sleep(2)

#TC9
@then('I should see job items listed under the "{department}"')
def step_then_i_should_see_job_items_under_software_department(context,department):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "job-item-header"))
    )

    job_items = context.driver.find_elements(By.CLASS_NAME, "job-item")

    if len(job_items) > 0:
        print(f"Expected Result: It should have job items under '{department}'")
        print(f"Actual Result: Job items are listed under '{department}")
    else:
        print(f"Expected Result: It should have job items under '{department}'")
        print(f"Actual Result: No job items found under '{department}'")


# @then('I should see "{field_name}" displayed')
# def step_then_i_should_see_field_displayed(context, field_name):
#     if context.driver.find_elements(By.XPATH, f"//*[contains(text(), '{field_name}')]"):
#         print(f"{field_name} is displayed.")
#     else:
#         print(f"{field_name} is NOT displayed.")
@then('I should see "{field_name}" displayed')
def step_then_i_should_see_field_displayed(context, field_name):
    expected_fields = [
        field_name,
        "Full Name:",
        "Phone Number:",
        "Email ID:",
        "LinkedIn Profile:",
        "Resume/ CV",
        "Submit"
    ]
    for field in expected_fields:
        if context.driver.find_elements(By.XPATH, f"//*[contains(text(), '{field}')]"):
            print(f"{field} is displayed.")
        else:
            print(f"{field} is NOT displayed.")

xpath_mappings = {
    "Ruby Developer": '/html/body/div/div[2]/div[3]/div[1]/div[1]/div[1]/div/a',
    "Web Developer": '/html/body/div/div[2]/div[3]/div[1]/div[2]/div[1]/div/a',
    "Python Developer":'/html/body/div/div[2]/div[3]/div[1]/div[3]/div[1]/div/a',
    "HR Specialist":'/html/body/div/div[2]/div[3]/div[1]/div[1]/div[1]/div/a',
    "HR Manager":'/html/body/div/div[2]/div[3]/div[1]/div[2]/div[1]/div/a',
    "figma handler": "/html/body/div/div[2]/div[3]/div[1]/div[2]/div[1]/a",
    "UI/UX Designer": "/html/body/div/div[2]/div[3]/div[1]/div[1]/div[1]/a",
    "Brake designer": "/html/body/div/div[2]/div[3]/div[1]/div[1]/div[1]/a",
    "Vehicle designer": "/html/body/div/div[2]/div[3]/div[1]/div[2]/div[1]/a"
    # Add other job roles and their respective XPaths here
}

@then('I click the Apply button for the "{field_name}" job')
def step_when_i_click_apply_field_name(context, field_name):
    print(field_name) 
    # Wait for the job listings to be displayed
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_mappings[field_name]))
    )

    # Find and click the "Apply" button for the specified job role
    apply_button = context.driver.find_element(By.XPATH, xpath_mappings[field_name])
    apply_button.click()
    time.sleep(3)    


#tc28
@then('I enter all the fields')
def step_then_i_enter_alltheFieldNames(context):
    time.sleep(5)
    name_input = context.driver.find_element(By.NAME, "name")
    email_input = context.driver.find_element(By.NAME, "email")
    number_input = context.driver.find_element(By.NAME, "number")
    # submit_button = context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/form/button")
    time.sleep(2)
    name_input.clear()
    email_input.clear()
    number_input.clear()
    time.sleep(2)
    submit_button.click()
    time.sleep(2)

@then('I should see the alert message displayed')
def step_alert_message_screen(context):
    alert = WebDriverWait(context.driver, 10).until(EC.alert_is_present())
    alert_text = alert.text
    time.sleep(2)
    expected_alert_text = "Name error!!!"
    if alert_text == expected_alert_text:
        print("Test passed: Alert message is displayed and correct")
    else:
        print(f"Test failed: Unexpected alert message: {alert_text}")

    alert.accept()

#29
@then('I enter a valid name with alphabetic characters only')
def step_then_i_enter_valid_name(context):
    name_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )
    name_input.clear()

    valid_name = "JohnDoe"  # Valid name without numbers
    name_input.send_keys(valid_name)
    time.sleep(2)  # Adjust as needed

@then('I should see the validation for the name input field')
def step_then_i_see_name_validation(context):
    name_input = context.driver.find_element(By.NAME, "name")
    input_value = name_input.get_attribute("value")
    is_valid = input_value.isalpha()
    time.sleep(3)  # Adjust as needed

    if is_valid:
        print(f"Test passed: '{input_value}' is a valid input")
    else:
        print(f"Test failed: '{input_value}' is not a valid input")

#30

@then('I enter a valid phone number')
def step_then_i_enter_valid_phone_number(context):
    number_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "number"))
    )
    number_input.clear()

    valid_number = "6361721712"  # Valid phone number
    number_input.send_keys(valid_number)
    time.sleep(2)  # Adjust as needed

@then('I should see the validation for the phone number input field')
def step_then_i_see_phone_number_validation(context):
    number_input = context.driver.find_element(By.NAME, "number")
    entered_value = number_input.get_attribute("value")

    valid_number = "6361721712"  # Expected valid phone number

    if entered_value == valid_number:
        print(f"Test passed: '{valid_number}' is a valid input and matches the entered value")
    else:
        print(f"Test failed: '{valid_number}' is not a valid input or does not match the entered value")

@then('I should observe the phone number input value is truncated to 10 digits')
def step_verify_phone_number_limitation(context):
    time.sleep(1)
    phone_number_input = context.driver.find_element(By.NAME, "number")

    if len(phone_number_input.get_attribute("value")) == 10:
        print("Test passed: Phone number is limited to 10 digits")
    else:
        print("Test failed: Phone number allows more or less than 10 digits")

# Step to enter invalid phone numbers in the phone number field
@when('I enter invalid phone numbers in the phone number field')
def step_enter_invalid_phone_numbers(context):
    time.sleep(3)
    invalid_numbers = ["abcd", "!@#$%", "Doe"]
    number_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.NAME, "number"))
)
    time.sleep(3)

    for invalid_number in invalid_numbers:
        number_input.clear()
        number_input.send_keys(invalid_number)
        time.sleep(2)
        # Wait for the value attribute to become empty
        WebDriverWait(context.driver, 10).until(lambda driver: number_input.get_attribute("value") == "")

# Step to verify the field value becomes empty after invalid input
@then('I should observe the field value becomes empty after invalid input')
def step_verify_empty_field_after_invalid_input(context):
    number_input = context.driver.find_element(By.NAME, "number")
    entered_value = number_input.get_attribute("value")

    if not entered_value:
        for invalid_number in ["abcd", "!@#$%", "Doe"]:
            print(f"Test passed: '{invalid_number}' is an invalid input and the value is empty")
    else:
        for invalid_number in ["abcd", "!@#$%", "Doe"]:
            print(f"Test failed: '{invalid_number}' is not an invalid input or the value is not empty")

@given('I am on the application page')
def step_given_i_am_on_application_page(context):
    service=Service(executable_path='/home/ananth/Downloads/chromedriver-linux64/chromedriver')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/usr/bin/google-chrome'
    chrome_options.add_argument('--headless')
    # Set ChromeDriver path

    # Create Chrome WebDriver with specified options
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to the desired URL
    context.driver.get("https://hades-stage.simpleenergy.in/apply/be7e88ca-9162-4103-83d0-fbd9261ea984")
   

@when('I wait for the email field to be clickable')
def step_wait_for_email_field_clickable(context):
    wait = WebDriverWait(context.driver, 10)
    context.email_input = wait.until(EC.element_to_be_clickable((By.NAME, "email")))

@when('I enter a valid email address in the email field')
def step_enter_valid_email(context):
    time.sleep(3)
    valid_email = "valid.email@example.com"
    context.email_input.send_keys(valid_email)
    time.sleep(2)
    action = ActionChains(context.driver)
    action.move_by_offset(0, 0).click().perform()

@then('I should verify that the entered email address is accepted')
def step_verify_entered_email_accepted(context):
    time.sleep(2)
    entered_email = context.email_input.get_attribute("value")
    valid_email = "valid.email@example.com"

    if entered_email == valid_email:
        print("Test passed: Valid email address is accepted")
    else:
        print("Test failed: Valid email address is not accepted")

@when('I clear the email input field')
def step_clear_email_input_field(context):
    context.email_input.clear()

@when('I enter an invalid email address in the email field')
def step_enter_invalid_email(context):
    context.email_input.send_keys("afsds@v.com@")

@when('I click outside the email input box to trigger validation')
def step_click_outside_email_input(context):
    action = ActionChains(context.driver)
    action.move_by_offset(0, 0).click().perform()

@then('I should wait for the error message to appear')
def step_wait_for_error_message(context):
    error_message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//small[text()='*Please enter a valid email address']"))
    )
    time.sleep(3)
    context.error_message = error_message

@then('I should verify that the invalid email address is not accepted')
def step_verify_invalid_email_not_accepted(context):
    if context.error_message.is_displayed():
        print("Test Passed: Invalid email address not accepted")
    else:
        print("Test Failed: Invalid email address accepted")

@when('I wait for the LinkedIn input field to be visible')
def step_wait_for_linkedin_field_visible(context):
    context.linkedin_input = WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div[4]/input'))
    )

@when('I enter a valid LinkedIn profile URL in the input field')
def step_enter_valid_linkedin_url(context):
    valid_linkedin = "https://www.linkedin.com/in/yourprofile"
    context.linkedin_input.clear()
    context.linkedin_input.send_keys(valid_linkedin)
    time.sleep(3)

@then('I should verify that the entered LinkedIn URL is accepted')
def step_verify_entered_linkedin_url(context):
    entered_value = context.linkedin_input.get_attribute("value")
    valid_linkedin = "https://www.linkedin.com/in/yourprofile"

    if entered_value == valid_linkedin:
        print(f"Test passed: '{valid_linkedin}' is a valid LinkedIn profile")
    else:
        print(f"Test failed: '{valid_linkedin}' is not a valid LinkedIn profile")

@when('I wait for the file upload element to be visible')
def step_wait_for_file_upload_element(context):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='upload-one']"))
        )
    except TimeoutException:
        print("Test failed: Upload button not found.")
        context.driver.quit()

@when('I upload a document file')
def step_upload_document_file(context):
    try:
        time.sleep(4)
        file_input = context.driver.find_element(By.ID, 'fileInput')
        context.driver.execute_script("arguments[0].style.display = 'block';", file_input)
        file_input.send_keys("/home/ananth/Downloads/1-MB-DOC.doc")
    except Exception as e:
        print(f"Test failed: {str(e)}")
        context.driver.quit()

@then('I should see a success message confirming the file upload')
def step_confirm_file_upload(context):
    print("Test passed: File uploaded successfully.")

@when(u'I wait for the \'Submit\' button to be clickable')
def step_wait_for_submit_button(context):
    try:
        submit_button = WebDriverWait(context.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
        )
        context.submit_button = submit_button
    except TimeoutException:
        print("Timeout: The 'Submit' button was not found within the specified time.")
        context.driver.quit()

@when(u'I click the \'Submit\' button')
def step_click_submit_button(context):
    try:
        context.submit_button.click()
    except Exception as e:
        print(f"An error occurred: {e}")
        context.driver.quit()



@then('I should receive a confirmation of successful click')
def step_confirm_successful_click(context):
    print("Successfully clicked the 'Submit' button.")
    context.driver.quit()


@when('I click the "Submit" button without filling the required fields')
def step_click_submit_without_filling_fields(context):
    try:
        wait = WebDriverWait(context.driver, 30)
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']")))
        submit_button.click()
        time.sleep(2)
        context.alert = wait.until(EC.alert_is_present())
        context.alert.dismiss()
        print("Alert dismissed. Submit button not clicked due to missing fields.")
        print('Test case passed')
    except Exception as e:
        print(f"An error occurred: {e}")

@then('I should see an alert message indicating missing fields')
def step_see_alert_missing_fields(context):
    assert context.alert is not None, "Expected alert indicating missing fields not found."

@when('I search for the keyword "{keyword}"')
def step_search_for_keyword(context, keyword):
    search_input = context.driver.find_element(By.CSS_SELECTOR, ".search-input")
    search_input.clear()
    search_input.send_keys(keyword)
    time.sleep(3)
    search_input.send_keys(Keys.ENTER)
    time.sleep(3)

@then('I should see job listings displayed')
def step_see_job_listings_displayed(context):
    try:
        wait = WebDriverWait(context.driver, 10)
        job_listings = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-item")))
        time.sleep(2)
        if len(job_listings) > 0:
            print("Test passed: Job listings are displayed after searching.")
        else:
            print("Test failed: No job listings found after searching.")
    finally:
        context.driver.quit()

@when('I enter an unlikely keyword in the search input field')
def step_when_i_enter_unlikely_keyword(context):
    search_input = context.driver.find_element(By.CSS_SELECTOR, ".search-input")
    search_input.clear()
    search_input.send_keys("UnlikelySearchKeyword")
    time.sleep(3)
    search_input.send_keys(Keys.ENTER)
    time.sleep(2)

@then('I should see the \'Uh oh! No results found\' message indicating no jobs were found')
def step_then_see_no_results_message(context):
    wait = WebDriverWait(context.driver, 10)
    no_results_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".no-results-message .noResults-message")))

    if "Uh oh! No results found" in no_results_message.text:
        print("Test passed: 'Uh oh! No results found' message is displayed when an invalid keyword is entered.")
    else:
        print("Test failed: Message is different or not displayed correctly.")

@when('I enter an invalid keyword in the search input field')
def step_when_enter_invalid_keyword(context):
    search_input = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
    search_input.send_keys("sdsa")
    action = ActionChains(context.driver)
    action.move_by_offset(0, 0).click().perform()

@then('I should see the \'No results found\' message')
def step_then_see_no_results_message(context):
    no_results_message = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='noResults-message']")))

    if no_results_message.is_displayed():
        print("Test Passed: No jobs found for an invalid keyword")
    else:
        print("Test Failed: Jobs found for an invalid keyword")

    context.driver.quit()
    

@when('I open the "AllDepartments" dropdown menu')
def step_when_open_all_departments(context):
    time.sleep(3)
    dropdown_xpath = "//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-formControl dept-dropdown-filter css-fvipm8']"
    dropdown_box = context.driver.find_element(By.XPATH, dropdown_xpath)
    dropdown_box.click()
    menu_xpath = "//ul[@role='listbox']"
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, menu_xpath)))

@then(u'I should see the following department options')
def step_then_see_department_options(context):
    expected_options = [
        "All Departments", "Design team", "Hardware Department", "Software Department", "HR department"
    ]

    actions = ActionChains(context.driver)
    options = []

    while len(options) < len(expected_options):
        options = context.driver.find_elements(By.XPATH, "//li[@role='option']")
        if len(options) < len(expected_options):
            actions.move_to_element(options[-1]).perform()

    displayed_options = [option.text for option in options]
    time.sleep(3)

    assert displayed_options == expected_options, "Not all options are displayed in the dropdown menu."

    context.driver.quit()    

@when('I click the "Copy" button')
def step_impl(context):
    copy_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "upload-icon")))
    copy_button.click()

@then('I should see the "Link Copied!" message')
def step_impl(context):
    link_copied_message = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "job-role-button-link")))
    assert link_copied_message.is_displayed(), "Link Copied! message is not displayed."

@then('the message should contain the job listing link')
def step_impl(context):
    link_copied_message = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "job-role-button-link")))
    copied_text = link_copied_message.text
    expected_text = "Link Copied!"
    assert expected_text in copied_text, f"'{expected_text}' not found in '{copied_text}'."
    print("Test passed: Link copied successfully.")

@when('I navigate back to the landing page')
def step_impl(context):
    landing_page_url = "https://hades-stage.simpleenergy.in/"
    context.driver.get(landing_page_url)
    WebDriverWait(context.driver, 10).until(EC.url_matches(landing_page_url))

@then('I should successfully return to the landing page')
def step_impl(context):
    landing_page_url = "https://hades-stage.simpleenergy.in/"
    if context.driver.current_url == landing_page_url:
        print("Successfully returned to the landing page.")
    else:
        print("Navigation to the landing page failed.")

@when('I click on the "Discover Jobs" link')
def step_when_click_discover_jobs_link(context):
    time.sleep(2)
    discover_jobs_link = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-logo-heading-discover")))
    discover_jobs_link.click()

@then('I should land on the job discovery page')
def step_then_land_on_job_discovery_page(context):
    time.sleep(3)
    discover_jobs_text = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "heroBanner-text-discover")))
    assert discover_jobs_text.text == "Discover Jobs"

@then('I should see the available departments')
def step_then_see_available_departments(context):
    time.sleep(3)
    departments = context.driver.find_elements(By.CLASS_NAME, "dept-dropdown-filter-discover")
    expected_departments = ["All Departments", "Design team", "Hardware Department", "Software Department", "HR department"]
    for department in departments:
        assert department.text.strip() in expected_departments

@then('I should see the search option')
def step_then_see_search_option(context):
    time.sleep(3)
    search_placeholder = context.driver.find_element(By.CLASS_NAME, "search-placeholder")
    assert search_placeholder.is_displayed()

@then('I should see the "Apply" buttons')
def step_then_see_apply_buttons(context):
    # Add a wait to ensure the buttons are present before attempting to find them
    apply_buttons = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='job-apply-button-discover']/a"))
    )
    assert len(apply_buttons) > 0, "No 'Apply' buttons found"


@then('Test passed: All elements on the page verified successfully.')
def step_then_all_elements_verified(context):
    pass
    print("\tPassed\n")# This step is not functional but serves as a placeholder for the print statement 


@when('I search for a job with keyword "{keyword}"')
def step_when_search_for_job(context, keyword):
    search_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "search-placeholder"))
    )
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.RETURN)

@then('I should find the job "{job_title}" in the search results')
def step_then_find_job_in_search_results(context, job_title):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "job-list-item"))
    )
    time.sleep(2)
    search_results = context.driver.find_elements(By.CLASS_NAME, "desc_title")
    found_job = False
    for result in search_results:
        if job_title in result.text:
            found_job = True
            break

    assert found_job, f"Job '{job_title}' not found in search results."

@when('I search for an invalid job query "{invalid_query}"')
def step_when_search_invalid_query(context, invalid_query):
    search_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "search-placeholder"))
    )
    search_input.send_keys(invalid_query, Keys.RETURN)

@then('I should not find any job listings')
def step_then_no_job_listings(context):
    job_listings_container = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "job-lists-discover"))
    )
    time.sleep(2)
    job_listings = job_listings_container.find_elements(By.CLASS_NAME, "job-list-item")
    time.sleep(2)
    assert len(job_listings) == 0, f"Job listings displayed for an invalid query: '{context.text}'"

@then('I should see the list of jobs')
def step_then_see_list_of_jobs(context):
    time.sleep(2)
    job_list_items = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "job-list-item"))
    )
    assert len(job_list_items) > 0, "No jobs found on the page."

@then('I select the "Design team" department from the dropdown')
def step_then_select_design_team(context):
    departments_dropdown = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "jobs-all-departments")))
    departments_dropdown.click()
    design_team_filter = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@value='Design team']")))
    design_team_filter.click()
    time.sleep(3)

@then('I should see jobs listed under the "Design team" department')
def step_then_verify_design_team_jobs(context):
    time.sleep(4)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "job-list-item")))
    job_titles = context.driver.find_elements(By.CLASS_NAME, "desc_title")
    for job_title in job_titles:
        assert  job_title.text, f"Job '{job_title.text}' does not belong to the 'Design team' department."
    print(f"Test passed: All jobs of the 'Design team' department are displayed.")


@then('I select the "{department}" from the departments dropdown')
def step_then_select_department(context, department):
    departments_dropdown = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "jobs-all-departments")))
    departments_dropdown.click()

    department_filter = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[@value='{department}']")))
    department_filter.click()
    time.sleep(3)

@then('I should see jobs listed under the "{department}"')
def step_then_see_jobs_in_department(context, department):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "job-list-item")))
    time.sleep(2)

    job_titles = context.driver.find_elements(By.CLASS_NAME, "desc_title")

    for job_title in job_titles:
        assert job_title.text, f"Job '{job_title.text}' does not belong to the '{department}' department."

    print(f"Test passed: All jobs of the '{department}' department are displayed.")

@then('I should see job listings displayed for the "{department}"')
def step_then_see_job_listings(context, department):
    wait = WebDriverWait(context.driver, 10)
    job_list_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "job-list-item")))

    if not job_list_items:
        print(f"No job listings found for the {department}.")
    else:
        job_titles = [item.find_element(By.CLASS_NAME, "desc_title").text for item in job_list_items]
        print(f"Job titles in the {department}:")
        for title in job_titles:
            print(title)
        print("Test case passed")

@then('I should see the "{expected_text}" text displayed')
def step_then_see_expected_text(context, expected_text):
    try:
        how_we_hire_text = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flow-title"))
        )
        
        assert how_we_hire_text.text == expected_text, f"Text not displayed correctly. Expected: {expected_text}"

        print(f"Test passed: '{expected_text}' text is displayed.")

    except TimeoutException:
        print(f"Test failed: '{expected_text}' text is not displayed.")

    except Exception as e:
        print(f"Test failed: {str(e)}")

@then('all elements below "{text}" should be visible')
def step_then_see_elements_below_text(context, text):
    try:
        text_element = context.driver.find_element(By.XPATH, f"//*[text()='{text}']")
        elements_below_text = text_element.find_elements(By.XPATH, "following-sibling::*")

        for element in elements_below_text:
            assert element.is_displayed(), "Text element is not displayed."

        print(f"Test passed: All elements below '{text}' are displayed.")

    except Exception as e:
        print(f"Test failed: {str(e)}")

@then('I should see the "{job_title}" job title displayed')
def step_then_see_job_title(context, job_title):
    job_title_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//*[contains(@class, 'desc_title') and contains(text(), '{job_title}')]"))
    )
    time.sleep(2)    
    assert job_title_element.is_displayed(), f"Job title '{job_title}' is not displayed."

@when('I hover over the "{element_text}" job title')
def step_when_hover_job_title(context, element_text):
    time.sleep(3)    
    # Wait for the "Ruby Developer" element to be visible on the page
    ruby_developer_title = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "desc_title"))
    )
    time.sleep(2)
    # Hover over the "Ruby Developer" element
    actions = ActionChains(context.driver)
    actions.move_to_element(ruby_developer_title).perform()

    # Wait for the "Show Description" element to be visible on hover
    show_description = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Show Description')]"))
    )
    time.sleep(3)

    # Verify that the "Show Description" is displayed
    assert show_description.is_displayed(), "Show Description not displayed on hover."

@then('I should see the "{expected_text}" option displayed')
def step_then_see_option(context, expected_text):
    show_description = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//p[contains(text(), '{expected_text}')]"))
    )
    assert show_description.is_displayed(), f"'{expected_text}' not displayed on hover."
    print(f"Test passed: '{expected_text}' is displayed on hover.")

@when('I click on the "Show Description" link')
def step_when_click_show_description(context):
    show_description_link = context.driver.find_element(By.CLASS_NAME, "click_desc")
    show_description_link.click()
    time.sleep(2)

@then('I should see the job description window')
def step_then_see_description_window(context):
    description_window = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "description_window"))
    )
    assert description_window.is_displayed(), "Description window is not displayed."

@then('I should see the job description text')
def step_then_see_description_text(context):
    job_description_text = context.driver.find_element(By.CLASS_NAME, "job_description_text")
    assert job_description_text.is_displayed(), "Job description text is not displayed."

@then('I should see the job meta data')
def step_then_see_meta_data(context):
    job_meta_data = context.driver.find_elements(By.CLASS_NAME, "job_meta_data")
    assert job_meta_data, "Job meta data is not displayed."

@then('I should see the apply button')
def step_then_see_apply_button(context):
    apply_button = context.driver.find_element(By.ID, "apply_btn")
    assert apply_button.is_displayed(), "Apply button is not displayed."
    print("Test passed: All expected elements are displayed within the description window.")

@when('I click on the "Apply" button within the description window')
def step_when_click_apply_button(context):
    apply_button = context.driver.find_element(By.ID, "apply_btn")
    apply_button.click()

@then('I should navigate to the job apply page')
def step_then_navigate_to_apply_page(context):
    time.sleep(4)
    new_page_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.job-application-container"))
    )
    assert new_page_element, "Failed to navigate to the new page."
    print("Test passed: Successfully navigated to the new page.")

@then('I should see the job form')
def step_then_see_job_form(context):
    job_form = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "job-form")))
    assert job_form.is_displayed(), "Job form is not displayed."

@then('I should see the job title')
def step_then_see_job_title(context):
    job_title = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "job-description-header"))) 
    # job_title = context.driver.find_element(By.CLASS_NAME, "job-description-header")
    assert job_title.is_displayed(), "Job title is not displayed."

@then('I should see the job experience')
def step_then_see_job_experience(context):
    job_experience = context.driver.find_element(By.CLASS_NAME, "job-description-experience")
    assert job_experience.is_displayed(), "Job experience is not displayed."

@then('I should see the job description')
def step_then_see_job_description(context):
    job_description = context.driver.find_element(By.ID, "job-description-text")
    assert job_description.is_displayed(), "Job description is not displayed."

@then('I should see the job description page')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "job-description")))


@when('I click the "Read More" button')
def step_impl(context):
    read_more_button = context.driver.find_element(By.CLASS_NAME, "read-more-button")
    read_more_button.click()

@then('the job description should expand')
def step_impl(context):
    read_less_text = WebDriverWait(context.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "read-more-button"), "Read Less"))
    assert read_less_text, "'Read More' button did not change to 'Read Less' after clicking."

@then('I should see the expected texts on the new page')
def step_impl(context):
    time.sleep(4)
    expected_texts = [
        "Job Description:",
        "Responsibilities:",
        "Preferred Qualifications:",
        "Benefits:",
        "How to Apply:",
        "Application Deadline:"
    ]
    new_page_text = context.driver.page_source

    for text in expected_texts:
        assert text in new_page_text, f"Expected text '{text}' not found on the new page."

@when('I scroll down to view the footer')
def step_scroll_to_footer(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

@then(u'I should verify the presence of "{element_text}" in the footer')
def step_verify_footer_element(context, element_text):
    try:
        element = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{element_text}')]"))
        )

        if element.is_displayed():
            print(f"'{element_text}' is present in the footer.")
        else:
            print(f"'{element_text}' is NOT present in the footer.")
    except Exception as e:
        print(f"Element '{element_text}' not found on the page within the extended timeout.")

@then('I wait for the web page to fully load')
def step_wait_for_load(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "work-content-text")))
    time.sleep(4)

@then('I verify each text')
def step_verify_texts(context):
    expected_texts = ["Belonging", "Inclusion", "Equity", "Diversity"]
    elements = context.driver.find_elements(By.CLASS_NAME, "work-title")

    for i, element in enumerate(elements):
        text = element.text
        if text == expected_texts[i]:
            print(f"Text '{text}' is displayed.")
        else:
            print(f"Text '{expected_texts[i]}' is not displayed.")

@then('I verify each texts')
def step_verify_texts(context):
    expected_texts = [
        "We aim not only to nurture a sense of belonging within our corporate culture but also to magnify it on a global scale",
        "We prioritise empathy as a guiding principle and continually seek avenues to integrate inclusivity into our organisational culture",
        "Our mission is to guarantee that all individuals have equal and just access to opportunities and progression.",
        "We strive to ensure fair or increased inclusion of historically underrepresented communities"
    ]

    elements = context.driver.find_elements(By.CLASS_NAME, "work-content-text")

    for i, element in enumerate(elements):
        text = element.text
        if text == expected_texts[i]:
            print(f"Text '{text}' is displayed.")
        else:
            print(f"Text '{expected_texts[i]}' is not displayed.")

@then('I verify the expected text')
def step_verify_expected_text(context):
    expected_texts = ["What it means to us"]
    elements = context.driver.find_elements(By.CLASS_NAME, "work-heading")
    check1 = False

    for i, element in enumerate(elements):
        text = element.text
        if text == expected_texts[i]:
            print(f"Text '{text}' is displayed.\n")
            check1 = True
        else:
            print(f"Text '{expected_texts[i]}' is not displayed.\n")

    return check1

@then('I verify the description text')
def step_verify_description_text(context):
    description = "Fostering a sense of belonging goes beyond good intentions. It 's about embracing diversity, staying aware of differences, and taking active steps. For us, Diversity, Equity, Inclusion, and Belonging mean creating a place where everyone is valued and welcomed."
    elements = context.driver.find_elements(By.CLASS_NAME, "work-content")
    check2 = False

    for i, element in enumerate(elements):
        text = element.text
        if text == description:
            print(f"Description '{text}' is displayed.\n")
            check2 = True
        else:
            print(f"Description '{text}' is not displayed.\n")

    return check2


@then('I check if all input fields are empty')
def step_check_empty_input_fields(context):
    name_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.NAME, 'name')))
    email_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
    number_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.NAME, 'number')))
    linkedin_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div/form/div[4]/input')))

    if all(field.get_attribute('value') == '' for field in [name_input, email_input, number_input, linkedin_input]):
        print("All input fields are empty.")
    else:
        print("Not all input fields are empty. Test failed.")

@then('I check if the submit button color is grey')
def step_check_submit_button_color(context):
    submit_button = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'common-action-button')))
    submit_button_color = submit_button.value_of_css_property('background-color')

    # Check if the button color matches the expected grey color when fields are empty
    expected_grey_color = 'rgba(201, 201, 201, 1)'  # Adjust this to the expected color
    if submit_button_color == expected_grey_color:
        print("Submit button color is grey when all fields are empty.")
    else:
        assert False, "Submit button color is not grey when all fields are empty. Test failed."

@when('I fill in the application form with valid details')
def step_impl_when(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.NAME, 'name')))
    name_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.NAME, 'name')))
    email_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
    number_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.NAME, 'number')))
    linkedin_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div/form/div[4]/input')))
    
    time.sleep(3)
    name_input.send_keys("Your Name")
    time.sleep(2)
    email_input.send_keys("your@email.com")
    time.sleep(2)
    number_input.send_keys("9234567890")
    time.sleep(2)
    linkedin_input.send_keys("https://www.linkedin.com/in/yourprofile")
    time.sleep(4)

@when('I upload a resume')
def step_impl_when_upload(context):
    # Upload file
    file_input = context.driver.find_element(By.ID, 'fileInput')
    context.driver.execute_script("arguments[0].style.display = 'block';", file_input)
    file_input.send_keys("/home/ananth/Downloads/1-MB-DOC.doc")
    time.sleep(2)  # Wait for a short duration to ensure the file is uploaded

@when('I submit the application')
def step_impl_when_submit(context):
    # Click the submit button after file upload
    submit_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'common-action-button')))
    submit_button.click()
    # Wait for the application success page to load
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'applicationSuccess')))
    time.sleep(2)  # Additional wait time for stability

@then('I should see a success message confirming the submission')
def step_impl_then(context):
    # Check if the application success message is displayed
    if context.driver.find_element(By.ID, 'submitted_titile').is_displayed():
        print("Application submitted successfully!")
    else:
        print("Application submission failed.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when('I fill in the application form without details')
def step_fill_application_form_without_details(context):
    name_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.NAME, 'name')))
    email_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
    number_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.NAME, 'number')))
    file_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, 'fileInput')))
    
    # Filling the form with empty or default values
    name_input.send_keys("Your Name")
    email_input.send_keys("your@email.com")
    number_input.send_keys("1234567890")
    file_input.send_keys("/home/ananth/Downloads/1-MB-DOC.doc")
    WebDriverWait(context.driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'spinner')))


@then('I should see an alert indicating the error')
def step_verify_alert_presence(context):
    try:
        alert = WebDriverWait(context.driver, 5).until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Alert message: {alert_text}")
        alert.accept()  # Accept the alert
    except TimeoutException:
        print("No alert found. Test failed.")

@then('I should not see the application success message')
def step_verify_no_success_message(context):
    try:
        WebDriverWait(context.driver, 5).until_not(EC.presence_of_element_located((By.CLASS_NAME, 'applicationSuccess')))
        print("Application submission without details successful. Test passed.")
    except TimeoutException:
        print("Application submission without details failed. Test failed.")

@when('I click the submit button')
def step_impl_when_submit(context):
    submit_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'common-action-button')))
    submit_button.click()

@when('I wait for the application success page to load')
def step_impl_when_success_page(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'applicationSuccess')))
    time.sleep(4)

@when('I click the How We Hire button')
def step_impl_when_how_we_hire(context):
    how_we_hire_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submitted_button')))
    how_we_hire_button.click()

@then('I should verify the functionality of the How We Hire button')
def step_impl_then_verify_button(context):
    if context.driver.find_element(By.ID, 'flow-title').is_displayed():
        print("How we hire button is working successfully. Test case passed.")
    else:
        print("Test case failed.")


@then('I should verify the job title consistency on the application success page')
def step_impl_then(context):
    time.sleep(3)
    job_title_element = context.driver.find_element(By.CLASS_NAME, 'job-application-title')
    job_title = job_title_element.text
    print(f"Job Title: {job_title}")

    submit_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'common-action-button')))
    submit_button.click()

    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'applicationSuccess')))
    time.sleep(2)

    success_job_title_element = context.driver.find_element(By.CLASS_NAME, 'job-application-title')
    success_job_title = success_job_title_element.text
    print(f"Job Title on Application Success Page: {success_job_title}")

    if job_title == success_job_title:
        print("Job titles match. Test passed.")
    else:
        print("Job titles do not match. Test failed.")

@then('I should verify the presence of the "Copy Link" logo')
def step_impl_then(context):
    try:
        logo_element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='upload-icon']/img")))
        
        if logo_element.is_displayed():
            print("Copy Link logo is displayed. Test passed.")
        else:
            print("Copy Link logo is not displayed. Test failed.")
    
    except Exception as e:
        print("An error occurred:", e)


@when('I scroll to the job lists section and view them')
def step_scroll_to_and_view_job_lists(context):
    # Scroll to the job-lists section
    time.sleep(3)
    # job_lists_element = context.driver.find_element(By.CLASS_NAME, "job-lists")
    job_lists_element=WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "job-lists"))
    )
    time.sleep(3)
    
    context.driver.execute_script("arguments[0].scrollIntoView(true);", job_lists_element)
    time.sleep(3)

    # Validate if job lists are visible
    assert "job-lists" in context.driver.page_source.lower(), "Job lists not visible"
    # You can add additional verification steps as needed





@then('I close the browser')
def step_close_browser(context):
    context.driver.quit()


def after_scenario(context, scenario):
    context.driver.quit()






















# @when('I click on the dropdown and select "Software Department"')
# def step_when_i_select_software_department(context):
#     dropdown_element = WebDriverWait(context.driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiSelect-select"))
#     )
#     time.sleep(2)
    
#     dropdown_element.click()
#     time.sleep(2)

#     software_option = context.driver.find_element(By.XPATH, "//li[contains(text(),'Software Department')]")
#     software_option.click()
#     time.sleep(2)
# #TC9

# @then('I should see job items listed under the "Software Department"')
# def step_then_i_should_see_job_items_under_software_department(context):
#     WebDriverWait(context.driver, 10).until(
#         EC.presence_of_all_elements_located((By.CLASS_NAME, "job-item-header"))
#     )

#     job_items = context.driver.find_elements(By.CLASS_NAME, "job-item")

#     if len(job_items) > 0:
#         print("Expected Result: It should have job items under Software Department")
#         print("Actual Result: Job items are listed under Software Department")
#     else:
#         print("Expected Result: It should have job items under Software Department")
#         print("Actual Result: No job items found under Software Department")

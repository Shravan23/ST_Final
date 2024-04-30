from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_chrome_options():
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode.
    options.add_argument("--no-sandbox")  # Bypass OS security model.
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems.
    options.add_argument("--disable-gpu")  # Applicable to windows os only.
    options.add_argument("--window-size=1920,1080")
    return options

@given('I am on the login page')
def step_impl(context):
    context.browser = webdriver.Chrome(options=get_chrome_options())  # Ensure ChromeDriver is installed and in PATH
    context.browser.get('http://127.0.0.1:5000/login')

@when('I enter valid credentials')
def step_impl(context):
    # Updated element selectors
    username_field = context.browser.find_element(By.ID, 'username')
    password_field = context.browser.find_element(By.ID, 'password')
    submit_button = context.browser.find_element(By.ID, 'submit')

    username_field.send_keys('pant')
    password_field.send_keys('pant123')
    submit_button.click()

@then('I should be redirected to the profile page')
def step_impl(context):
    assert 'profile' in context.browser.current_url
    context.browser.quit()

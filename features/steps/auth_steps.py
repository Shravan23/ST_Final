from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('I am on the login page')
def step_impl(context):
    context.browser = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
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

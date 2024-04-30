from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the registration page')
def step_impl(context):
    context.browser = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
    context.browser.get('http://127.0.0.1:5000/register')

@when('I enter valid registration details')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    context.browser.find_element(By.ID, 'username').send_keys('newuser')
    context.browser.find_element(By.ID, 'email').send_keys('newuser@example.com')
    context.browser.find_element(By.ID, 'password').send_keys('newpassword')
    context.browser.find_element(By.ID, 'confirm_password').send_keys('newpassword')
    context.browser.find_element(By.ID, 'submit').click()

@then('I should be registered and redirected to the login page')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.url_contains('/login')
    )
    assert '/login' in context.browser.current_url
    context.browser.quit()

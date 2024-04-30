from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import random
import string

def get_chrome_options():
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode.
    options.add_argument("--no-sandbox")  # Bypass OS security model.
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems.
    options.add_argument("--disable-gpu")  # Applicable to windows os only.
    options.add_argument("--window-size=1920,1080")
    return options

@given('I am on the registration page')
def step_impl(context):
    context.browser = webdriver.Chrome(options=get_chrome_options())  # Ensure ChromeDriver is installed and in PATH
    context.browser.get('http://localhost:8080/register')

@when('I enter valid registration details')
def step_impl(context):
    letters = string.ascii_lowercase
    userName = result_str = ''.join(random.choice(letters) for i in range(8))
    email = userName + '@example.com'
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    context.browser.find_element(By.ID, 'username').send_keys(userName)
    context.browser.find_element(By.ID, 'email').send_keys(email)
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

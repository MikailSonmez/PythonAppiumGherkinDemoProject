from behave import given, when, then
from selenium.webdriver.common.by import By

given("I am on the login screen")
def step_impl(context):
    pass

@when("I enter valid credentials")
def step_impl(context):
    context.driver.find_element(By.ID, "username_field").send_keys("testuser")
    context.driver.find_element(By.ID, "password_field").send_keys("password123")
    context.driver.find_element(By.ID, "login_button").click()

@then("I should see the dashboard screen")
def step_impl(context):
    assert context.driver.find_element(By.ID, "dashboard_screen")
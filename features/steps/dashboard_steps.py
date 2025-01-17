from behave import given, then

given("I am on the dashboard screen")
def step_impl(context):
    pass 

@then("the title should be \"Dashboard\"")
def step_impl(context):
    title_element = context.driver.find_element_by_id("dashboard_title")
    assert title_element.text == "Dashboard"

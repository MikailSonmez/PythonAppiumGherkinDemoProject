from utils.appium_utils import get_appium_driver

def before_all(context):
    context.driver = get_appium_driver()

def after_all(context):
    context.driver.quit()
import json
from appium import webdriver

def get_appium_driver():
    with open("utils/config.json") as f:
        config = json.load(f)

    return webdriver.Remote(
        command_executor="http://127.0.0.1:4723/wd/hub",
        desired_capabilities=config
    )


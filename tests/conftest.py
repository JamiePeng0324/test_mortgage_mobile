import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from appium.webdriver import Remote
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def driver():
    desired_caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "emulator-5554",
        "browserName": "Chrome",
        "chromedriverExecutable": "C:/Users/Jamie/Desktop/chromedriver-win32/chromedriver.exe"
    }
    options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = Remote(command_executor="http://localhost:4723/wd/hub", options=options)
    yield driver
    driver.quit()
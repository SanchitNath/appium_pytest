import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def driver():
    # Configure capabilities using UiAutomator2Options
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.set_capability("appPackage", "com.flipkart.android")
    options.set_capability("appActivity", "com.flipkart.android.SplashActivity")
    # Force a fresh start every time
    options.no_reset = False
    options.set_capability("fullReset", False)
    appium_server_url = 'http://127.0.0.1:4723'
    # Initialize the driver session
    driver = webdriver.Remote(appium_server_url, options=options)
    driver.implicitly_wait(10)  # Global timeout for elements to appear
    yield driver
    if driver:
        driver.quit()
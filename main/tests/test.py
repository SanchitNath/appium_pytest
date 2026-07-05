from appium.webdriver.common.appiumby import AppiumBy
import time
import pytest
import os
from utils.logger import LogGen
logger = LogGen.loggen()

@pytest.mark.Emulator
class TestEmulator:
    def setup_method(self):
        logger.info("In setup method")
        logger.info(os.path.basename(__file__))
        logger.info(os.path.splitext(os.path.basename(__file__)))
        logger.info("_________")

    def test_open_flipkart_and_select_language(self, driver):
        logger.info("Flipkart application launched successfully!")
        # Example Step: Handle the initial language selection screen if it appears
        try:
            # Locate English language button (update ID if Flipkart structure changes)
            english_btn = driver.find_element(by=AppiumBy.ID, value="com.flipkart.android:id/select_language")
            english_btn.click()
            logger.info("Selected English language successfully.")

            # Locate the 'Continue' button and click it
            continue_btn = driver.find_element(by=AppiumBy.ID, value="com.flipkart.android:id/continue_button")
            continue_btn.click()
        except Exception as e:
            logger.error(f"Language screen did not appear or elements changed, skipping. Error: {e}")
        # Allow the home screen to settle for visual validation
        time.sleep(3)

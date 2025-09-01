from selenium.webdriver.support.ui import WebDriverWait
import time
from .logger import message_logger



def hide_keyboard(driver):
    """
    Hides the on-screen keyboard on LambdaTest mobile devices 
    to prevent it from blocking other elements during test execution.
    """
    try:
        driver.execute_script("document.activeElement.blur();")
        time.sleep(0.5) 
    except Exception as e:
        message_logger().warning(f"JavaScript blur() command failed, but continuing. Error: {e}")
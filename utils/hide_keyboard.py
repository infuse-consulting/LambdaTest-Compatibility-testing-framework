from selenium.webdriver.support.ui import WebDriverWait
import time
from utils.logger import message_logger

def hide_keyboard(driver):
    try:
        driver.execute_script("document.activeElement.blur();")
        time.sleep(0.5) 
    except Exception as e:
        message_logger().warning(f"JavaScript blur() command failed, but continuing. Error: {e}")
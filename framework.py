import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException,ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.logger import message_logger
from utils.get_platform import get_platform

class Framework:    
    def __init__(self,driver):
        self.wait_time=10
        self.driver=driver
        self.wait=WebDriverWait(self.driver,self.wait_time)
        self.real_device,self.platform = get_platform(driver.capabilities_dict)

    def navigate_to_page(self,url:str):
        try:
            self.driver.get(url)
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME,'body')))
            message_logger().info(f"Navigated to page :{url}")
            return self.driver.title
        except Exception as e:
            message_logger().exception(f"Failed to load {url}")
            return None

    def find_element(self,locator:dict):
        try:
            by, value =self.get_element_by_type(locator)
            return self.wait.until(EC.presence_of_element_located((by, value)))    
        except (TimeoutException,NoSuchElementException,Exception) as e:
                message_logger().exception(f"Error finding element with locator {locator}")
                return e
    
    def find_elements(self, locator:dict):
        try:
            by, value = self.get_element_by_type(locator)
            return self.wait.until(
                EC.presence_of_all_elements_located((by, value))
            )
        except (TimeoutException, NoSuchElementException,Exception) as e:
            return e
        
    def click_element(self, locator: dict):
        try:
            by, value = self.get_element_by_type(locator)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, value)))
            element = self.find_element(locator)

            if element is None:
                message_logger().error(f"Element not found: {locator}")
                return False

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.5)
            try:
                element.click()
                message_logger().info(f"Clicked element {locator} using standard click.")
            except Exception as e:
                message_logger().warning(f"Standard click failed: {e}")
                try:
                    self.driver.execute_script("arguments[0].click();", element)
                    message_logger().info(f"Clicked element {locator} using JavaScript.")
                except Exception as js_e:
                    message_logger().error(f"[ERROR] Both clicks failed for {locator}: {js_e}")
                    return False
            return True

        except Exception as e:
            message_logger().error(f"[ERROR] Click handler failed for {locator}: {e}")
            return False

    def enter_keys(self, locator: dict, key: str):
        element = self.find_element(locator)
        if element is None or isinstance(element, Exception):
            message_logger().error(f"Element not found or failed to locate: {locator}")
            return False
        try:
            element.send_keys(key)
            message_logger().info(f"Sent keys to element: {locator}")
            return True
        except ElementNotInteractableException as e:
            message_logger().error(f"Element not interactable for locator {locator}")
        except TimeoutException as e:
            message_logger().error(f"Timeout while sending keys to {locator}")
        except Exception as e:
            message_logger().exception(f"Unexpected error while sending keys to {locator}")
        return False


    def get_element_text(self,locator:dict):
        element=self.find_element(locator)
        if element is None:
            return False
        try:
            text = element.text
            if not text:  # If text is empty (input field) get the value attribute
                text = element.get_attribute('value')
            return text if text else None
        except (TimeoutException,Exception) as e:
            return None

    def get_element_by_type(self, locator:dict):
        locator_types = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "class": By.CLASS_NAME,
            "tag": By.TAG_NAME,
            "link": By.LINK_TEXT,
            "partial_link": By.PARTIAL_LINK_TEXT
        }
        try:
            by, value = next(iter(locator.items()))
            by_type = locator_types.get(by.lower())
            if by_type:
                return (by_type, value)
            else:
                raise ValueError(f"Unsupported locator type: {locator}")
        except Exception as e:
            message_logger().error(f"Error parsing locator: {locator}")
            return (None, None)

            
    def get_element_attribute(self,locator:dict,attribute:str):
        element = self.find_element(locator)
        if element is None:
            return False
        try:
            attribute_value = element.get_attribute(attribute)
            if attribute_value == '':
                return (f"Attribute is not found.")
            return attribute_value
        except (Exception) as e:
            return None 
        
    def wait_for_element_to_appear(self, locator: dict, timeout: int = 15):
        message_logger().info(f"[DEBUG] Timeout received: {timeout}")
        by, value = self.get_element_by_type(locator)
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            message_logger().info(f"Element became visible: {locator}")
            return True
        except TimeoutException:
            message_logger().warning(f"Timeout: Element did not appear within {timeout} seconds: {locator}")
            return False
        except Exception as e:
            message_logger().exception(f"Unexpected error while waiting for element to appear: {locator}")
            return False

    def is_element_displayed(self, locator: dict) -> bool:
        try:
            element = self.find_element(locator)
            if element and element.is_displayed():
                message_logger().info(f"Element is displayed: {locator}")
                return True
            else:
                message_logger().info(f"Element is not displayed or not found: {locator}")
                return False
        except Exception as e:
            message_logger().exception(f"Error while checking if element is displayed: {locator}, Error: {e}")
            return False


    def select_from_dropdown_by_value(self,locator:dict,value:str):
        element = self.find_element(locator)
        if element is None:
            message_logger().error(f"Dropdown not found: {locator}")
            return False
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            Select(element).select_by_value(value)
            message_logger().info(f"Element with {locator} is selected")
            return value
        except Exception as e:
            message_logger().info(f"Element with {locator} is selected , Error: {e}")
            return None
        
    def get_input_field_by_label_text(self, label_text: str):
        xpath = f"//label[contains(text(),'{label_text}')]/following::input[1]"
        return {"xpath": xpath}

    def is_checkbox_checked(self, locator: dict) -> bool:
        element = self.find_element(locator)
        if element is None:
            print(f"Checkbox not found: {locator}")
            return False
        try:
            return element.is_selected()
        except Exception as e:
            print(f"Error checking checkbox state: {e}")
            return False
        
    def wait_for_element_to_disappear(self, locator: dict, timeout: int = 10):
        by, value = self.get_element_by_type(locator)
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.presence_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            message_logger().warning(f"Timeout: Element still present after {timeout} seconds: {locator}")
            return False


    def wait_and_click_enabled_button(self, locator: dict, timeout=20):
        try:
            element=self.find_element(locator)
            
            by, value = self.get_element_by_type(locator)
            WebDriverWait(self.driver, timeout).until(
                lambda driver: (
                    driver.find_element(by, value).is_enabled() and
                    not driver.find_element(by, value).get_attribute("disabled")
                )
            )
            self.click_element(locator)
            return True
        except Exception as e:
            print(f"Failed to click enabled button: {e}")
            return False

    def wait_until_dropdown_enabled(self, locator: dict, timeout: int = 15):
        """
        Wait until a dropdown is enabled based on the 'data-disabled' attribute being 'false'.
        """
        try:
            element = self.find_element(locator)
            WebDriverWait(self.driver, timeout).until(
                lambda d: element.get_attribute("data-disabled") == "false"
            )
            message_logger().info(f"Dropdown {locator} is now enabled.")
            return True
        except TimeoutException:
            message_logger().warning(f"Timeout: Dropdown {locator} is not enabled after {timeout} seconds.")
            return False
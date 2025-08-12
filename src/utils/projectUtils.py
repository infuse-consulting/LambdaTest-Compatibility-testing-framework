from utils.logger import message_logger
from selenium.webdriver.support.ui import Select
from framework import Framework

class Utils(Framework):
    def __init__(self, driver):
        super().__init__(driver)

    def assert_text(self,expected,actual,assert_msg):
        assert_pass=f"{assert_msg} : Expected value {expected} matches {actual}"
        assert_fail=f"{assert_msg} : Could not find {expected} value. Instead found {actual}"
        try:
            assert(expected==actual)
            message_logger().info(assert_pass)
        except:
            message_logger().info(assert_fail)
            raise (AssertionError(assert_fail))
        
    def assert_dropdown_value(self, locator, expected, assert_msg):
        element=self.find_element(locator)
        selected_option = Select(element).first_selected_option.get_attribute("value")
        assert_pass = f"{assert_msg} : Selected option '{expected}' is correct"
        assert_fail = f"{assert_msg} : Expected '{expected}', but found '{selected_option}'"
        try:
            assert expected == selected_option
            message_logger().info(assert_pass)
        except:
            message_logger().info(assert_fail)
            raise AssertionError(assert_fail)

    def assert_input_value(self, locator, expected, assert_msg):
        element=self.find_element(locator)
        actual = element.get_attribute("value").strip()
        assert_pass = f"{assert_msg} : Expected '{expected}' matches actual '{actual}'"
        assert_fail = f"{assert_msg} : Expected '{expected}', but found '{actual}'"
        try:
            assert expected == actual
            message_logger().info(assert_pass)
        except:
            message_logger().info(assert_fail)
            raise AssertionError(assert_fail)

    def assert_checkbox_selected(self, locator, assert_msg):
        element=self.find_element(locator)
        is_checked = element.is_selected()
        assert_pass = f"{assert_msg} : Checkbox is selected"
        assert_fail = f"{assert_msg} : Checkbox is NOT selected"
        try:
            assert is_checked
            message_logger().info(assert_pass)
        except:
            message_logger().info(assert_fail)
            raise AssertionError(assert_fail)

    def assert_radio_selected(self, locator, assert_msg):
        element=self.find_element(locator)
        is_selected = element.is_selected()
        assert_pass = f"{assert_msg} : Radio button is selected"
        assert_fail = f"{assert_msg} : Radio button is NOT selected"
        try:
            assert is_selected
            message_logger().info(assert_pass)
        except:
            message_logger().info(assert_fail)
            raise AssertionError(assert_fail)
        
    def assert_page_is_displayed(self,locator, assert_msg):
        element=self.find_element(locator)
        assert_pass = f"{assert_msg} page is displayed"
        assert_fail = f"{assert_msg} page is not displayed"
        try:
            assert element.is_displayed() 
            message_logger().info(assert_pass)
        except:
            message_logger().info(assert_fail)
            raise AssertionError(assert_fail)
    
    def assert_element_visible(self,locator,assert_msg):
        assert_pass = f"{assert_msg} element is displayed"
        assert_fail = f"{assert_msg} element is not displayed"    
        try:
            assert self.wait_for_element_to_appear(locator)
            message_logger().info(assert_pass)
        except:
            message_logger().info(assert_fail)
            raise AssertionError(assert_fail)    

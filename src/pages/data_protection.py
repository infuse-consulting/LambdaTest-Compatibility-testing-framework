from framework import Framework
from pages.equal_opportunities import EqualOpportunitiesPage
import time
from utils.logger import message_logger
from utils.hide_keyboard import hide_keyboard

class DataProtection(Framework):
    def __init__(self, driver):
        super().__init__(driver)
        self.agreement={"xpath":"//label[text()='I Agree']/preceding-sibling::input"}
        self.email_checkbox={"xpath":"//label[contains(text(),'Mail')]/preceding-sibling::input[1]"}
        self.mobile_continue_button={"xpath":"(//a[span[text()='Continue']])[4]"} 
        self.save_button={"xpath":"//a[span[text()='Save']]"}
        self.desktop_continue_button={"xpath":"(//a[span[text()='Continue']])[2]"}
        self.opportunities_title={"xpath":"//h2[contains(text(),'Equal Opportunities')]"}

    def fill_data_protection(self):
        hide_keyboard(self.driver)
        self.click_element(self.agreement)
        self.click_element(self.email_checkbox)

    def submit_form(self):
        if self.platform in ["mobile"]:
            self.click_element(self.save_button)
            self.wait_for_element_to_appear(self.mobile_continue_button)
            time.sleep(1)
            self.click_element(self.mobile_continue_button)
        else:
            self.click_element(self.save_button)
            time.sleep(3)
            self.click_element(self.desktop_continue_button)

        self.wait_for_element_to_appear(self.opportunities_title)
        return EqualOpportunitiesPage(self.driver)
    

    
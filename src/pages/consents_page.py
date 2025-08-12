from framework import Framework
import time
from utils.hide_keyboard import hide_keyboard

class ConsentsPage(Framework):
    def __init__(self, driver):
        super().__init__(driver)
        self.evidence={"xpath":"//label[contains(text(),'Evidence Type')]/following-sibling::div//select"}
        self.upload_button={"xpath":"(//a[span[text()='Upload']])"}
        self.success_popup={"xpath":"//h4[span[text()='Success']]"}
        self.close_button={"xpath":"//button[text()='Close']"}
        self.mobile_continue_button={"xpath":"(//a[span[text()='Continue']])[2]"}
        self.desktop_continue_button={"xpath":"(//a[span[text()='Continue']])"}
        self.agree_checkbox={"xpath":"//label[contains(text(),'* I Agree')]"}
        self.desktop_submit_button={"xpath":"(//a[span[contains(text(),'Submit')]])[1]"}
        self.mobile_submit_button={"xpath":"(//a[span[contains(text(),'Submit')]])[2]"}
        self.submit_page={"xpath":"//h4[contains(text(),'ready to submit your details')]"}
        self.agree_checkbox_button={"xpath":"//label[contains(text(),'* I Agree')]/preceding-sibling::input"}
        self.application_submitted_page={"xpath":"//h3[contains(text(),'Application Submitted')]"}

    def fill_Consents(self):
        hide_keyboard(self.driver)
        self.click_element(self.agree_checkbox)

    def submit_form(self):
        if self.platform in ["mobile"]:
            self.click_element(self.mobile_continue_button)
            self.wait_for_element_to_appear(self.submit_page)
            self.click_element(self.mobile_submit_button)
        else:
            self.click_element(self.desktop_continue_button)
            self.wait_for_element_to_appear(self.submit_page)
            self.click_element(self.desktop_submit_button)

    def close_success_popup(self):
        if self.platform in ["mobile"]:
            self.wait_for_element_to_appear(self.close_button, timeout=10)
            self.click_element(self.close_button)
            self.wait_for_element_to_appear(self.application_submitted_page)
        else:
            self.wait_for_element_to_appear(self.close_button, timeout=10)
            time.sleep(1)
            self.click_element(self.close_button)
            self.wait_for_element_to_appear(self.application_submitted_page)
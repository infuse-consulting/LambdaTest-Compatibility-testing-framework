from framework import Framework
import time
from pages.further_details import FurtherDetailsPage
from utils.hide_keyboard import hide_keyboard

class PersonalDetailsPage(Framework):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver 
        self.first_name = self.get_input_field_by_label_text("* First name")
        self.last_name = self.get_input_field_by_label_text("* Last name")
        self.middle_name = self.get_input_field_by_label_text("Middle name(s)")
        self.ehcp={"xpath":"//label[contains(text(),'Do you have or currently applying for EHCP?')]/following-sibling::div//select"}
        self.postcode = self.get_input_field_by_label_text("address or postcode to search")
        self.find_button={"xpath":"//a[span[text()='Find']]"}
        self.address_search_result={"xpath":"//label[contains(text(),'Address Search Results')]/following-sibling::div//select"}
        self.mobile_continue_button={"xpath":"(//a[span[text()='Continue']])[2]"}
        self.desktop_continue_button={"xpath":"(//a[span[text()='Continue']])"}
        self.address_value="8630506"
        self.residency_title={"xpath":"//h2[contains(text(),'Residency')]"}
        self.personal_details_page_title={"xpath":"//h2[contains(text(),'Personal Details')]"}

    def fill_personal_details(self):
        time.sleep(2)
        self.select_from_dropdown_by_value(self.ehcp,"N")
        self.enter_keys(self.postcode,"EN3")
        if self.platform in ["android", "ios"]:
            hide_keyboard(self.driver)
            self.click_element(self.find_button)
        else:
            hide_keyboard(self.driver)
            self.click_element(self.find_button)
        time.sleep(2)
        self.select_from_dropdown_by_value(self.address_search_result,"8630506")

    def submit_form(self):
        if self.platform in ["mobile"]:
            self.click_element(self.mobile_continue_button)
        else:
            time.sleep(2)
            self.click_element(self.desktop_continue_button)
        self.wait_for_element_to_appear(self.residency_title)
        return FurtherDetailsPage(self.driver)

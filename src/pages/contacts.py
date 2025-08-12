from framework import Framework
from pages.data_protection import DataProtection
import time
from utils.hide_keyboard import hide_keyboard


class Contacts(Framework):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver 
        self.title={"xpath":"//label[contains(text(),'Title')]/following::select[1]"}
        self.first_name = self.get_input_field_by_label_text("* First name")
        self.last_name = self.get_input_field_by_label_text("* Last name")
        self.mobile=self.get_input_field_by_label_text("* Mobile")
        self.email=self.get_input_field_by_label_text("* Email")
        self.relationship={"xpath":"//label[contains(text(),'Relationship')]/following::select[1]"}
        self.permission_to_contact={"xpath":"//label[contains(text(),'Permission to contact')]/following::select[1]"}
        self.postcode = self.get_input_field_by_label_text("Type part of an address or postcode to search")
        self.find_button={"xpath":"//a[span[text()='Find']]"}
        self.address_search_result={"xpath":"//label[contains(text(),'Address Search Results')]/following-sibling::div//select"}
        self.save_this_contact_button={"xpath":"(//a[span[text()='Save this contact']])"}
        self.mobile_continue_button={"xpath":"(//a[span[text()='Continue']])[2]"}
        self.desktop_continue_button={"xpath":"(//a[span[text()='Continue']])"}
        self.data_protection_title={"xpath":"//h2[contains(text(),'Marketing communication preferences')]"}

    def fill_contact_details_form(self):
        self.select_from_dropdown_by_value(self.title,"MR")
        self.enter_keys(self.first_name,"Test")
        self.enter_keys(self.last_name,"test")
        self.enter_keys(self.email,"test@test.com")
        self.enter_keys(self.mobile,"07777777777")
        self.select_from_dropdown_by_value(self.relationship,"GUARDIAN")
        self.select_from_dropdown_by_value(self.permission_to_contact,"N")
        self.enter_keys(self.postcode,"RG42 3XG")
        
        if self.platform in ["mobile"]:
            hide_keyboard(self.driver)
            self.wait_and_click_enabled_button(self.find_button)
        else:
            hide_keyboard(self.driver)
            self.click_element(self.find_button)

    def submit_form(self):
        if self.platform in ["mobile"]:
            self.wait_until_dropdown_enabled(self.address_search_result)
            self.select_from_dropdown_by_value(self.address_search_result,"20060612")
            self.click_element(self.save_this_contact_button)
            self.wait_for_element_to_appear(self.mobile_continue_button)
            self.click_element(self.mobile_continue_button)
        else:
            time.sleep(2)
            self.select_from_dropdown_by_value(self.address_search_result,"20060612")
            self.wait_and_click_enabled_button(self.save_this_contact_button)
            self.wait_for_element_to_appear(self.desktop_continue_button)
            self.click_element(self.desktop_continue_button)

        if self.platform in ["mobile"]:
            time.sleep(2)
            self.click_element(self.mobile_continue_button)
        else:
            time.sleep(2)
            self.click_element(self.desktop_continue_button)
        self.wait_for_element_to_appear(self.data_protection_title)
        return DataProtection(self.driver)





    


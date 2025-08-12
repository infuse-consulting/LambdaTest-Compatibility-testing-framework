from framework import Framework
import uuid
from pages.personal_details_page import PersonalDetailsPage
import time
from utils.hide_keyboard import hide_keyboard
from utils.generate_name import generate_dummy_names

class RegisterPage(Framework):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver 
        self.accept_cookie_button = {"xpath": "//a[contains(text(), 'ACCEPT')]"}
        self.desktop_create_account = {"xpath": "//a[contains(text(),'Create an account')]"}
        self.mobile_create_account = {"xpath": "//button[text()='Create an account']"}
        self.create_account_popup={"id":"ca-panel-modal-body"}
        self.create_account_popup_button={"xpath":"//a[contains(text(),'Create account')]"}
        self.page_title = {"id": "page-title"}
        self.first_name = self.get_input_field_by_label_text("* First name")
        self.last_name = self.get_input_field_by_label_text("* Last name")
        self.date={"xpath":"//div[@id='combodateDiv']/span/select[1]"}
        self.month={"xpath":"//div[@id='combodateDiv']/span/select[2]"}
        self.year={"xpath":"//div[@id='combodateDiv']/span/select[3]"}
        self.title={"xpath":"//label[contains(text(),'Title')]/following::select[1]"}
        self.sex_assigned_at_birth={"xpath":"//label[contains(text(),'Sex assigned at birth')]/following::select[1]"}
        self.gender_identity={"xpath":"//label[contains(text(),'Gender')]/following::select[1]"}
        self.mobile=self.get_input_field_by_label_text("* Mobile")
        self.email=self.get_input_field_by_label_text("* Student email")
        self.password={"xpath":"//label[contains(text(),'Password')]/following::input[@type='password' and @data-val-required][1]"}
        self.confirm_password={"xpath":"//label[contains(text(),'Confirm password')]/following::input[@type='password' and @data-val-required][1]"}
        self.accept_policy_checkbox={"xpath":"//input[@type='checkbox' and contains(@aria-labelledby, 'PLEASE_CONFIRM')]"}
        self.privacy_policy_new={"xpath":"//label[contains(text(), 'Please confirm that you have read')]/preceding-sibling::input[@type='checkbox']"}
        self.mobile_register_button={"xpath":"(//a[@data-button-name='DISP_REGISTER' and span[text()='Register']])[2]"}
        self.desktop_register_button={"xpath":"(//a[@data-button-name='DISP_REGISTER' and span[normalize-space(text())='Register']])"}
        self.success_popup={"xpath":"//h4[span[text()='Success']]"}
        self.close_button={"xpath":"//button[text()='Close']"}
        self.unique_email = f"testuser_{uuid.uuid4().hex[:6]}@example.com"
        self.first_name_value ,self.last_name_value=generate_dummy_names()
        self.phone="07777777777"
        
        self.personal_details_page_title={"xpath":"//h2[contains(text(),'Personal Details')]"}

    def register(self):
        try:
            self.wait_for_element_to_appear(self.accept_cookie_button,timeout=5)
            if self.is_element_displayed(self.accept_cookie_button):
                self.click_element(self.accept_cookie_button)
        except:
            pass 
        if self.platform in ["mobile"]:
            self.click_element(self.mobile_create_account)
            self.wait_for_element_to_appear(self.create_account_popup,timeout=5)
            
            self.click_element(self.create_account_popup_button)
        else:
            self.click_element(self.desktop_create_account)
            self.wait_for_element_to_appear(self.first_name, timeout=10)

        
    def fill_registration_form(self):
        self.select_from_dropdown_by_value(self.title,"MS")
        self.enter_keys(self.first_name,self.first_name_value)
        self.enter_keys(self.last_name,self.last_name_value)
        self.select_from_dropdown_by_value(self.date,"2")
        self.select_from_dropdown_by_value(self.month,"2")
        self.select_from_dropdown_by_value(self.year,"2002")
        self.select_from_dropdown_by_value(self.sex_assigned_at_birth,"F")
        self.select_from_dropdown_by_value(self.gender_identity,"F")
        self.enter_keys(self.email,self.unique_email)
        self.enter_keys(self.mobile,self.phone)
        self.enter_keys(self.password,"Jane1234Kelly")
        self.enter_keys(self.confirm_password,"Jane1234Kelly")
        hide_keyboard(self.driver)
        self.click_element(self.privacy_policy_new)  
        self.wait_for_element_to_appear(self.privacy_policy_new, timeout=5)

    def submit_form(self):
        if self.platform in ["mobile"]:
            hide_keyboard(self.driver)
            self.click_element(self.mobile_register_button)
        else:
            hide_keyboard(self.driver)
            self.click_element(self.desktop_register_button)
        self.wait_for_element_to_appear(self.close_button, timeout=20)
       
    def close_success_popup(self):
        if self.platform in ["mobile"]:
            self.click_element(self.close_button)
            self.wait_for_element_to_appear(self.personal_details_page_title)
        else:
            time.sleep(1)
            self.click_element(self.close_button)
            self.wait_for_element_to_appear(self.personal_details_page_title)
        return PersonalDetailsPage(self.driver)



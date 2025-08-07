from framework import Framework
from pages.contacts import Contacts

class FurtherDetailsPage(Framework):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver 
        self.nationality={"xpath":"//label[contains(text(),'What is your nationality')]/following-sibling::div//select"}
        self.disability={"xpath":"//label[contains(text(),'Do you have a disability or learning difficulty?')]/following-sibling::div//select"}
        self.residency_status={"xpath":"//label[contains(text(),'What is your residency status?')]/following-sibling::div//select"}
        self.lived_in_uk={"xpath":"//label[contains(text(),'Have  you lived in the UK for the last 3 years?')]/following::label[contains(text(),'Yes')][1]"}
        self.time_limit_in_uk={"xpath":"//label[contains(text(),'Is there any time limit of your stay in the UK?')]/following::label[contains(text(),'No')][1]"}
        self.wheelchair_user={"xpath":"//label[contains(text(),'Are you a wheelchair user?')]/following::label[contains(text(),'No')][1]"}
        self.criminal_convictions={"xpath":"//label[contains(text(),'Do you have any prior criminal convictions or cautions?')]/following::label[contains(text(),'No')][1]"}
        self.exclusion_from_school={"xpath":"//label[contains(text(),'Have you had any permanent exclusions from your school?')]/following::label[contains(text(),'No')][1]"}
        self.local_authority_care={"xpath":"//label[contains(text(),'Have you spent any time in local authority care/foster home?')]/following::label[contains(text(),'No')][1]"}
        self.mobile_continue_button={"xpath":"(//a[span[text()='Continue']])[2]"}
        self.desktop_continue_button={"xpath":"(//a[span[text()='Continue']])"}
        self.contacts_title={"xpath":"//h2[contains(text(),'Current Contacts')]"}

        self.lived_in_uk_button={"xpath":"//label[contains(text(),'Have  you lived in the UK for the last 3 years?')]/following::label[contains(text(),'Yes')][1]/following::input"}
        self.time_limit_in_uk_button={"xpath":"//label[contains(text(),'Is there any time limit of your stay in the UK?')]/following::label[contains(text(),'No')][1]/following::input"}
        self.wheelchair_user_button={"xpath":"//label[contains(text(),'Are you a wheelchair user?')]/following::label[contains(text(),'No')][1]/following::input"}
        self.criminal_convictions_button={"xpath":"//label[contains(text(),'Do you have any prior criminal convictions or cautions?')]/following::label[contains(text(),'No')][1]/following::input"}
        self.exclusion_from_school_button={"xpath":"//label[contains(text(),'Have you had any permanent exclusions from your school?')]/following::label[contains(text(),'No')][1]/following::input"}
        self.local_authority_care_button={"xpath":"//label[contains(text(),'Have you spent any time in local authority care/foster home?')]/following::label[contains(text(),'No')][1]/following::input"}
        self.gsce_result={"xpath":"//label[contains(text(),'* Have you recieved your GCSE English and Maths results?')]/following::label[contains(text(),'Yes')][1]/following::input"}


    def fill_further_details_form(self):
        self.select_from_dropdown_by_value(self.nationality,"XF")
        self.select_from_dropdown_by_value(self.residency_status,"BRITISH")
        self.select_from_dropdown_by_value(self.disability,"2")

        self.click_element(self.lived_in_uk)
        self.click_element(self.time_limit_in_uk)
        self.click_element(self.wheelchair_user)
        self.click_element(self.criminal_convictions)
        self.click_element(self.exclusion_from_school)
        self.click_element(self.local_authority_care)

    def submit_form(self):
        if self.platform in ["mobile"]:
            self.click_element(self.mobile_continue_button)
        else:
            self.click_element(self.desktop_continue_button)

        self.wait_for_element_to_appear(self.contacts_title,timeout=3)
        return Contacts(self.driver)

        
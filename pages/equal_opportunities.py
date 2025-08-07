from framework import Framework
from pages.photo_upload_page import PhotoUploadPage

class EqualOpportunitiesPage(Framework):
    def __init__(self, driver):
        super().__init__(driver)
        self.education_healthcare_plan={"xpath":"//label[contains(text(),'currently applying for Education Healthcare Plan (EHCP)?')]/following::label[contains(text(),'No')][1]"}
        self.criminal_convictions={"xpath":"//label[contains(text(),'criminal convictions')]/following::label[contains(text(),'No')][1]"}
        self.social_worker={"xpath":"//label[contains(text(),'Social Worker')]/following::label[contains(text(),'No')][1]"}
        self.mental_health={"xpath":"//label[contains(text(),'mental health')]/following::label[contains(text(),'No')][1]"}
        self.young_carer={"xpath":"//label[contains(text(),'Young Carer')]/following::label[contains(text(),'No')][1]"}
        self.free_school_meals={"xpath":"//label[contains(text(),'Have you recieved free school meals?')]/following::label[contains(text(),'I have not recieved free school meal')]"}
        self.full_time_education={"xpath":"//label[contains(text(),'full-time education or training')]/following::label[contains(text(),'No')][1]"}
        self.ethnicity={"xpath":"//label[contains(text(),'best describes your ethnicity')]/following-sibling::div//select"}
        self.employment_status={"xpath":"//label[contains(text(),'employment status')]/following-sibling::div//select"}
        self.benefits={"xpath":"//label[contains(text(),'Do you recieve any of these benefits')]/following-sibling::div//select"}
        self.highest_qualification={"xpath":"//label[contains(text(),'highest qualification')]/following-sibling::div//select"}
        self.gsce_english_grade={"xpath":"//label[contains(text(),'GCSE English Language Grade')]/following-sibling::div//select"}
        self.gsce_maths_grade={"xpath":"//label[contains(text(),'GCSE Maths Grade')]/following-sibling::div//select"}
        self.achievement_in_english={"xpath":"//label[contains(text(),'achieve 9-4/A*-C in GCSE English')]/following::label[contains(text(),'No')][1]"}
        self.achievement_in_maths={"xpath":"//label[contains(text(),'achieve GCSE Maths at 9-4/A*-C')]/following::label[contains(text(),'No')][1]"}
        self.mobile_continue_button_1={"xpath":"(//a[span[text()='Continue']])[3]"}
        self.mobile_continue_button_2={"xpath":"(//a[span[text()='Continue']])[2]"}
        self.desktop_continue_button={"xpath":"(//a[span[text()='Continue']])"}
        self.update_qualifications_page={"xpath":"//h2[contains(text(),'Update Qualifications')]"}
        self.photo_upload_page={"xpath":"//h1[contains(text(),'Photo Upload')]"}

        self.education_healthcare_plan_button={"xpath":"//label[contains(text(),'currently applying for Education Healthcare Plan (EHCP)?')]/following::label[contains(text(),'No')][1]/following::input"}
        self.criminal_convictions_button={"xpath":"//label[contains(text(),'criminal convictions')]/following::label[contains(text(),'No')][1]/following::input"}
        self.social_worker_button={"xpath":"//label[contains(text(),'Social Worker')]/following::label[contains(text(),'No')][1]/following::input"}
        self.mental_health_button={"xpath":"//label[contains(text(),'mental health')]/following::label[contains(text(),'No')][1]/following::input"}
        self.young_carer_button={"xpath":"//label[contains(text(),'Young Carer')]/following::label[contains(text(),'No')][1]/following::input"}
        self.free_school_meals_button={"xpath":"//label[contains(text(),'Have you recieved free school meals?')]/following::label[contains(text(),'I have not recieved free school meal')]/following::input"}
        self.full_time_education_button={"xpath":"//label[contains(text(),'full-time education or training')]/following::label[contains(text(),'No')][1]/following::input"}
        self.achievement_in_english_button={"xpath":"//label[contains(text(),'achieve 9-4/A*-C in GCSE English')]/following::label[contains(text(),'No')][1]/following::input"}
        self.achievement_in_maths_button={"xpath":"//label[contains(text(),'achieve GCSE Maths at 9-4/A*-C')]/following::label[contains(text(),'No')][1]/following::input"}
        self.gsce_result={"xpath":"//label[contains(text(),'* Have you recieved your GCSE English and Maths results?')]/following::label[contains(text(),'Yes')][1]/following::input"}
        self.language_spoken_at_home={"xpath":"//label[contains(text(),'What language is spoken at home?')]/following::select[1]"}
        self.medications={"xpath":"//label[contains(text(),'Do you receive any medications that need to be taken during attendance at college?')]/following::select[1]"}

    def fill_equal_opportunities(self):
        self.select_from_dropdown_by_value(self.ethnicity,"98")
        self.click_element(self.education_healthcare_plan)
        self.click_element(self.free_school_meals)
        self.click_element(self.criminal_convictions)
        self.click_element(self.social_worker)
        self.click_element(self.mental_health)
        self.click_element(self.young_carer)
        self.select_from_dropdown_by_value(self.language_spoken_at_home,"English")
        self.select_from_dropdown_by_value(self.medications,"N")
        self.click_element(self.full_time_education)
        self.select_from_dropdown_by_value(self.employment_status,"12")
        self.select_from_dropdown_by_value(self.highest_qualification,"4")
        self.click_element(self.gsce_result)
        self.select_from_dropdown_by_value(self.gsce_english_grade,"5")
        self.select_from_dropdown_by_value(self.gsce_maths_grade,"5")
        self.click_element(self.achievement_in_english)
        self.click_element(self.achievement_in_maths)

    def submit_form(self):
        if self.platform in ["mobile"]:
            self.click_element(self.mobile_continue_button_1)
            self.wait_for_element_to_appear(self.update_qualifications_page)
            self.click_element(self.mobile_continue_button_2)
        else:
            self.click_element(self.desktop_continue_button)
            self.wait_for_element_to_appear(self.update_qualifications_page)
            self.click_element(self.desktop_continue_button)
        self.wait_for_element_to_appear(self.photo_upload_page)
        return PhotoUploadPage(self.driver)

from framework import Framework
from pages.consents_page import ConsentsPage
from utils.upload_file import upload_file_to_lambdatest

class EvidencePage(Framework):
    def __init__(self, driver):
        super().__init__(driver)
        self.evidence={"xpath":"//label[contains(text(),'Evidence Type')]/following-sibling::div//select"}
        self.choose_file={"xpath":"//label[contains(text(),'To Upload')]/following::div[2]/input"}
        self.upload_button={"xpath":"(//a[span[text()='Upload']])"}
        self.success_popup={"xpath":"//h4[span[text()='Success']]"}
        self.close_button={"xpath":"//button[text()='Close']"}
        self.mobile_continue_button={"xpath":"(//a[span[text()='Continue']])[2]"}
        self.desktop_continue_button={"xpath":"(//a[span[text()='Continue']])"}
        self.evidence_row={"xpath":"//table[@data-control='datagrid' and @role='grid']//tbody//tr"}
        self.file_name="C:\\Users\\srujana.prabhu\\Pictures\\Screenshots\\myimages\\desktop.png"
        self.consents_page={"xpath":"//h2[contains(text(),'Consents')]"}
        self.file_path="C:\\Users\\srujana.prabhu\\Pictures\\Screenshots\\myimages\\desktop.png"

    def fill_evidence(self):
        self.select_from_dropdown_by_value(self.evidence,"EHCP")
        self.enter_keys(self.choose_file,self.file_path)
        self.click_element(self.upload_button)

    def submit_form(self):
        if self.platform in ["mobile"]:
            self.wait_for_element_to_appear(self.evidence_row, timeout=10)
            self.wait_for_element_to_appear(self.mobile_continue_button)
            self.click_element(self.mobile_continue_button)
        else:
            self.wait_for_element_to_appear(self.evidence_row, timeout=10)
            self.wait_for_element_to_appear(self.mobile_continue_button)
            self.click_element(self.desktop_continue_button)
        self.wait_for_element_to_appear(self.consents_page)
        return ConsentsPage(self.driver)

        
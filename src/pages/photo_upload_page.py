from framework import Framework
from pages.evidence_page import EvidencePage
from selenium.webdriver.support.ui import WebDriverWait
import time
 
class PhotoUploadPage(Framework):
    def __init__(self, driver):
        super().__init__(driver)
        self.choose_file={"id":"images"}
        self.save_button={"xpath":"(//a[span[text()='Save']])"}
        self.success_popup={"xpath":"//h4[span[text()='Success']]"}
        self.close_button={"xpath":"//button[text()='Close']"}
        self.mobile_continue_button={"xpath":"(//a[span[text()='Continue']])[2]"}
        self.desktop_continue_button={"xpath":"(//a[span[text()='Continue']])"}
        self.evidence_page={"xpath":"//h1[contains(text(),'Evidence')]"}
        self.local_file_path="C:\\Users\\srujana.prabhu\\Pictures\\Screenshots\\myimages\\desktop.png"
        self.android_path="//android.widget.TextView[@text='desktop.png']"

    def wait_for_condition(self, condition_fn, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda driver: condition_fn(driver))

    def fill_photo_upload(self):
        self.enter_keys(self.choose_file,self.local_file_path)
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.choose_file)
        self.click_element(self.save_button)
        time.sleep(1)
        self.wait_for_element_to_appear(self.close_button, timeout=10)
        self.click_element(self.close_button)

    def submit_form(self):
        if self.platform in ["mobile"]:
            self.click_element(self.mobile_continue_button)
        else:
            self.click_element(self.desktop_continue_button)
        self.wait_for_element_to_appear(self.evidence_page)
        return EvidencePage(self.driver)


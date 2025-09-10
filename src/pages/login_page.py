from framework import Framework
from ..utils.hide_keyboard import hide_keyboard

class LoginPage(Framework):
    def __init__(self, driver):
        super().__init__(driver)
        self.username={"xpath":"//input[@id='user-name']"}
        self.password={"xpath":"//input[@id='password']"}
        self.login_button={"xpath":"//input[@id='login-button']"}
        self.products_catalog_page={"xpath":"//div[contains(text(),'Products')]"}

    def login(self):
        self.enter_keys(self.username,"standard_user")
        self.enter_keys(self.password,"secret_sauce")
        hide_keyboard(self.driver)
        self.click_element(self.login_button)
        


    

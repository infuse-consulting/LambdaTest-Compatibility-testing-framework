from framework import Framework

class LoginPage(Framework):
    def __init__(self, driver):
        super().__init__(driver)
        self.username="//input[@id='user-name']"
        self.password="//input[@id='password']"
        self.login_button="//input[@id='login-button']"

    def login(self):
        self.enter_keys(self.username,"standard_user")
        self.enter_keys(self.password,"secret_sauce")
        self.click_element(self.login_button)


    

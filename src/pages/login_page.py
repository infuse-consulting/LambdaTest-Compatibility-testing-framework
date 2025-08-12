from framework import Framework

class LoginPage(Framework):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver 
        self.email = {"id": "user-name"}
        self.password = {"id": "password"}
        self.submit_button={"id":"login-button"}

    def login(self,email,password):
        self.enter_keys(self.email, email)
        self.enter_keys(self.password, password)
        self.click_element(self.submit_button)

        
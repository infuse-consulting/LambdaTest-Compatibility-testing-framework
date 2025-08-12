import pytest
from src.pages.login_page import LoginPage
from src.utils.projectUtils import Utils

@pytest.mark.usefixtures("driver", "dataLoad")
def test_course_registration_for_student(driver, dataLoad):
    _, _, url = dataLoad
    driver.get(url)
    login_page = LoginPage(driver)
    assertion=Utils(driver)
    login_page.login()
    # assertion.assert_page_is_displayed()

import pytest
from src.pages.register_page import RegisterPage
from src.utils.projectUtils import Utils

@pytest.mark.usefixtures("driver", "dataLoad")
def test_course_registration_for_student(driver, dataLoad):
    _, _, url = dataLoad
    driver.get(url)
    resgister_page = RegisterPage(driver)
    assertion=Utils(driver)

    resgister_page.register()
    assertion.assert_page_is_displayed(resgister_page.page_title,"Register")
    resgister_page.fill_registration_form()
    assertion.assert_checkbox_selected(resgister_page.privacy_policy_new, "Privacy policy checkbox")
    resgister_page.submit_form()
    personal_details_page=resgister_page.close_success_popup()
    personal_details_page.fill_personal_details()
    further_details_page=personal_details_page.submit_form()
    assertion.assert_page_is_displayed(personal_details_page.residency_title,"Further details")

    further_details_page.fill_further_details_form()
    contact_page=further_details_page.submit_form()
    assertion.assert_page_is_displayed(further_details_page.contacts_title,"Current Contacts")

    contact_page.fill_contact_details_form()
    data_protection=contact_page.submit_form()
    data_protection.fill_data_protection()
    equal_opportunities_page=data_protection.submit_form()
    assertion.assert_page_is_displayed(data_protection.opportunities_title,"Equal Opportunities")

    equal_opportunities_page.fill_equal_opportunities()
    photo_upload_page=equal_opportunities_page.submit_form()
    assertion.assert_page_is_displayed(equal_opportunities_page.photo_upload_page,"Photo Upload")

    photo_upload_page.fill_photo_upload()
    evidence_page=photo_upload_page.submit_form()
    assertion.assert_page_is_displayed(photo_upload_page.evidence_page,"Evidence")

    evidence_page.fill_evidence()
    assertion.assert_element_visible(evidence_page.evidence_row,"Evidence file name")
    consents_page=evidence_page.submit_form()
    assertion.assert_page_is_displayed(evidence_page.consents_page,"Consents")

    consents_page.fill_Consents()
    assertion.assert_checkbox_selected(consents_page.agree_checkbox_button,"I Agree consents")
    consents_page.submit_form()
    consents_page.close_success_popup()
    
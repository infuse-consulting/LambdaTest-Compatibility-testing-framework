

def test_login(setup):
    login_page, assertion, url = setup
    login_page.navigate_to_page(url)
    login_page.login()
    assertion.assert_page_is_displayed(login_page.products_catalog_page,"Products Catalog Page")

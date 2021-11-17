link = "http://selenium1py.pythonanywhere.com/"


def test_user_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


def test_user_should_see_fail_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")



from playwright.sync_api import Page


def test_multiplexecution(page:Page):
    browser=page.context.browser
    context1=browser.new_context()
    page1=context1.new_page()
    page1.goto("https://automationexercise.com/")
    page1.get_by_role("link", name=" Signup / Login").click()
    page1.get_by_placeholder("Email Address").first.fill("playwrightpython1234@gmail.com")
    page1.get_by_placeholder("Password").fill("Test@123")
    page1.get_by_role("button", name="Login").click()
    page1.wait_for_timeout(3000)

    context2=browser.new_context()
    page2=context2.new_page()
    page2.goto("https://automationexercise.com/")
    page2.get_by_role("link", name=" Signup / Login").click()
    page2.get_by_placeholder("Email Address").first.fill("playwrightpython1234@gmail.com")
    page2.get_by_placeholder("Password").fill("Test@123")
    page2.get_by_role("button", name="Login").click()
    page2.wait_for_timeout(3000)
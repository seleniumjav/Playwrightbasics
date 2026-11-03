from playwright.sync_api import Page

from Login import Login


def test_loginverify(page:Page):
    log=Login(page)
    log.openUrl("https://automationexercise.com/")
    log.loginclick()
    log.loginsubmit("playwrightpython1234@gmail.com","Test@123")
    page.wait_for_timeout(3000)


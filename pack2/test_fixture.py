import pytest
from playwright.sync_api import Page



def test_login(page:Page):
    page.goto("https://tutorialsninja.com/demo/")
    page.get_by_title("My Account").click(timeout=10000)
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("E-Mail Address").fill("seleniumpython@gmail.com")
    page.get_by_placeholder("Password").fill('Selenium@2026')
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(3000)
    page.close()




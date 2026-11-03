import pytest
from playwright.sync_api import Page


class TestPage:
    def test_product(self,page:Page):
        page.goto("https://tutorialsninja.com/demo/")
        page.locator('(//a[@href="https://tutorialsninja.com/demo/index.php?route=product/product&product_id=43"])[2]').click()
        page.locator('#button-cart').click()
        page.get_by_role("link",name="shopping cart").click()
        page.wait_for_timeout(3000)
        page.close()

    def test_login(self,page: Page):
        page.goto("https://tutorialsninja.com/demo/")
        page.get_by_title("My Account").click(timeout=10000)
        page.get_by_role("link", name="Login").click()
        page.get_by_placeholder("E-Mail Address").fill("seleniumpython@gmail.com")
        page.get_by_placeholder("Password").fill('Selenium@2026')
        page.get_by_role("button", name="Login").click()
        page.wait_for_timeout(3000)
        page.close()

class TestLogin:
    def test_fileupload(self,page: Page):
        page.goto("https://practice.expandtesting.com/upload")
        with page.expect_file_chooser() as file:
            page.locator('#fileInput').click()

        filevalue = file.value
        filevalue.set_files("C:\\Users\\Admin\\Desktop\\Userdata.csv")
        page.locator("#fileSubmit").click()

        page.wait_for_timeout(3000)
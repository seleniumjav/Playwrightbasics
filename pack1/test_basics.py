import time

from playwright.sync_api import Page, expect, Playwright

def test_demo(page:Page,playwright:Playwright):

    page.goto("https://tutorialsninja.com/demo/")
    expect(page).to_have_url("https://tutorialsninja.com/demo/")
    time.sleep(2)

def test_verifytitle(page:Page):
    page.goto("https://tutorialsninja.com/demo/")
    expect(page).to_have_title("Your Store")
    time.sleep(2)


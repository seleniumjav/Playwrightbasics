from playwright.sync_api import Page


def test_reuseui(page:Page):
    context=page.context.browser.new_context(storage_state="state.json")
    page=context.new_page()
    page.goto("https://automationexercise.com/")
    page.get_by_role("link",name="Logout").click()
    page.wait_for_timeout(3000)

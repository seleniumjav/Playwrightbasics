import time

from playwright.sync_api import Playwright, Page


def test_apiregister(playwright:Playwright,page:Page):
    email = f"playwright{int(time.time())}@gmail.com"
    password = "Test@12345"

    # post
    request = playwright.request.new_context()
    url = "https://automationexercise.com/api/createAccount"

    response = request.post(
        url=url,
        form={
            "name": "Playwright123456789",
            "email": email,
            "password": password,
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "8",
            "birth_year": "1998",
            "firstname": "Rahul",
            "lastname": "Sharma",
            "company": "ABC Technologies",
            "address1": "123 MG Road",
            "address2": "Near City Center",
            "country": "India",
            "zipcode": "560001",
            "state": "Karnataka",
            "city": "Bengaluru",
            "mobile_number": "9876543210"
        }
    )
    print("Status", response.status)
    print("Response", response.text())

    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name=" Signup / Login").click()
    page.get_by_placeholder("Email Address").first.fill(email)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(3000)

    page.context.storage_state(path="state.json")
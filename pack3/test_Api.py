import csv
import time

from playwright.sync_api import Playwright


def test_get(playwright:Playwright):
    request=playwright.request.new_context()
    url="https://automationexercise.com/api/productsList"
    response=request.get(url)
    assert response.status==200

    productlist=response.json()
    assert len(productlist)>0

    first=productlist["products"][13]
    # for product in first:
    #     print(product)

    assert isinstance(first['id'],int)

    usertype=first["category"]["usertype"]["usertype"]
    assert usertype in ["Men","Women","Kids"]

def test_post(playwright:Playwright):
    request=playwright.request.new_context()
    url="https://automationexercise.com/api/createAccount"

    response=request.post(
        url=url,
        form={
          "name": "Playwright123456789",
          "email": f"playwright{int(time.time())}@gmail.com",
          "password": "Test@12345",
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
    print("Status",response.status)
    print("Response",response.text())

def test_getlogin(playwright:Playwright):
    request=playwright.request.new_context()
    url="https://automationexercise.com/api/verifyLogin"

    response=request.post(
        url=url,
        form={
            "email": "rahul.s6@example.com",
            "password": "Test@12345",
        }
    )

    print("Status",response.status)
    print("Response",response.text())


def read_data(path):
    file=open(path,"r",encoding="utf-8")
    return list(csv.DictReader(file))

def test_csvdata(playwright:Playwright):
    request=playwright.request.new_context()
    url="https://automationexercise.com/api/createAccount"

    users=read_data("Userdata.csv")

    for user in users:
        response=request.post(
            url=url,
            form={
                "name":user["name"],
                "email":user["email"],
                "password":user["password"],
                "title":user["title"],
                "birth_date":user["birth_date"],
                "birth_month":user["birth_month"],
                "birth_year":user["birth_year"],
                "firstname":user["firstname"],
                "lastname":user["lastname"],
                "company":user["company"],
                "address1":user["address1"],
                "address2":user["address2"],
                "country":user["country"],
                "zipcode":user["zipcode"],
                "state":user["state"],
                "city":user["city"],
                "mobile_number":user["mobile_number"],
            }
        )

        print(response.status)
        print("Response",response.text())


def test_Apitest(playwright:Playwright):
    email=f"playwright{int(time.time())}@gmail.com"
    password="Test@12345"

    #post
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
    #Put
    updateuser=request.put(
        url="https://automationexercise.com/api/updateAccount",
        form={
            "name": "Playwright123456789",
            "email": email,
            "password": password,
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "8",
            "birth_year": "1998",
            "firstname": "Rahul updated",
            "lastname": "Sharma updated",
            "company": "ABC Technologies updated",
            "address1": "123 MG Road",
            "address2": "Near City Center",
            "country": "India",
            "zipcode": "560001",
            "state": "Karnataka",
            "city": "Bengaluru",
            "mobile_number": "9876543210"
        }
    )
    print("Status",updateuser.status)
    print("Response", updateuser.text())

    #Get
    getuser=request.get(
        url="https://automationexercise.com/api/getUserDetailByEmail",
        params={
            "email": email
        }
    )
    print("Details",getuser.text())
    print("Status", getuser.status)

    #Delete
    deleteuser=request.delete(
        url="https://automationexercise.com/api/deleteAccount",
        form={
            "email": email,
            "password": password
        }
    )
    print("Status",deleteuser.status)
    print("Response", deleteuser.text())

    getuser = request.get(
        url="https://automationexercise.com/api/getUserDetailByEmail",
        params={
            "email": email
        }
    )
    print("Details", getuser.text())
    print("Status", getuser.status)

def test_authentication(playwright:Playwright):
    token="74a78baa310e7d706aad723a8e429348ba0f2efa605bcd0a9fa926c3ec54ace1"
    api=playwright.request.new_context(
        base_url="https://gorest.co.in/public/v2/users",
        extra_http_headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/json"
        }
    )

    response=api.get(
        url="https://gorest.co.in/public/v2/users",
    )

    print("Status",response.status)
    print("Response", response.text())
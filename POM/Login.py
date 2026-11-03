class Login:
    def __init__(self,page):
        self.page = page
        self.login=page.get_by_role("link", name=" Signup / Login")
        self.email=page.get_by_placeholder("Email Address").first
        self.password=page.get_by_placeholder("Password")
        self.loginbtn=page.get_by_role("button", name="Login")

    def openUrl(self,url):
        self.page.goto(url)

    def loginclick(self):
        self.login.click()

    def loginsubmit(self,email,password):
        self.email.fill(email)
        self.password.fill(password)
        self.loginbtn.click()


from project.pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,page):
       super().__init__(page)
    def login(self,email,password):
        self.page.get_by_role("textbox",name="username").fill(email)
        self.page.get_by_role("textbox",name="password").fill(password)
        self.page.locator("button").click()
        self.page.screenshot(path="login_Attempt.png")
    #return Dashboard_page(self.page)
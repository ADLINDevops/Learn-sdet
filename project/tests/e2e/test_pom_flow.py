import pytest
def test_login_to_dashboard():
    from project.pages.Login_page import LoginPage
    from playwright.sync_api import sync_playwright
    #from playwright.sync_api import Page
    @pytest.fixture #doesnot manually close the browser
    def page():
     with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        pages=browser.new_page()
        pages.goto("https://the-internet.herokuapp.com/login")
        login_page=LoginPage(pages)
        #url="https://the-internet.herokuapp.com/login"
        
        dashboard=login_page.login("tomsmith","SuperSecretPassword!")
     import requests
     user_response=requests.get("https://jsonplaceholder.typicode.com")
     assert user_response.status_code==200
     browser.close()
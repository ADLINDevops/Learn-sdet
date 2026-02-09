def test_mocked_api():
    from tests.pages.Login_page import LoginPage
    from unittest.mock import patch

    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value={"valid":True}
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
                browser=p.chromium.launch(headless=True)
                page=browser.new_page()
                page.goto("https://the-internet.herokuapp.com/login")
                login=LoginPage(page)
                login.login("e2e@gmail.com","test")
                assert page.locator("h1").is_visible()
                browser.close()
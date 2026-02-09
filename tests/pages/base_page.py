from playwright.sync_api import Page # type: ignore

class BasePage:
    def __init__(self,page:Page):
        self.page=page
    def navigate(self,url):
        self.page.goto(url,timeout=30000)
    def take_screenshot(self,name):
        self.page.screenshot(path=f"image/{name}.png")



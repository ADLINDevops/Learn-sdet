from playwright.sync_api import sync_playwright
#import synchronous version of python
#ASync-handles thousands of pages at once, sync- perfect for standard test suites
def test_example_browser():#tells pytest as testcase
    with sync_playwright() as p:#contextmanager-> starts playwright engine and closes 
        #automatically when code inside finishes/crashes
        browser=p.chromium.launch(headless=False)#browser manager-opens the browser in
        #new window, headless=True->runs invisibly and faster
        page=browser.new_page()#incognito tab.No cookies, no history
        page.goto("https://example.com")
        title=page.locator("h1").inner_text()
        assert title=="Example Domain"
        page.screenshot(path="Screenshots/browser.png")
        print("Browser launched.Test Passed")
        browser.close()
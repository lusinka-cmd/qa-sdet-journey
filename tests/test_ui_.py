from playwright.sync_api import sync_playwright

def test_search_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com")

        # search input
        page.fill("textarea[name='q']", "Playwright")

        # press Enter
        page.press("textarea[name='q']", "Enter")

        # wait a bit
        page.wait_for_timeout(3000)

        # check result
        assert "Playwright" in page.title()

        browser.close()
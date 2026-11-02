from playwright.sync_api import sync_playwright


def test_website_title():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://example.com")

        assert page.title() == "Example Domain"  # This assertion is intentionally incorrect to demonstrate a failing test

        browser.close()
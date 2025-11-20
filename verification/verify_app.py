
import os
import re
from playwright.sync_api import Page, expect, sync_playwright

def verify_app(page: Page):
    # Load the file
    cwd = os.getcwd()
    page.goto(f"file://{cwd}/index.html")

    # Check title
    expect(page).to_have_title("Голосовой калькулятор")

    # Screenshot 1: Calculator View (Default)
    page.screenshot(path="verification/1_calculator_light.png")

    # Open Menu
    page.click("#menuBtn")
    expect(page.locator("#drawer")).to_have_class(re.compile(r"open"))

    # Screenshot 2: Menu Open
    # Wait a bit for animation
    page.wait_for_timeout(300)
    page.screenshot(path="verification/2_menu_open.png")

    # Navigate to Settings
    page.click("button[onclick=\"app.navigate('settings')\"]")
    # Verify settings view is active
    expect(page.locator("#view-settings")).to_have_class(re.compile(r"active"))

    # Screenshot 3: Settings View
    page.wait_for_timeout(300)
    page.screenshot(path="verification/3_settings_light.png")

    # Switch to Dark Theme
    page.click("#themeDark")

    # Verify dark theme attribute
    expect(page.locator("html")).to_have_attribute("data-theme", "dark")

    # Screenshot 4: Settings Dark
    page.screenshot(path="verification/4_settings_dark.png")

    # Navigate to About
    page.click("#menuBtn")
    page.click("button[onclick=\"app.navigate('about')\"]")

    # Screenshot 5: About Page Dark
    page.wait_for_timeout(300)
    page.screenshot(path="verification/5_about_dark.png")

    # Navigate back to Calculator
    page.click("#menuBtn")
    page.click("button[onclick=\"app.navigate('calc')\"]")

    # Screenshot 6: Calculator Dark
    page.wait_for_timeout(300)
    page.screenshot(path="verification/6_calculator_dark.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_app(page)
        finally:
            browser.close()

from playwright.sync_api import sync_playwright, expect
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Load the page
    page.goto(f"file://{os.path.abspath('index.html')}")

    # Check for Add Player in Sidebar
    # Open Sidebar first
    page.click("#menuBtn")
    # Wait for sidebar to open
    page.wait_for_selector(".side-drawer.open")

    add_btn = page.locator("#addPlayerBtn")
    expect(add_btn).to_be_visible()

    # Check Dark Mode Toggle
    theme_btn = page.locator("#toggleThemeBtn")
    expect(theme_btn).to_be_visible()

    # Toggle Theme
    theme_btn.click()
    # Verify dark mode attribute
    expect(page.locator("html")).to_have_attribute("data-theme", "dark")

    # Take screenshot of Sidebar with Dark Mode
    page.screenshot(path="verification/sidebar_dark.png", full_page=True)

    # Add a player and verify no nickname
    page.fill("#usernameInput", "TestPlayer")
    add_btn.click()
    page.click("#closeDrawerBtn") # Close drawer to see list

    # Wait for player
    expect(page.locator(".p-name").first).to_have_text("TestPlayer")

    # Verify NO rank badge
    expect(page.locator(".rank-badge")).not_to_be_visible()

    # Take screenshot of list
    page.screenshot(path="verification/list_view.png", full_page=True)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)

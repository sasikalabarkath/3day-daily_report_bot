

import asyncio

from playwright.sync_api import sync_playwright


browser = sync_playwright().start().chromium.launch(headless=True)
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    page.goto("https://www.google.com")
    page.screenshot(path="google.png")
    browser.close() 

    'navigation to weather forecast website'
    page.goto("https://www.weather-forecast.com/locations/Chennai/forecasts/latest")
    page.screenshot(path="chennai.png")

    'click on the full forecast link'
    page.click('text=hourly ')
    page.screenshot(path="forecast.png")

    'typing'
    page.fill('input[name="q"]', 'playwright python')
    page.press('input[name="q"]', 'Enter')
    page.screenshot(path="search_results.png")

    'waiting for an element to be visible'
    page.wait_for_selector('text=Playwright for Python')
    page.screenshot(path="playwright_python.png")


    'extracting data from the page'
    title = page.title()
    print(f"Page title: {title}")
    browser.close()

   
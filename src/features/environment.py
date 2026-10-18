from playwright.sync_api import sync_playwright
from pages.base_page import BasePage


def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)
    context.page = context.browser.new_page()
    context.base_page = BasePage(context.page)


def after_scenario(context, scenario):
    context.browser.close()
    context.playwright.stop()

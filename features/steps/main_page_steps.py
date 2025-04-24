from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open the main page soft.reelly.io')
def open_reelly_page(context):
    context.app.main_page.open_reelly_page()
    context.app.main_page.click_sign_in()
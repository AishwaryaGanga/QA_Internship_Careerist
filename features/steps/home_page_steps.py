from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on “off plan” at the left side menu.')
def click_on_off_plan_menu(context):
    # context.app.home_page.click_on_off_plan_menu()
    context.app.home_page.click_on_mobile_off_plan_menu()
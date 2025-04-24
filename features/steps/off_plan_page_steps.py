from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify the right page opens.')
def verify_off_plan_page_opens(context):
    context.app.off_plan_page.verify_off_plan_page_opens()

@then('Verify each product on this page contains a title and picture visible.')
def verify_products_title_and_images(context):
    context.app.off_plan_page.verify_products_title_and_images()
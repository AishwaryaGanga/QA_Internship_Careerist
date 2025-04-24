from selenium.webdriver.common.by import By
from behave import given, when, then



@given('Log in to the page.')
def sign_in_login_page(context):
    context.app.sign_in_page.input_crendentials()
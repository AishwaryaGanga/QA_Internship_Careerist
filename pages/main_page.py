from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

class MainPage(Page):
    SIGN_IN_LINK = (By.CSS_SELECTOR, "[wized = 'signinButtonSignup']")


    def open_reelly_page(self):
        self.open_url(self.base_url)
        sleep(3)

    def click_sign_in(self):
        self.click(*self.SIGN_IN_LINK)
        sleep(3)
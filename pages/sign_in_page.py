from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(Page):

    EMAIL = (By.ID, "email-2")
    PASSWORD = (By.ID, "field")
    CONTINUE = (By.CSS_SELECTOR, "[wized = 'loginButton']")


    def input_crendentials(self):
        self.input_text('aishwaryaganga.s@gmail.com', *self.EMAIL)
        self.input_text('Test123', *self.PASSWORD)
        self.click(*self.CONTINUE)


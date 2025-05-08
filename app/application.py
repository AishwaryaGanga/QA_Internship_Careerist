from pages.base_page import Page
from pages.off_plan_page import OffPlanPage
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.home_page import HomePage

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.off_plan_page = OffPlanPage(self.driver)

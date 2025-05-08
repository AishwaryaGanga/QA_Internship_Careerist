from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class HomePage(Page):

    OFF_PLAN = (By.XPATH, "//a[@href='/off-plan']//div[@class='div-block-121']//div[@class='g-menu-text'][normalize-space()='Off-plan']" )
    MOBILE_OFF_PLAN = (By.CSS_SELECTOR, "a[wized='newOffPlanLink'] div[class='menu-text']")

    def click_on_off_plan_menu(self):
        self.click(*self.OFF_PLAN)

    def click_on_mobile_off_plan_menu(self):
        self.clicks(*self.MOBILE_OFF_PLAN)
        # self.wait.until(
        #     EC.element_to_be_clickable(self.MOBILE_OFF_PLAN),
        #     message=f'Element not clickable by {self.MOBILE_OFF_PLAN}'
        # ).click()
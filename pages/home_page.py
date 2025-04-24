from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class HomePage(Page):

    OFF_PLAN = (By.XPATH, "//a[@href='/off-plan']//div[@class='div-block-121']//div[@class='g-menu-text'][normalize-space()='Off-plan']" )

    def click_on_off_plan_menu(self):
        self.click(*self.OFF_PLAN)
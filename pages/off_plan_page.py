from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

class OffPlanPage(Page):

    PROD_LISTING = (By.CSS_SELECTOR, "[wized ='cardOfProperty']")
    PROD_TITLES = (By.CSS_SELECTOR, ".project-name")
    PROD_IMAGES = (By.CSS_SELECTOR, ".project-image")

    def verify_off_plan_page_opens(self):
        page = self.base_url + "/off-plan"
        sleep(3)
        print(page)

    def verify_products_title_and_images(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(3)

        products = self.find_elements(*self.PROD_LISTING)

        for product in products:
            names = product.find_element(*self.PROD_TITLES).text
            assert names, 'Product name not found'
            print("Product names: ", names)

            product.find_elements(*self.PROD_IMAGES)




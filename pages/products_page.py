from pages.base_page import BasePage 
from locators.locator_login import Locators



class Products(BasePage):
    
    def category(self):
        self.page.locator(Locators.product).click()
        self.page.locator(Locators.product_search).fill("Dresses")
        self.page.locator(Locators.search_button).click()
        self.page.wait_for_timeout(3000)
        
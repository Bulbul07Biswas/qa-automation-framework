from pages.base_page import BasePage
from locators.locator_login import Locators
from playwright.sync_api import expect


class HomePage(BasePage):
    
    def homepage_carousel(self):
        self.page.locator(Locators.Test_cases_button).click()
        expect(self.page.locator(Locators.Test_case_text)).to_have_text('Below is the list of test Cases for you to practice the Automation. Click on the scenario for detailed Test Steps:')
        
    def test_case_page(self):
        self.page.locator(Locators.Test_case_Register_user).click()
        expect(self.page.locator(Locators.Test_Register_user_cases)).to_have_text('1. Launch browser')
        self.page.locator("#collapse1").get_by_text("Launch browser").click()



        
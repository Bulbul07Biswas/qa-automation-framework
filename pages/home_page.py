from pages.base_page import BasePage
from locators.locator_login import Locators
from playwright.sync_api import expect
from pages.login_page import LoginPage 


class HomePage(BasePage):
    
    def homepage_carousel(self):
        self.page.locator(Locators.home_popup)
        self.page.locator(Locators.Test_cases_button).click()
        self.page.wait_for_timeout(3000)
        expect(self.page.locator(Locators.Test_case_text)).to_have_text('Below is the list of test Cases for you to practice the Automation. Click on the scenario for detailed Test Steps:')
        
    def test_case_page(self):
        # self.page.locator(Locators.home_popup).click()
        self.page.locator(Locators.Test_case_Register_user).click()
        expect(self.page.locator(Locators.Test_Register_user_cases)).to_have_text('1. Launch browser')
        # self.page.wait_for_timeout(2000)
        self.page.locator("#collapse1").get_by_text("Launch browser").click()
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        subscription_scroll= self.page.locator(Locators.Test_Subscription_email)
        subscription_scroll.scroll_into_view_if_needed()
        # self.page.wait_for_timeout(3000)
        subscription_scroll.fill("bulbul07@gammaedge.com")
        # self.page.wait_for_timeout(2000)
        self.page.locator(Locators.Test_Subscription_submit).click()
        expect(self.page.locator(Locators.Test_toast_sucess_msg)).to_be_visible()        
    



        
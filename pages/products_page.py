from pages.base_page import BasePage 
from locators.locator_login import Locators
from playwright.sync_api import expect



class Products(BasePage):
    
    def category(self):
        self.page.locator(Locators.product).click()
        self.page.locator(Locators.product_search).fill("Dresses")
        self.page.locator(Locators.search_button).click()
        self.page.wait_for_timeout(3000)
        
        
    def saree(self):
        self.page.locator(Locators.women_catagory).click()
        self.page.get_by_role("link",name=Locators.saree_link).click()
        heading=self.page.get_by_text(Locators.saree_homepage)
        expect(heading).to_be_visible()
        #yaha humne locator ko var m store karwaya hai and uspr expect and 
        text=heading.inner_text()
        print(text)
        cotton_saree=self.page.get_by_text(Locators.saree_cotton_silk).first
        cotton_saree.scroll_into_view_if_needed()
        cotton_saree.hover()
        add_to_cart=self.page.get_by_text(Locators.add_to_cart).first
        add_to_cart.click()
        self.page.wait_for_timeout(2000)        
        expect(self.page.get_by_text(Locators.added_popup)).to_be_visible()
        self.page.get_by_text(Locators.view_cart_text).click()
        self.page.wait_for_timeout(2000)
        
        
    def checkout(self):
        self.page.get_by_text(Locators.checkout_proceed).click()
        comment=self.page.locator(Locators.add_comment)
        expect(comment).to_be_visible(timeout=5000)
        comment.scroll_into_view_if_needed()
        comment.fill("The product quality is amazing")
        self.page.get_by_text(Locators.place_order).click()
        self.page.wait_for_timeout(4000)
        
        
    def payment(self):
        card=self.page.locator(Locators.card_name)
        expect(card).to_be_visible(timeout=2000)
        card.fill('Bulbul')
        self.page.wait_for_selector(Locators.card_number)
        self.page.locator(Locators.card_number).fill("123456")
        self.page.locator(Locators.cvc).fill("90")
        self.page.locator(Locators.expire_date).fill("12/12")        
        self.page.locator(Locators.expire_year).fill("2009")
        self.page.screenshot(path="screenshot.png")
        self.page.locator(Locators.confirm_order).click()
        self.page.wait_for_timeout(3000)
        self.page.screenshot(path="sceenshot.png")
        # notification=self.page.locator(Locators.success_notification)
        # notification.wait_for(state="visible", timeout=10000)                      
        # expect(notification).to_have_text("Your order has been placed successfully!")
        # notification = self.page.get_by_text("Your order has been placed successfully!", exact=True)
        # expect(notification).to_be_hidden()        
        

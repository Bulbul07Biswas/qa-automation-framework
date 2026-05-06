
from locators.locator_login import Locators
from playwright.sync_api import expect
from utils.read_data import read_json 

class BasePage:


 def __init__(self, page):    
    self.page= page
#Step 2-Page is stored or initialiaze, this is constructor 
# so jaise hi object banta hai ye automatically run hoga, 
# Jo step1 se page mila hai wo issele raha hai


 def valid_login(self, email, password):
      self.page.locator(Locators.Signup_login).click()
      
      expect(self.page.locator(Locators.User_email)).to_be_visible()

      email_field = self.page.locator(Locators.User_email)
      email_field.clear()
      email_field.fill(email)

      password_field = self.page.get_by_placeholder(Locators.User_password)
      password_field.clear()
      password_field.fill(password)
      
      self.page.locator(Locators.Login_button).click()
      
 def invalid_login(self, email, password):
     self.page.locator(Locators.Signup_login).click()
        
     expect(self.page.locator(Locators.User_email)).to_be_visible()
        
     email_field= self.page.locator(Locators.User_email)
     email_field.clear()
     email_field.fill(email)
    
     password_field= self.page.get_by_placeholder(Locators.User_password)
     password_field.clear()
     password_field.fill(password)
     self.page.locator(Locators.Login_button).click()
     print("Invalid login attempt! Pls try with valid credentials")
        
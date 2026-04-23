# Step 3- isme page wise class and function banana hai, yaha hmne 
# step 2 mai jo page bnaya tha usme url opn kar rhe hai
#yaha hum locators ki activity perform krte hai like click , opn dropdown like activity

from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.locator_login import Locators

class LoginPage(BasePage):
    
#   def navigate(self):
#     self.page.goto("https://automationexercise.com/")
    
    
  def valid_login(self,email,password):
      self.page.locator(Locators.Signup_login).click()
    #   self.page.wait_for_timeout(1000)
      
      expect(self.page.locator(Locators.User_email)).to_be_visible()
      email_field=self.page.locator(Locators.User_email)
      email_field.clear()
      email_field.fill(email) 

      password_field=self.page.get_by_placeholder(Locators.User_password)
      password_field.clear()
      password_field.fill(password)
      
      self.page.locator(Locators.Login_button).click()
    
  def login_successfull(self):
      logout= self.page.get_by_role("link", name='Logout')
      
      try:
          expect(logout).to_be_visible(timeout=5000)
          print("Login succesfull")
      except:
          print("Invalid attempt")
       
        
    
    
      
      
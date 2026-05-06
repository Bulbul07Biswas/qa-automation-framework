# Step 3- isme page wise class and function banana hai, yaha hmne 
# step 2 mai jo page bnaya tha usme url opn kar rhe hai
#yaha hum locators ki activity perform krte hai like click , opn dropdown like activity

from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.locator_login import Locators
from utils.read_data import read_json 

class LoginPage(BasePage):
  

  def login_successfull(self):
      logout= self.page.get_by_role("link", name='Logout')
      
      try:
          expect(logout).to_be_visible(timeout=5000)
          print("Login succesfull")
      except:
          print("Invalid attempt")
       
  def login_failed(self):
      expect(self.page.locator(Locators.invalid_login_msg)).to_be_visible()
      
      
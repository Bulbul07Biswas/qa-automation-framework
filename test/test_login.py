#test file mai hum test logic likhte hai

from pages.login_page import LoginPage
from pages.home_page import HomePage
from playwright.sync_api import expect
from utils.read_data import read_json 



def test_nevi(page):
    print("Test started")
    data= read_json("login.json")
    print("DATA:", data)
    nevi= LoginPage(page)
    
    nevi.valid_login(
        
        data["valid_login"]["email"],
        data["valid_login"]["password"]
    )

    nevi.login_successfull()
    
def test_homePage(page):
    home= HomePage(page)
    home.homepage_carousel()
    home.test_case_page()
    


    
    
    
    
    
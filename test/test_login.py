#test file mai hum test logic likhte hai

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import Products
from playwright.sync_api import expect
from utils.read_data import read_json 
from pages.base_page import BasePage



def test_login_successfull(login):
     successfull= LoginPage(login)
     successfull.login_successfull()


def test_homePage(login):
    home = HomePage(login)
    home.homepage_carousel()
    home.test_case_page()

def test_productPage(login):
    product = Products(login)
    product.category()
    
def test_invalid_login(page):
    data= read_json("login.json")
    base= BasePage(page)
    base.invalid_login(
    data["invalid_login"]["email"],
    data["invalid_login"]["password"]
                     )
   
def test_saree_product(login):
    product= Products(login)
    product.saree()
    product.checkout()
    product.payment()













# def test_nevi(page):
    # print("Test started")
    # # data= read_json("login.json")
    # nevi= LoginPage(page)
    
    # nevi.valid_login(
        
    #     # data["valid_login"]["email"],
    #     # data["valid_login"]["password"]
    # )
  #____________________________________________________________________  
# def test_nevi(page):
#     data = read_json("login.json")

#     base = BasePage(page)

#     base.valid_login(
#         data["valid_login"]["email"],
#         data["valid_login"]["password"]
#     )

#     # nevi.login_successfull()
    
# def test_homePage(page):
    
#     data = read_json("login.json")

#     base = BasePage(page)

#     base.valid_login(
#         data["valid_login"]["email"],
#         data["valid_login"]["password"])
    
    
#     home= HomePage(page)
#     home.homepage_carousel()
#     home.test_case_page()
    
# def test_productPage(page):
#     product= Products(page)
#     product.category()
    
    


    
    
    
    
    
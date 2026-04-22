#Step1- Browser launch kia hai, jisme new page opnkar rahe hai, yaha browser means
#chrome and context means whole window
import pytest
from playwright.sync_api import sync_playwright
#“Ye ek setup function hai jo test se pehle run hoga”
@pytest.fixture(scope='function')
#scope='function'-Har test ke liye naya browser + naya page banega
def page(): #jb bhi hm test function bnayege ye to pytest ise automaticlly cl krega.
    with sync_playwright() as p:
        #above line mai playwright is strarted and ek object p bana hai(jo brow control krega)
        browser = p.chromium.launch(headless=False,args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page= context.new_page()
        
        page.goto("https://automationexercise.com/")
        yield page
        #yield ek pause point hai,like setup is completed hai now this page will woek for test)
        context.close()
        #Browser context band.session clean ho gaya
        browser.close()
        #Test khatam → cleanup done


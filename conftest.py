
import pytest
from playwright.sync_api import sync_playwright
from pages.base_page import BasePage
from utils.read_data import read_json

@pytest.fixture(scope='function')
#scope='function'-Har test ke liye naya browser + naya page banega
def page(): #jb bhi hm test function bnayege ye to pytest ise automaticlly cl krega.
    with sync_playwright() as p:
        #above line mai playwright is strarted and ek object p bana hai(jo brow control krega)
        browser = p.chromium.launch(headless=False,args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        # Step1- Browser launch kia hai, jisme new page opnkar rahe hai, yaha browser means
        # chrome and context means whole window
        page= context.new_page()
        page.goto("https://automationexercise.com/")
        yield page
        #yield ek pause point hai,like setup is completed hai now this page will woek for test)
        context.close()
        #Browser context band.session clean ho gaya
        browser.close()




@pytest.fixture(scope="function")
def login(page):
    data = read_json("login.json")
    
    # Debug print
    print("Browser launched and URL opened")

    # Perform login
    base = BasePage(page)
    base.valid_login(
    data["valid_login"]["email"],
    data["valid_login"]["password"]
        )


    yield page 
    return page


#For screenshot capture

import pytest
import os
from datetime import datetime



SCREENSHOT_DIR = os.path.join(os.getcwd(), "reports", "screenshots")
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:
            os.makedirs("screenshots", exist_ok=True)

            file_name = f"screenshots/{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

            page.screenshot(path=file_name)

            print(f"\nScreenshot saved at: {file_name}")


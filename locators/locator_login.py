
class Locators:
    User_email= "(//input[@type='email'])[1]"
    User_password= "Password"
    Signup_login= '//a[contains(text(),"Signup")]'
    Login_button= "//button[contains(text(),'Login')]"
    logout_button= "a[href='/logout']"
    
#HomePage_Loctors

    Test_cases_button = "(//a[@class='test_cases_list'])[1]"
    Test_case_text= "//h5"
    Test_case_Register_user= "//u[text()='Test Case 1: Register User']"
    Test_Register_user_cases= "(//li[@class='list-group-item'])[1]"
    Test_Subscription_email= "#susbscribe_email"
    Test_Subscription_submit= "//i[@class='fa fa-arrow-circle-o-right']"
    Test_toast_sucess_msg= "[class='alert-success alert']"
    # Test_case_Register_user= "//u[text()='Test Case 1: Register User']"
    
    
    #Product_Locator
    product= "//li//i[@class='material-icons card_travel']"
    product_search= "#search_product"
    search_button= "#submit_search"
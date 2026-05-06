
class Locators:
    User_email= "(//input[@type='email'])[1]"
    User_password= "Password"
    Signup_login= '//a[contains(text(),"Signup")]'
    Login_button= "//button[contains(text(),'Login')]"
    logout_button= "a[href='/logout']"
    
    #incorrect_login_attempt
    invalid_login_msg= "Your email or password is incorrect!"
    
#HomePage_Loctors

    home_popup =".continue-prompt-text"
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
    women_catagory= "(//i[@class='fa fa-plus'])[1]"
    
    
    #saree
    saree_link= "Saree "
    saree_homepage= "Women - Saree Products"
    saree_cotton_silk= "Cotton Silk Hand Block Print Saree"
    add_to_cart='Add to cart'
    added_popup= 'Added!'
    view_cart_text='View Cart'
    
    #checkout
    checkout_proceed= 'Proceed To Checkout'
    add_comment= '.form-control'
    place_order= 'Place Order'
    
    
    #payment
    card_name= "//input[@class='form-control']"
    card_number='//input[@class="form-control card-number"]'
    cvc= '//input[@class="form-control card-cvc"]'
    expire_date='//input[@class="form-control card-expiry-month"]' 
    expire_year='//input[@class="form-control card-expiry-year"]'
    confirm_order='//button[@class="form-control btn btn-primary submit-button"]'
    success_notification= ".alert-success"
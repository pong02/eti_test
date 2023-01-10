import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import page

# class EtisalatTestHomeSearch(unittest.TestCase):
#     # this tests search functions from home
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         self.driver.set_window_position(*screenOffset)
#         self.driver.get("https://otewww2.nic.ae/") 
#         # at the time of writing, the SSL/Certificate ERROR is not fixed yet, just ignore it

#     # test cases, must start with test_ and be between setup and teardown
#     def test_title(self):
#         mainPage = page.MainPage(self.driver)
#         assert mainPage.is_title_matches()

#     def test_search_available_domain(self):
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         assert search_result_page.is_result_valid()

#     def test_search_owned_domain(self):
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "google.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         assert search_result_page.is_result_invalid()

#     # def test_search_reserved_domain(self):
#     #     mainPage = page.MainPage(self.driver)
#     #     mainPage.search_text_element = "aeda.abudhabi"
#     #     mainPage.click_search_button()
#     #     search_result_page = page.SearchResultPage(self.driver)
#     #     assert search_result_page.is_result_reserved()
#     #   DOMAIN IS NOW NOT AVAILABLE, not reserved anymore 
#     # (the rules of domain reservation shows that it is NOT a constant)

#     def test_search_premium_domain(self):
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "nike.vip"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         assert search_result_page.is_result_reserved()

#     def test_search_domain_extless(self):
#         #this is kept as a >=1 check as they might want to offer more ext in the future
#         mainPage = page.MainPage(self.driver)
#         #60 char is the max
#         mainPage.search_text_element = "thisisatestdomainnameforetisalatdomainsstagingstorefront1234"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         assert search_result_page.is_results_fetched()

#     def tearDown(self):
#         self.driver.close()
    
# class EtisalatTestSearchDropdowns(unittest.TestCase):
#     #we tested the rows, now we test the drop downs
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         self.driver.set_window_position(*screenOffset)
#         self.driver.get("https://otewww2.nic.ae/") 

#     def test_available_dropdown(self):
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         assert search_result_page.is_dropdown_valid()
#         assert search_result_page.is_dropdown_interactable()
#         assert search_result_page.is_dropdown_set()

#     def test_interaction(self):
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         assert search_result_page.is_dropdown_set()

#     def test_unavailable_dropdown(self):
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "google.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         assert not search_result_page.is_dropdown_valid()

#     def test_multi_dropdowns(self):
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         #this just tests if more than 1 dropdown summoned
#         assert search_result_page.is_multiple_dropdown_valid()
#         assert search_result_page.is_multiple_dropdown_set()

#     def tearDown(self):
#         self.driver.close()
    
# class EtisalatTestSearchAddButtons(unittest.TestCase):
#     #we tested the dropdowns, now we test the buttons (unclicked,clicked)
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         self.driver.set_window_position(*screenOffset)
#         self.driver.get("https://otewww2.nic.ae/") 

#     def test_button_available(self):
#         # assuming an available domain, the button must be
#         # clickable -> changes outlook onClick (cancel button summoned)
#         # reversible -> cancel button click will revert it back to default state
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         # test if button clickable
#         assert search_result_page.is_add_clickable()
#         # test if button state has changed on click
#         assert search_result_page.is_click_changing_btn()
#         # test if pressing again reverts
#         assert search_result_page.is_click_changing_btn(clicked=True)
        

#     def test_button_unavailable(self):
#         # assuming an unavailable domain, the button must not be clickable
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "google.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         # test if button clickable
#         assert not search_result_page.is_add_clickable()

#     def test_multi_button_available(self):
#         # assuming an available domain, the button must be
#         # clickable -> changes outlook onClick (cancel button summoned)
#         # reversible -> cancel button click will revert it back to default state
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "nike"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         # test if buttons clickable
#         # assert search_result_page.is_multi_add_clickable()
#         # test if button states changed on click
#         assert search_result_page.is_multi_click_changing_btn()
#         # test if pressing again reverts
#         assert search_result_page.is_multi_click_changing_btn(clicked=True)

#     def tearDown(self):
#         self.driver.close()
    
# class EtisalatTestSearchSummary(unittest.TestCase):
#     #we tested every element in the page, now we put all tgt and check the summary
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         self.driver.set_window_position(*screenOffset)
#         self.driver.get("https://otewww2.nic.ae/") 

#     def test_add_single_item_out_of_one(self):
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)

#         assert search_result_page.is_one_added_to_summary()

#     def test_add_single_item_out_of_many(self):
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)

#         assert search_result_page.is_one_added_to_summary()

#     def test_add_single_item_out_of_one_add_all(self):
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)

#         assert search_result_page.is_one_added_to_summary(addAll=True)

#     def test_add_multiple_item(self):
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
        
#         assert search_result_page.is_all_added()

#     def test_add_all_item(self):
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
        
#         assert search_result_page.is_all_added(addAll = True)

#     # ==========================INVALID==========================
#     def test_add_zero_item_out_of_one(self):
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "google.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)

#         assert search_result_page.is_nothing_added()

#     # disabling cause google.ae is now released to public, no longer reserved
#     # def test_add_zero_item_out_of_many(self):
#     #     mainPage = page.MainPage(self.driver)
#     #     mainPage.search_text_element = "google"
#     #     mainPage.click_search_button()
#     #     search_result_page = page.SearchResultPage(self.driver)

#     #     assert search_result_page.is_nothing_added()

#     def test_add_zero_item_out_of_one_add_all(self):
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "google.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)

#         assert search_result_page.is_nothing_added(addAll=True)

#     # disabling cause google.ae is now released to public, no longer reserved
#     # def test_add_multiple_item_invalid(self):
#     #     mainPage = page.MainPage(self.driver)
#     #     mainPage.search_text_element = "google"
#     #     mainPage.click_search_button()
#     #     search_result_page = page.SearchResultPage(self.driver)
        
#     #     assert search_result_page.is_nothing_added()

#     # google.ae is now released to the public, rendering this case unusable.
#     # def test_add_all_item_invalid(self):
#     #     mainPage = page.MainPage(self.driver)
#     #     mainPage.search_text_element = "google"
#     #     mainPage.click_search_button()
#     #     search_result_page = page.SearchResultPage(self.driver)
        
#     #     assert search_result_page.is_nothing_added(addAll = True)

#     def tearDown(self):
#         self.driver.close()
    
# class EtisalatTestSearchContinue(unittest.TestCase):
#     #now we test payment (continue)
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         self.driver.set_window_position(*screenOffset)
#         self.driver.get("https://otewww2.nic.ae/") 

#     def test_zero_item_continue_valid(self):
#         # should return error popup
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         # continue without checking anything
#         search_result_page.click_continue()

#         assert search_result_page.is_add_prompt()

#     def test_zero_item_continue_invalid(self):
#         # should return error popup
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "google.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         # continue with clicking add all when nothign is valid
#         search_result_page.click_add_all()
#         search_result_page.click_continue()

#         assert search_result_page.is_add_prompt()

#     def test_single_item_continue(self):
#         # should ask for login
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         search_result_page.click_add_all()
#         search_result_page.click_continue()

#         assert not search_result_page.is_add_prompt()

#         login_page = page.LoginPageContinue(self.driver)
#         assert login_page.is_login_prompt()

#     def test_multiple_item_continue(self):
#         # should ask for login
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         search_result_page.click_add_all()
#         search_result_page.click_continue()

#         assert not search_result_page.is_add_prompt()

#         login_page = page.LoginPageContinue(self.driver)
#         assert login_page.is_login_prompt()

#     def tearDown(self):
#         self.driver.close()

# class EtisalatTestContinueLogin(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         self.driver.set_window_position(*screenOffset)
#         self.driver.get("https://otewww2.nic.ae/") 
#         # we have to reach continue button first
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         search_result_page.click_add_all()
#         search_result_page.click_continue()
#         # we will now see the login page

#     def test_login_no_name(self):
#         login_page = page.LoginPageContinue(self.driver)
#         login_page.password_text_element = "P@ssw0rd"
#         login_page.captcha_text_element = "12345"
#         # fill in everything but name shoudl show:
#         # The login details entered are incorrect, please enter the correct login details.
#         assert login_page.is_login_invalid()

#     def test_login_no_pw(self):
#         login_page = page.LoginPageContinue(self.driver)
#         # login_page.username_text_element = "ckusage"
#         login_page.enter_name("ckusage")
#         login_page.captcha_text_element = "12345"
#         # fill in everything but pw shoudl show:
#         # The login details entered are incorrect, please enter the correct login details.
#         assert login_page.is_login_invalid()

#     def test_login_no_captcha(self):
#         login_page = page.LoginPageContinue(self.driver)
#         login_page.enter_name("ckusage")
#         login_page.password_text_element = "P@ssw0rd"
#         # fill in everything but captcha, should return 
#         # The captcha details entered are incorrect, please enter the correct captcha details.
#         assert login_page.is_captcha_invalid()

#     def test_login_filled(self):
#         login_page = page.LoginPageContinue(self.driver)
#         login_page.enter_name("ckusage")
#         login_page.password_text_element = "P@ssw0rd"
#         login_page.captcha_text_element = "12345"
#         # fill in everything (captcha SHOULD fail BECAUSE we cant bypass)
#         # due to the captcha this is the extent we can test
#         assert login_page.is_captcha_invalid()

#     def tearDown(self):
#         self.driver.close()

# class EtisalatTestAccountLogin(unittest.TestCase):
#     # This is login from home
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         self.driver.set_window_position(*screenOffset)
#         self.driver.get("https://otewww2.nic.ae/")
#         # click account login
#         mainPage = page.MainPage(self.driver)
#         mainPage.click_login_button()
        

#     def test_login_no_name(self):
#         login_page = page.LoginPage(self.driver)
#         login_page.password_text_element = "P@ssw0rd"
#         login_page.captcha_text_element = "12345"
#         # fill in everything but name shoudl show:
#         # The login details entered are incorrect, please enter the correct login details.
#         assert login_page.is_login_invalid()

#     def test_login_no_pw(self):
#         login_page = page.LoginPage(self.driver)
#         # login_page.username_text_element = "ckusage"
#         login_page.username_text_element = "ckusage"
#         login_page.captcha_text_element = "12345"
#         # fill in everything but pw shoudl show:
#         # The login details entered are incorrect, please enter the correct login details.
#         assert login_page.is_login_invalid()

#     def test_login_no_captcha(self):
#         login_page = page.LoginPage(self.driver)
#         login_page.username_text_element = "ckusage"
#         login_page.password_text_element = "P@ssw0rd"
#         # fill in everything but captcha, should return 
#         # The captcha details entered are incorrect, please enter the correct captcha details.
#         assert login_page.is_captcha_invalid()

#     def test_login_filled(self):
#         login_page = page.LoginPage(self.driver)
#         login_page.username_text_element = "ckusage"
#         login_page.password_text_element = "P@ssw0rd"
#         login_page.captcha_text_element = "12345"
#         # fill in everything (captcha SHOULD fail BECAUSE we cant bypass)
#         # due to the captcha this is the extent we can test
#         assert login_page.is_captcha_invalid()

#     def tearDown(self):
#         self.driver.close()

# class EtisalatTestAccountCreation(unittest.TestCase):
#     # here, we will only test the FORM FIELD VALIDATION CAPTCHA CANNOT BE OVERCOME
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         self.driver.set_window_position(*screenOffset)
#         self.driver.get("https://otewww2.nic.ae/") 
#         # for this page, we can only reach from CONTINUE so we reach contnue first
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123.com"
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         search_result_page.click_add_all()
#         search_result_page.click_continue()
#         #we will now see the create button, click it
#         login_page = page.LoginPageContinue(self.driver)
#         login_page.click_create()

#     def test_empty_fields(self):
#         # submit without checking should show error dialogue
#         create_page = page.CreatePage(self.driver)
#         create_page.click_submit()
#         # check and submit should be invalid (all errors - cant be empty)
#         assert create_page.is_checkbox_dialogue()
#         create_page.checkCheckBox()
#         create_page.click_submit()
#         assert not create_page.is_form_valid()
        

#     def test_completed_fields_valid(self):
#         create_page = page.CreatePage(self.driver)
#         create_page.company_org = "qinetics"
#         create_page.contactPIC = "Pong" 
#         create_page.addr1 = "L4E2 Enterprise 4,"  
#         create_page.addr2 = "Technology Park Malaysia,"
#         create_page.city = "Bukit Jalil," 
#         create_page.state = "Kuala Lumpur,"  
#         create_page.zipPO = "57000" 
#         create_page.countrySelect() #random country 
#         create_page.phonePre = "123" 
#         create_page.phonePost = "12345678" 
#         create_page.mobilePre = "123" 
#         create_page.mobilePost = "12345678" 
#         create_page.faxPre = "123" 
#         create_page.faxPost = "12345678" 
#         create_page.email = "zhongzhe.pong@qinetics.net" 
#         create_page.tax = "81273612378" 
#         create_page.userID = create_page.randomUserName() #random name (its actually created)
#         create_page.password = "P@ssw0rd" 
#         create_page.confirmPassword = "P@ssw0rd" 
#         # submit without checking should show error dialogue
#         create_page.click_submit()
#         assert create_page.is_checkbox_dialogue()
#         create_page.checkCheckBox()
#         create_page.click_submit()
#         assert create_page.is_form_valid()

#     def test_neccesary_fields_valid(self):
#         create_page = page.CreatePage(self.driver)
#         create_page.contactPIC = "Pong" 
#         create_page.addr1 = "L4E2 Enterprise 4, Technology Park Malaysia,"
#         create_page.city = "Bukit Jalil,"  
#         create_page.zipPO = "57000" 
#         create_page.phonePre = "123" 
#         create_page.phonePost = "12345678" 
#         create_page.email = "zhongzhe.pong@qinetics.net" 
#         create_page.userID = create_page.randomUserName() #random name (its actually created)
#         create_page.password = "P@ssw0rd" 
#         create_page.confirmPassword = "P@ssw0rd" 
#         # submit without checking should show error dialogue
#         create_page.click_submit()
#         assert create_page.is_checkbox_dialogue()
#         create_page.checkCheckBox()
#         create_page.click_submit()
#         assert create_page.is_form_valid()

#     def test_completed_fields_invalid(self):
#         create_page = page.CreatePage(self.driver)
#         create_page.company_org = "testing123"
#         create_page.contactPIC = "testing123" 
#         create_page.addr1 = "testing123"  
#         create_page.addr2 = "testing123"
#         create_page.city = "testing123" 
#         create_page.state = "testing123"  
#         create_page.zipPO = "testing123" 
#         create_page.countrySelect() #random country 
#         create_page.phonePre = "testing123" 
#         create_page.phonePost = "testing123" 
#         create_page.mobilePre = "testing123" 
#         create_page.mobilePost = "testing123" 
#         create_page.faxPre = "testing123" 
#         create_page.faxPost = "testing123" 
#         create_page.email = "testing123" 
#         create_page.tax = "testing123" 
#         create_page.userID = "testing123" 
#         create_page.password = "testing123" 
#         create_page.confirmPassword = "testing123" 
#         # submit without checking should show error dialogue
#         create_page.click_submit()
#         assert create_page.is_checkbox_dialogue()
#         create_page.checkCheckBox()
#         create_page.click_submit()
#         assert not create_page.is_form_valid()

#     def tearDown(self):
#         self.driver.close()

# '''
# not having captcha means there is no longer an issue in testing further items
# I dont feel comfortable copy pasting these, as it might be too much to change, 
# opening up possible areas for error. thus, it will be single and multiple as 2 suites in total, 
# WHEN multiple, a popup may appear for .abudhabi and arabic ext
# '''
class EtisalatTestPaymentStep2Single(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.set_window_position(*screenOffset)
        self.driver.get("https://otewww2.nic.ae/") 
        # for this page, we can only reach from CONTINUE so we reach contnue first
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.com" 
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        search_result_page.click_add_all()
        search_result_page.click_continue()
        #if search in multimode, we will get a pop up on continue
        search_result_page.close_pop_up()
        #we will now see the create button, click it
        login_page = page.LoginPageContinue(self.driver)
        login_page.click_create()
        create_page = page.CreatePage(self.driver)
        # despite the field (org name) being named as NOT COMPULSORY, it must be filled to 
        # avoid error when applying for a domain
        create_page.company_org = "qinetics_testing"
        create_page.contactPIC = "Pong" 
        create_page.addr1 = "L4E2 Enterprise 4, Technology Park Malaysia,"
        create_page.city = "Bukit Jalil,"  
        create_page.zipPO = "57000" 
        create_page.phonePre = "123" 
        create_page.phonePost = "12345678" 
        create_page.email = "zhongzhe.pong@qinetics.net" 
        create_page.userID = create_page.randomUserName() #random name (its actually created)
        create_page.password = "P@ssw0rd" 
        create_page.confirmPassword = "P@ssw0rd" 
        create_page.checkCheckBox()
        create_page.click_submit()
        # this is the only way to reach this page
        # when the creation succeeded, we will be on step 2. in step2 we will test for summary 
        # and ability to move forward to the next page without errors

#     def test_results_step_2_only_whois(self):
#         # we want to test adding value added services here, note that only WHOIS is the default action
#         step_2_page = page.Step2Page(self.driver)
#         # should have value added services WITH ONLY 1 item (WHOIS)
#         assert step_2_page.is_summary_valid()
#         # remove whois
#         step_2_page.add_whois()
#         assert step_2_page.is_reverse_summary_valid()
#         # add whois
#         step_2_page.add_whois()
#         # go to step3 should be successful regardless of choices
#         step_2_page.click_continue()
#         # now check for elements in step3 present?
#         step_3_page = page.Step3Page(self.driver)
#         assert step_3_page.checkout_clickable()

#     def test_results_step_2_only_dnssec(self):
#         # we want to test adding value added services here
#         step_2_page = page.Step2Page(self.driver)
#         # should have value added services WITH ONLY 1 item (DNSSEC)
#         # remove whois and add dnssec
#         step_2_page.add_whois()
#         step_2_page.add_dnssec()   
#         assert step_2_page.is_summary_valid(mode=2)
#         # remove dnssec
#         step_2_page.add_dnssec()   
#         assert step_2_page.is_reverse_summary_valid()
#         # add dnssec 
#         step_2_page.add_dnssec()  
#         # go to step3 should be successful regardless of choices
#         step_2_page.click_continue()
#         # now check for elements in step3 present?
#         step_3_page = page.Step3Page(self.driver)
#         assert step_3_page.checkout_clickable()

#     def test_results_step_2_nothing(self):
#         # we want to test adding value added services here
#         step_2_page = page.Step2Page(self.driver)
#         # since whois is free and added by default, we have to click
#         # remove whois
#         step_2_page.add_whois()
#         assert step_2_page.is_summary_valid(mode=0)
#         # no need to test for reverse here since nothing is being added
#         # go to step3 should be successful regardless of choices
#         step_2_page.click_continue()
#         # now check for elements in step3 present?
#         step_3_page = page.Step3Page(self.driver)
#         assert step_3_page.checkout_clickable()

#     def test_results_step_2_all(self):
#         # we want to test adding value added services here
#         step_2_page = page.Step2Page(self.driver)
#         # should have value added services with 2 items
#         # add dnssec 
#         step_2_page.add_dnssec()
#         assert step_2_page.is_summary_valid(mode=3)
#         # remove both
#         step_2_page.add_whois()   
#         step_2_page.add_dnssec()  
#         assert step_2_page.is_reverse_summary_valid()
#         # add both back
#         step_2_page.add_whois()   
#         step_2_page.add_dnssec()  
#         # go to step3 should be successful regardless of choices
#         step_2_page.click_continue()
#         # now check for elements in step3 present?
#         step_3_page = page.Step3Page(self.driver)
#         assert step_3_page.checkout_clickable()

#     def tearDown(self):
#         self.driver.close()

# class EtisalatTestPaymentStep2Multi(unittest.TestCase):
#     # this is overriding the setup for single, to limit the area of change
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         self.driver.set_window_position(*screenOffset)
#         self.driver.get("https://otewww2.nic.ae/") 
#         # for this page, we can only reach from CONTINUE so we reach contnue first
#         mainPage = page.MainPage(self.driver)
#         mainPage.search_text_element = "etisalattesting123" 
#         mainPage.click_search_button()
#         search_result_page = page.SearchResultPage(self.driver)
#         search_result_page.click_add_all()
#         search_result_page.click_continue()
#         #if search in multimode, we will get a pop up on continue
#         search_result_page.close_pop_up()
#         #we will now see the create button, click it
#         login_page = page.LoginPageContinue(self.driver)
#         login_page.click_create()
#         create_page = page.CreatePage(self.driver)
#         # despite the field (org name) being named as NOT COMPULSORY, it must be filled to 
#         # avoid error when applying for a domain
#         create_page.company_org = "qinetics_testing"
#         create_page.contactPIC = "Pong" 
#         create_page.addr1 = "L4E2 Enterprise 4, Technology Park Malaysia,"
#         create_page.city = "Bukit Jalil,"  
#         create_page.zipPO = "57000" 
#         create_page.phonePre = "123" 
#         create_page.phonePost = "12345678" 
#         create_page.email = "zhongzhe.pong@qinetics.net" 
#         create_page.userID = create_page.randomUserName() #random name (its actually created)
#         create_page.password = "P@ssw0rd" 
#         create_page.confirmPassword = "P@ssw0rd" 
#         create_page.checkCheckBox()
#         create_page.click_submit()

#     def test_results_step_2_only_whois(self):
#         EtisalatTestPaymentStep2Single.test_results_step_2_only_whois(self)

#     def test_results_step_2_only_dnssec(self):
#         EtisalatTestPaymentStep2Single.test_results_step_2_only_dnssec(self)

#     def test_results_step_2_nothing(self):
#         EtisalatTestPaymentStep2Single.test_results_step_2_nothing(self)

#     def test_results_step_2_all(self):
#         EtisalatTestPaymentStep2Single.test_results_step_2_all(self)

#     def tearDown(self):
#         self.driver.close()
import time
class EtisalatTestPaymentStep3Single(unittest.TestCase):
    def setUp(self):
        # reuse setup for step2 and add on
        EtisalatTestPaymentStep2Single.setUp(self)
        # this leaves it at step 2 (adding VAS)
        step_2_page = page.Step2Page(self.driver)
        step_2_page.click_continue()
        # this leaves us at step 3 interface

    '''
    we want to test:
    - check all and if it affects the amt
    - check 1
    - check all 1 by 1 * N/A for single
    - check modify
    - check drop down
    - check checkout reidr
    - check back
    '''
    # def test_results_step_3_year_changed(self):
    #     # year change should be possible and should NOT affect check out
    #     step_3_page = page.Step3Page(self.driver)
    #     # this will be zero because there is only 1 in the first place
    #     for _ in range(10):
    #         #keep changing, shouldnt be a problem
    #         step_3_page.set_dropdown(0)
    #     assert not step_3_page.is_checkbox_error()
    #     step_3_page.click_checkout()
    #     step_4_page = page.Step4Page(self.driver)
    #     assert step_4_page.proceed_complete()
        
    # def test_results_step_3_unchecked_all(self):
    #     # when we uncheck via checkall, we should get an error pop up
    #     step_3_page = page.Step3Page(self.driver)
    #     step_3_page.checkAllCheckBox()
    #     # this will be zero because there is only 1 in the first place
    #     step_3_page.click_checkout()
    #     assert step_3_page.is_checkbox_error()
        
    # def test_results_step_3_unchecked_single(self):
    #     # when we uncheck vie itself, we should get an error pop up
    #     step_3_page = page.Step3Page(self.driver)
    #     step_3_page.checkCheckBox(1)
    #     # this will be zero because there is only 1 in the first place
    #     step_3_page.click_checkout()
    #     assert step_3_page.is_checkbox_error()
        
    # def test_results_step_3_unchecked_single_WHOIS(self):
    #     # when we uncheck just the whois protection, it should not have error
    #     step_3_page = page.Step3Page(self.driver)
    #     step_3_page.checkCheckBox(2)
    #     # this will be zero because there is only 1 in the first place
    #     step_3_page.click_checkout()
    #     assert not step_3_page.is_checkbox_error()

    def test_results_step_3_modify_registrant(self):
        # modify buttons should only exist on DOMAIN rows
        # modification should not affect ability to go next
        step_3_page = page.Step3Page(self.driver)
        step_3_page.click_modify(0)
        form = page.ModifyPage(self.driver)
        form.fillRegistrant()
        form.checkTnC()

        # post modification should still see the same items in page (just compare page source? xd)
        
    def tearDown(self):
        self.driver.close()

# class EtisalatTestPaymentStep4Single(unittest.TestCase):
#     def setUp(self):
#         # reuse setup for step2 and add on
#         EtisalatTestPaymentStep2Single.setUp(self)
#         # this leaves it at step 2 (adding VAS)
#         step_2_page = page.Step2Page(self.driver)
#         step_2_page.click_continue()
#         # this leaves us at step 3 interface
#     def test_results_step_4(self):
#         # we want to test adding value added services here
#         step_3_page = page.Step3Page(self.driver)
#         step_3_page.click_checkout()
#         step_4_page = page.Step4Page(self.driver)
#         step_4_page.checkCheckbox()
#         step_4_page.click_proceed()
#         #here we will see the payment gateway
#         payment_page = page.PaymentGatewayPage(self.driver)
#         payment_page.wait_gateway_load()
#         payment_page.card_num_field = "4111111111111111"
#         payment_page.cvv_field = "123"
#         payment_page.click_pay()
#         # here we should see the customer survey pop up stacked on 
#         # top of the transaction details
#         # from here we can go to dash board and etc        
#         return True

#     def tearDown(self):
#         self.driver.close()
    

if __name__ == "__main__":
    global screenOffset
    # right : screenOffset= +X
    # left : screenOffset= -X
    # if screen not present, it will jut put in the middle
    screenOffset = (-1500,-100)
    unittest.main(warnings='ignore')
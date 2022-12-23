import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import page


class EtisalatTestHomeSearch(unittest.TestCase):
    # this tests search functions from home
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.set_window_position(*screenOffset)
        self.driver.get("https://otewww2.nic.ae/") 
        # at the time of writing, the SSL/Certificate ERROR is not fixed yet, just ignore it

    # test cases, must start with test_ and be between setup and teardown
    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

    def test_search_available_domain(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_valid()

    def test_search_owned_domain(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "google.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_invalid()

    # def test_search_reserved_domain(self):
    #     mainPage = page.MainPage(self.driver)
    #     mainPage.search_text_element = "aeda.abudhabi"
    #     mainPage.click_search_button()
    #     search_result_page = page.SearchResultPage(self.driver)
    #     assert search_result_page.is_result_reserved()
    #   DOMAIN IS NOW NOT AVAILABLE, not reserved anymore 
    # (the rules of domain reservation shows that it is NOT a constant)

    def test_search_premium_domain(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "nike.vip"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_reserved()

    def test_search_domain_extless(self):
        #this is kept as a >=1 check as they might want to offer more ext in the future
        mainPage = page.MainPage(self.driver)
        #60 char is the max
        mainPage.search_text_element = "thisisatestdomainnameforetisalatdomainsstagingstorefront1234"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_fetched()

    def tearDown(self):
        self.driver.close()
    
class EtisalatTestSearchDropdowns(unittest.TestCase):
    #we tested the rows, now we test the drop downs
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.set_window_position(*screenOffset)
        self.driver.get("https://otewww2.nic.ae/") 

    def test_available_dropdown(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_dropdown_valid()
        assert search_result_page.is_dropdown_interactable()
        assert search_result_page.is_dropdown_set()

    def test_interaction(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_dropdown_set()

    def test_unavailable_dropdown(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "google.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert not search_result_page.is_dropdown_valid()

    def test_multi_dropdowns(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        #this just tests if more than 1 dropdown summoned
        assert search_result_page.is_multiple_dropdown_valid()
        assert search_result_page.is_multiple_dropdown_set()

    def tearDown(self):
        self.driver.close()
    
class EtisalatTestSearchAddButtons(unittest.TestCase):
    #we tested the dropdowns, now we test the buttons (unclicked,clicked)
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.set_window_position(*screenOffset)
        self.driver.get("https://otewww2.nic.ae/") 

    def test_button_available(self):
        # assuming an available domain, the button must be
        # clickable -> changes outlook onClick (cancel button summoned)
        # reversible -> cancel button click will revert it back to default state
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        # test if button clickable
        assert search_result_page.is_add_clickable()
        # test if button state has changed on click
        assert search_result_page.is_click_changing_btn()
        # test if pressing again reverts
        assert search_result_page.is_click_changing_btn(clicked=True)
        

    def test_button_unavailable(self):
        # assuming an unavailable domain, the button must not be clickable
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "google.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        # test if button clickable
        assert not search_result_page.is_add_clickable()

    def test_multi_button_available(self):
        # assuming an available domain, the button must be
        # clickable -> changes outlook onClick (cancel button summoned)
        # reversible -> cancel button click will revert it back to default state
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "nike"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        # test if buttons clickable
        # assert search_result_page.is_multi_add_clickable()
        # test if button states changed on click
        assert search_result_page.is_multi_click_changing_btn()
        # test if pressing again reverts
        assert search_result_page.is_multi_click_changing_btn(clicked=True)

    def tearDown(self):
        self.driver.close()
    
class EtisalatTestSearchSummary(unittest.TestCase):
    #we tested every element in the page, now we put all tgt and check the summary
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.set_window_position(*screenOffset)
        self.driver.get("https://otewww2.nic.ae/") 

    def test_add_single_item_out_of_one(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)

        assert search_result_page.is_one_added_to_summary()

    def test_add_single_item_out_of_many(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)

        assert search_result_page.is_one_added_to_summary()

    def test_add_single_item_out_of_one_add_all(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)

        assert search_result_page.is_one_added_to_summary(addAll=True)

    def test_add_multiple_item(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        
        assert search_result_page.is_all_added()

    def test_add_all_item(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        
        assert search_result_page.is_all_added(addAll = True)

    # ==========================INVALID==========================
    def test_add_zero_item_out_of_one(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "google.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)

        assert search_result_page.is_nothing_added()

    def test_add_zero_item_out_of_many(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "google"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)

        assert search_result_page.is_nothing_added()

    def test_add_zero_item_out_of_one_add_all(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "google.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)

        assert search_result_page.is_nothing_added(addAll=True)

    def test_add_multiple_item_invalid(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "google"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        
        assert search_result_page.is_nothing_added()

    def test_add_all_item_invalid(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "google"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        
        assert search_result_page.is_nothing_added(addAll = True)

    def tearDown(self):
        self.driver.close()
    
class EtisalatTestSearchContinue(unittest.TestCase):
    #now we test payment (continue)
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.set_window_position(*screenOffset)
        self.driver.get("https://otewww2.nic.ae/") 

    def test_zero_item_continue_valid(self):
        # should return error popup
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        # continue without checking anything
        search_result_page.click_continue()

        assert search_result_page.is_add_prompt()

    def test_zero_item_continue_invalid(self):
        # should return error popup
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "google.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        # continue with clicking add all when nothign is valid
        search_result_page.click_add_all()
        search_result_page.click_continue()

        assert search_result_page.is_add_prompt()

    def test_single_item_continue(self):
        # should ask for login
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        search_result_page.click_add_all()
        search_result_page.click_continue()

        assert not search_result_page.is_add_prompt()

        login_page = page.LoginPage(self.driver)
        assert login_page.is_login_prompt()

    def test_multiple_item_continue(self):
        # should ask for login
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        search_result_page.click_add_all()
        search_result_page.click_continue()

        assert not search_result_page.is_add_prompt()

        login_page = page.LoginPage(self.driver)
        assert login_page.is_login_prompt()

    def test_login_no_name(self):
        # should ask for login
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        search_result_page.click_add_all()
        search_result_page.click_continue()
        login_page = page.LoginPage(self.driver)
        login_page.password_text_element = "P@ssw0rd"
        login_page.captcha_text_element = "12345"
        # fill in everything but name shoudl show:
        # The login details entered are incorrect, please enter the correct login details.
        assert login_page.is_login_invalid()

    def test_login_no_pw(self):
        # should ask for login
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        search_result_page.click_add_all()
        search_result_page.click_continue()
        login_page = page.LoginPage(self.driver)
        # login_page.username_text_element = "ckusage"
        login_page.enter_name("ckusage")
        login_page.captcha_text_element = "12345"
        # fill in everything but pw shoudl show:
        # The login details entered are incorrect, please enter the correct login details.
        assert login_page.is_login_invalid()

    def test_login_no_captcha(self):
        # should ask for login
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        search_result_page.click_add_all()
        search_result_page.click_continue()
        login_page = page.LoginPage(self.driver)
        login_page.enter_name("ckusage")
        login_page.password_text_element = "P@ssw0rd"
        # fill in everything but captcha, should return 
        # The captcha details entered are incorrect, please enter the correct captcha details.
        assert login_page.is_captcha_invalid()

    def test_login_filled(self):
        # should ask for login
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        search_result_page.click_add_all()
        search_result_page.click_continue()
        login_page = page.LoginPage(self.driver)
        login_page.enter_name("ckusage")
        login_page.password_text_element = "P@ssw0rd"
        login_page.captcha_text_element = "12345"
        # fill in everything (captcha SHOULD fail BECAUSE we cant bypass)
        # due to the captcha this is the extent we can test
        assert login_page.is_captcha_invalid()

    def tearDown(self):
        self.driver.close()


# class EtisalatTestAccountCreation(unittest.TestCase):
# # here, we will only test the FIELD VERIFICATION AS IT IS DISABLED
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # self.driver.set_window_position(*screenOffset)
#         self.driver.get("https://otewww2.nic.ae/") 

#     def tearDown(self):
#         self.driver.close()

# class EtisalatTestAccountLogin(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # self.driver.set_window_position(*screenOffset)
#         self.driver.get("https://otewww2.nic.ae/") 

#     def tearDown(self):
#         self.driver.close()

# class EtisalatTestDomainRenewal(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # self.driver.set_window_position(*screenOffset)
#         self.driver.get("https://otewww2.nic.ae/") 

#     def tearDown(self):
#         self.driver.close()

if __name__ == "__main__":
    global screenOffset
    # right : screenOffset= +X
    # left : screenOffset= -X
    # if screen not present, it will jut put in the middle
    screenOffset = (-1500,-100)
    unittest.main(warnings='ignore')
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import page


class EtisalatTestHomeSearch(unittest.TestCase):
    # this tests search functions from home
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://otewww2.nic.ae/") 
        # at the time of writing, the SSL/Certificate ERROR is not fixed yet, just ignore it

    # test cases, must start with test_ and be between setup and teardown
    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

    def test_search_available_domain(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.ae"
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
        self.driver.get("https://otewww2.nic.ae/") 

    def test_available_dropdown(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.ae"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_dropdown_valid()
        assert search_result_page.is_dropdown_interactable()
        assert search_result_page.is_dropdown_set()

    def test_interaction(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.ae"
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
        self.driver.get("https://otewww2.nic.ae/") 

    def test_add_single_item_out_of_one(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123.com"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)

        assert search_result_page.is_summary_added(0)
        assert search_result_page.is_summary_added(0,revert=True)   

    def test_add_single_item_out_of_many(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)

        assert search_result_page.is_summary_added(0)
        assert search_result_page.is_summary_added(0,revert=True)   

    def test_add_multiple_item(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        
        assert search_result_page.is_summary_added(1)
        assert search_result_page.is_summary_added(1,revert=True)  

    def test_add_all_item(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "etisalattesting123"
        mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        
        assert search_result_page.is_summary_added(2)
        assert search_result_page.is_summary_added(2,revert=True)  

    def tearDown(self):
        self.driver.close()
    
# class EtisalatTestSearchContinue(unittest.TestCase):
#     #now we test payment (continue)
#     def setUp(self):
    #     self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #     self.driver.get("https://otewww2.nic.ae/") 

    # def test_zero_item_continue(self):
    #     mainPage = page.MainPage(self.driver)
    #     mainPage.search_text_element = "google.com"
    #     mainPage.click_search_button()
    #     search_result_page = page.SearchResultPage(self.driver)

    # def test_single_item_continue(self):
    #     mainPage = page.MainPage(self.driver)
    #     mainPage.search_text_element = "etisalattesting123.com"
    #     mainPage.click_search_button()
    #     search_result_page = page.SearchResultPage(self.driver)

    # def test_multiple_item_continue(self):
    #     mainPage = page.MainPage(self.driver)
    #     mainPage.search_text_element = "etisalattesting123.com"
    #     mainPage.click_search_button()
    #     search_result_page = page.SearchResultPage(self.driver)

    # def tearDown(self):
    #     self.driver.close()


# class EtisalatTestAccountCreation(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         self.driver.get("https://otewww2.nic.ae/") 

#     def tearDown(self):
#         self.driver.close()

# class EtisalatTestAccountLogin(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         self.driver.get("https://otewww2.nic.ae/") 

#     def tearDown(self):
#         self.driver.close()

# class EtisalatTestDomainRenewal(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         self.driver.get("https://otewww2.nic.ae/") 

#     def tearDown(self):
#         self.driver.close()

if __name__ == "__main__":
    unittest.main(warnings='ignore')
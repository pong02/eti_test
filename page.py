import uuid
import random
from locator import *
from element import BasePageElement
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class SearchTextElement(BasePageElement):
    locator = "domains"

# Due to the repeat in loginVO.username, we have to enter this manually
# class UsernameLoginElement(BasePageElement):
#     locator = "loginVO.username"
# These are from continue page
class ContinuePasswordLoginElement(BasePageElement):
    locator = "loginVO.password"

class ContinueCaptchaLoginElement(BasePageElement):
    locator = "loginVO.answer"

#these are from homepage
class NameLoginElement(BasePageElement):
    locator = "username"

class PasswordLoginElement(BasePageElement):
    locator = "password"

class CaptchaLoginElement(BasePageElement):
    locator = "answer"

# +++ create acc page elements
class OrgElement(BasePageElement):
    locator = "userAccountVO.company"

class ContactPicElement(BasePageElement):
    locator = "userAccountVO.fname"
    
class AddrElement1(BasePageElement):
    locator = "userAccountVO.addr1"
      
class AddrElement2(BasePageElement):
    locator = "userAccountVO.addr2"
     
class cityElement(BasePageElement):
    locator = "userAccountVO.city"
    
class StateElement(BasePageElement):
    locator = "userAccountVO.state"
    
class zipPoElement(BasePageElement):
    locator = "userAccountVO.zip"
     
class phonePreElement(BasePageElement):
    locator = "phone1"
    
class phonePostElement(BasePageElement):
    locator = "phone2"
    
class mobilePreElement(BasePageElement):
    locator = "mobile1"
    
class mobilePostElement(BasePageElement):
    locator = "mobile2"
    
class faxPreElement(BasePageElement):
    locator = "fax1"
    
class faxPostElement(BasePageElement):
    locator = "fax2"
    
class emailElement(BasePageElement):
    locator = "userAccountVO.email"
    
class taxElement(BasePageElement):
    locator = "userAccountVO.trn"
    
class userIDElement(BasePageElement):
    locator = "userAccountVO.username"
    
class passwordElement(BasePageElement):
    locator = "userAccountVO.password"
    
class confirmPasswordElement(BasePageElement):
    locator = "confirmPassword"
    
#Payemtn gateway textfields
class cardNumElement(BasePageElement):
    locator = "creditCardNumber"

class cvvElement(BasePageElement):
    locator = "ValidationCode"

## Each class = 1 page to test, but all will inherit base page for driver
class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement() # descriptor for us to jet SET any input we want (if possible)

    def is_title_matches(self):
        return "Etisalat Domains Storefront" in self.driver.title

    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()

    def click_login_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

class SearchResultPage(BasePage):
    #============================Helper Functions================================
    def wait_load(self,noLoad=False):     
        #wait load will ensure all results have no more spinner
        resultContainer = WebDriverWait(self.driver,10).until(
        EC.presence_of_element_located(SearchResultsPageLocators.RESULT_CONTAINER)
        )
        #wait for all spinners to disappear
        # spinners = resultContainer.find_elements(By.TAG_NAME,"i")
        if (not noLoad):
            spinners = resultContainer.find_elements(*SearchResultsPageLocators.SPINNER)
            for spinner in spinners:
                WebDriverWait(self.driver, 30).until(
                EC.invisibility_of_element(spinner)
            )
        #the returned value will be the rows, fully loaded (results)
        # return resultContainer.find_elements(By.CLASS_NAME,"domainListingSearch")
        return resultContainer.find_elements(*SearchResultsPageLocators.RESULTS)

    def click_dropdown(self,domain_entry,target_index):
        #we just need to check if the text in drop changed
        #this is needed because the dropdowns are NOT select elements, but div
        #domain entry will be a SINGLE ROW in results page (result)
        drop = domain_entry.find_element(*SearchResultsPageLocators.DROPDOWN_PARENT)
        drop.click()
        dropdown = domain_entry.find_element(*SearchResultsPageLocators.DROPDOWN_BOX)
        options = dropdown.find_elements(*SearchResultsPageLocators.DROPDOWN_OPTIONS)
        options[target_index].click()

    def close_pop_up(self):
        try:
            popup = self.driver.find_element(*SearchResultsPageLocators.POP_UP)
            btn = popup.find_element(*SearchResultsPageLocators.POP_UP_ACCEPT)
            btn.click()
        except Exception as e:
            print("No pop up to close... Ignore if single mode. Otherwise, something is wrong")

    def domain_available(self,domain_entry):
        result_msg = domain_entry.find_element(*SearchResultsPageLocators.RESULT_MSG).text
        return result_msg == "This Domain is Available"

    def get_valid_domains(self,all_domain_entries):
        #this is to check if generated elements are of correct count (add button, dropdowns)
        count = 0
        for result in all_domain_entries:
            if self.domain_available(result):
                count+=1
        return count

    def get_valid_domain_names(self,all_domain_entries):
        valid_domains = []
        for result in all_domain_entries:
            if self.domain_available(result):
                name = result.find_element(*SearchResultsPageLocators.DOMAIN_NAME)
                valid_domains.append(name.text)
        return valid_domains

    def get_valid_index(self,domain_entries):
        #this is to check what index of the summary can be checked
        indices = [False]*len(domain_entries)
        for i in range(len(domain_entries)):
            if self.domain_available(domain_entries[i]):
                indices[i]=True
        return indices

    def click_add(self,result):
        #this just TRIES TO click THE DOMAIN ENTRRY IT IS PROVIDED
        # here we just want to skip if it cant be clicked
        try:
            #scrolling is actuallt NOT NEEDED as the topbar WILL NEVER block on 
            # the way down, but we keep it for completeness and safety
            btn = WebDriverWait(self.driver,1).until(
                EC.element_to_be_clickable(result.find_element(*SearchResultsPageLocators.ADD_BTN))
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(btn).perform()
            btn.click()
        except Exception as e:
            print("button not found on", result.find_element(*SearchResultsPageLocators.DOMAIN_NAME).text)
            return False
        return True

    def add_one_to_cart(self,domain_entries):
        clicked = False
        for entry in domain_entries:
            clicked = self.click_add(entry)
            if clicked:
                return
            
    def remove_one_from_cart(self,domain_entries):
        #it is literally the same thing, just for ease of reading
        self.add_one_to_cart(domain_entries)

    def add_all_to_cart(self,domain_entries):
        for entry in domain_entries:
            self.click_add(entry)
    
    def remove_all_from_cart(self,domain_entries):
        self.add_all_to_cart(domain_entries)
        
    def get_summary(self): 
        summary = self.driver.find_element(*SearchResultsPageLocators.SUMMARY)
        summDomains = summary.find_elements(*SearchResultsPageLocators.SUMMARY_DOMAINS)
        summPrice = summary.find_elements(*SearchResultsPageLocators.SUMMARY_PRICE)
        return list(zip(summDomains, summPrice))

    def total_summary(self,summaryEntries):
        # calculate some stats for further verification
        # we can increase quality of validation by ensuring 
        # more than OLD on add or less than OLD on cancel
        total = 0
        for d,p in summaryEntries:
            price = p.text.split(" ")
            if price[0] != '':
                total += float(price[1])
        return total

    def click_continue(self):
        submit = self.driver.find_element(*SearchResultsPageLocators.CONTINUE)
        submit.click()

    def click_add_all(self,noLoad = False):
        self.wait_load(noLoad)
        add_all = self.driver.find_element(*SearchResultsPageLocators.ADD_ALL)
        add_all.click()

    def summary_items_correct(self,domain_entries,newSummaryEntries,singleMode):
        # To check if the items displayed are correct and accurate, we need to check one by one
        # Every possible domain summons a BLANK '' on add click, regardless fo status
        # first get array of valid indices
            valid = self.get_valid_index(domain_entries)
            expectedCount = self.get_valid_domains(domain_entries)
            i = 0
            itemsShown = 0
            # for each domain available, check if it is BLANK. If not, since its singlemode, we break
            while i < len(domain_entries):
                if valid[i]:
                    if itemsShown == 0 and newSummaryEntries[i][0].text == '' and not singleMode:
                        #if it is valid and not SingleMODE, it should not be blank
                        print("There is an unexpected item in the summary listing at index",i,"should be valid, but is",newSummaryEntries[i][0].text)
                        return False
                    elif itemsShown == 1 and singleMode and newSummaryEntries[i][0].text != '':
                        #if it is valid but 1 item already on display, it shud be blank
                        print("There is an unexpected item in the summary listing at index",i,"should be blank, but is",newSummaryEntries[i][0].text)
                        return False
                    else:
                        #if valid and NOT BLANK AND not the first valid item
                        if singleMode:
                            itemsShown = 1
                        else:
                            itemsShown += 1
                else:
                    #make sure invalids are alwys blank
                    if newSummaryEntries[i][0].text != '':
                        print("There is an unexpected item in the summary listing at index: ",i)
                        return False
                i+=1
            if singleMode and itemsShown!=1:
                print("There is way too much items displayed!\nExpected: 1\nDisplayed:",itemsShown)
                return False
            elif itemsShown!= expectedCount and not singleMode:
                print("Displayed items do not match!\nExpected:",expectedCount,"\nDisplayed:",itemsShown)
                return False

            return True
    #=============================================================================

    def is_result_valid(self):
        results = self.wait_load()
        available = results[0].find_element(*SearchResultsPageLocators.RESULT_MSG) 
        return available.text == "This Domain is Available"

    def is_result_invalid(self):
        results = self.wait_load()
        available = results[0].find_element(*SearchResultsPageLocators.RESULT_MSG) 
        return available.text == "Not Available"

    def is_result_reserved(self):
        results = self.wait_load()
        available = results[0].find_element(*SearchResultsPageLocators.RESULT_MSG) 
        return "Domain has been reserved" in available.text or "This is a premium domain" in available.text

    def is_results_fetched(self):
        #checks if there is at least 1 entry in results only
        results = self.wait_load()
        return len(results)>=1

    def is_dropdown_valid(self):
        result = self.wait_load()[0] 
        #even tho wait load ensures the elements are loaded, 
        #we are testing INCASE it fails to load even when valid
        #we also reuse this for negative cases so try clause is needed
        try:
            drop = result.find_element(*SearchResultsPageLocators.DROPDOWN_PARENT)
        except:
            drop = None
        return drop != None

    def is_dropdown_interactable(self):
        result = self.wait_load()[0] 
        #even tho wait load ensures the elements are loaded, 
        #we are testing INCASE it fails to load even when valid
        #we also reuse this for negative cases so try clause is needed
        try:
            drop = result.find_element(*SearchResultsPageLocators.DROPDOWN_PARENT)
            return EC.element_to_be_clickable(drop)
        except: #in case the row is valid but does not have a drop down
            return False
    
    def is_dropdown_set(self):
        # NOTE: this tests for the ability to set dropdown, thus needing at least 2 UNIQUE options
        old =""
        new =""
        try:
            result = self.wait_load()[0]
            old = result.find_element(*SearchResultsPageLocators.DROPDOWN_PARENT).text
            # since this is a div we cant use select, use custom func
            self.click_dropdown(result,1)
            # we will click index 1 as it is safer
            new = result.find_element(*SearchResultsPageLocators.DROPDOWN_PARENT).text
        except Exception as e:
            print(e)
        return old != new #if changed, wont be same
    
    def is_multiple_dropdown_valid(self):
        #checks if there is a correct amount of dropdown shown
        count = 0
        results = self.wait_load()
        valid_domain_count = self.get_valid_domains(results)
        for result in results:
            try:
                drop = result.find_element(*SearchResultsPageLocators.DROPDOWN_PARENT)
            except:
                drop = None
            if drop != None:
                count += 1
        return count == valid_domain_count
    
    def is_multiple_dropdown_set(self):
        results = self.wait_load()
        changed = 0
        valid_domain_count = self.get_valid_domains(results)
        for result in results:
            # we will only try to click on rows that are AVAILABLE
            if result.find_element(*SearchResultsPageLocators.RESULT_MSG).text == "This Domain is Available":
                try:
                    old = result.find_element(*SearchResultsPageLocators.DROPDOWN_PARENT).text
                    # since this is a div we cant use select, use custom func
                    self.click_dropdown(result,1)
                    # we will click index 1 as it is the safest (who knows if some has less options?)
                    new = result.find_element(*SearchResultsPageLocators.DROPDOWN_PARENT).text
                    if old != new: #if changed, wont be same
                        changed += 1
                except Exception as e:
                    print(e)
        return changed == valid_domain_count

    def is_add_clickable(self):
        results = self.wait_load()
        result = results[0]
        try:
            btn = result.find_element(*SearchResultsPageLocators.ADD_BTN)
            return EC.element_to_be_clickable(btn)
        except: #in case the row is valid but does not have a button
            return False

    def is_click_changing_btn(self,clicked=False):
        #clicked is to ease reuse when page is alreadey loaded before
        results = self.wait_load(noLoad = clicked)
        #if clicked, no load
        result = results[0]
        pre = ""
        post = ""
        btn = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(result.find_element(*SearchResultsPageLocators.ADD_BTN))
        )
        pre = btn.text
        btn.click()
        post = btn.text
        return pre!=post

    def is_multi_add_clickable(self):
        results = self.wait_load()
        clickable = 0
        valid_domain_count = self.get_valid_domains(results)
        for result in results:
            if self.domain_available(result):
                try:
                    btn = result.find_element(*SearchResultsPageLocators.ADD_BTN)
                    if EC.element_to_be_clickable(btn):
                        clickable += 1
                except Exception as e:
                        print(e)
        return clickable == valid_domain_count

    def is_multi_click_changing_btn(self,clicked=False):
        #clicked is to ease reuse when page is alreadey loaded before
        results = self.wait_load(noLoad = clicked)
        #need to scroll back up to home
        valid_domain_count = self.get_valid_domains(results)
        #if clicked, no load
        changed = 0
        for result in results:
            pre = ""
            post = ""
            if self.domain_available(result):
                try:
                    btn = WebDriverWait(self.driver,10).until(
                        EC.element_to_be_clickable(result.find_element(*SearchResultsPageLocators.ADD_BTN))
                    )
                    actions = ActionChains(self.driver)
                    actions.move_to_element(btn).perform()
                    pre = btn.text
                    btn.click()
                    post = btn.text
                    if pre!=post:
                        changed += 1
                except Exception as e:
                    print(e)
        return changed == valid_domain_count

    def is_one_added_to_summary(self,addAll=False):
        #this one tests if 1/1 available will be added properly in summary (adn reverse)
        results = self.wait_load()
        # first thing to do would be to get the initial (blank) state
        initSummaryEntries = self.get_summary()
        initTotalPrice = self.total_summary(initSummaryEntries)

        #now we will add the desired number of domains
        if addAll:
            self.click_add_all()
        else:
            self.add_one_to_cart(results)

        #then get all the new data
        newSummaryEntries = self.get_summary()
        newTotalPrice = self.total_summary(newSummaryEntries)

        #first test we want to do is to test if the total amount is no longer same as initstate after adding
        if initTotalPrice == newTotalPrice:
            print("Summary Total is still = to initial state")
            return False
        
        #then we will test if the non initial amount is correct
        displayedTotal = float(self.driver.find_element(*SearchResultsPageLocators.SUMMARY_TOTAL).text.split(" ")[1])
        expectedTotal = self.total_summary(newSummaryEntries)
        if displayedTotal != expectedTotal:
            print("The amount shown in total is incorrect:\nExpected:",expectedTotal," Displayed:",displayedTotal)
            #this assumes that the items' prices in summary is correct
            return False

        #check items in summary (single)
        if not self.summary_items_correct(results,newSummaryEntries,True):
            return False

        # if it reaches this point, no problems in normal flow
        # return True
        
        # reverse operation, undo adding the desired number of domains
        if addAll:
            self.click_add_all(noLoad=True)
        else:
            self.remove_one_from_cart(results)

        #then get all the new data
        newSummaryEntries = self.get_summary()
        newTotalPrice = self.total_summary(newSummaryEntries)

        #first test we want to do is to test if the total amount is no longer same as initstate after adding
        if initTotalPrice != newTotalPrice:
            print("[R] Summary Total is != to initial state")
            return False
        
        #then we will test if the non initial amount is correct
        displayedTotal = float(self.driver.find_element(*SearchResultsPageLocators.SUMMARY_TOTAL).text.split(" ")[1])
        expectedTotal = initTotalPrice
        if displayedTotal != expectedTotal:
            print("[R] The amount shown in total is incorrect:\nExpected:",expectedTotal," Displayed:",displayedTotal)
            #this assumes that the items' prices in summary is correct
            return False

        #then we will test if the amount of items is correct
        #for reverse, we just need to loop over all summary entries and see if it is blank
        for i in range(len(newSummaryEntries)):
            if newSummaryEntries[i][0].text != '':
                print("[R] There are still items in the summary listing at index: ",i)
                return False

        # if it reaches this point, no problems in normal AND reverse flow
        return True
    
    def is_all_added(self,addAll=False):
        #this one tests if everything available will be added properly in summary (and reversed)
        results = self.wait_load()
        # first thing to do would be to get the initial (blank) state
        initSummaryEntries = self.get_summary()
        initTotalPrice = self.total_summary(initSummaryEntries)

        #now we will add the desired number of domains
        if addAll:
            self.click_add_all()
        else:
            self.add_all_to_cart(results)

        #then get all the new data
        newSummaryEntries = self.get_summary()
        newTotalPrice = self.total_summary(newSummaryEntries)

        #first test we want to do is to test if the total amount is no longer same as initstate after adding
        if initTotalPrice == newTotalPrice:
            print("Summary Total is still = to initial state")
            return False
        
        #then we will test if the non initial amount is correct
        displayedTotal = float(self.driver.find_element(*SearchResultsPageLocators.SUMMARY_TOTAL).text.split(" ")[1])
        expectedTotal = self.total_summary(newSummaryEntries)
        if displayedTotal != expectedTotal:
            print("The amount shown in total is incorrect:\nExpected:",expectedTotal," Displayed:",displayedTotal)
            #this assumes that the items' prices in summary is correct
            return False

        # check if summary items are correct in MANY mode
        if not self.summary_items_correct(results,newSummaryEntries,False):
            return False

        # if it reaches this point, no problems in normal flow
        # return True
        
        # reverse operation, undo adding the desired number of domains
        if addAll:
            self.click_add_all(noLoad=True)
        else:
            self.remove_all_from_cart(results)

        #then get all the new data
        newSummaryEntries = self.get_summary()
        newTotalPrice = self.total_summary(newSummaryEntries)

        #first test we want to do is to test if the total amount is no longer same as initstate after adding
        if initTotalPrice != newTotalPrice:
            print("[R] Summary Total is != to initial state")
            return False
        
        #then we will test if the non initial amount is correct
        displayedTotal = float(self.driver.find_element(*SearchResultsPageLocators.SUMMARY_TOTAL).text.split(" ")[1])
        expectedTotal = initTotalPrice
        if displayedTotal != expectedTotal:
            print("[R] The amount shown in total is incorrect:\nExpected:",expectedTotal," Displayed:",displayedTotal)
            #this assumes that the items' prices in summary is correct
            return False

        #then we will test if the items are correct
        # regardless of type, this will work as reverse SHOULD revert to all blanks
        for i in range(len(newSummaryEntries)):
            if newSummaryEntries[i][0].text != '':
                print("[R] There are still items in the summary listing at index: ",i)
                return False

        # if it reaches this point, no problems in normal AND reverse flow
        return True

    def is_nothing_added(self,addAll=False):
        #this one tests if everything available will be added properly in summary (and reversed)
        results = self.wait_load()
        # first thing to do would be to get the initial (blank) state
        initSummaryEntries = self.get_summary()
        initTotalPrice = self.total_summary(initSummaryEntries)

        #now we will add the desired number of domains
        if addAll:
            self.click_add_all()
        else:
            self.add_all_to_cart(results)

        #then get all the new data
        newSummaryEntries = self.get_summary()
        newTotalPrice = self.total_summary(newSummaryEntries)

        #first test we want to do is to test if the total amount is still same as initstate 
        if initTotalPrice != newTotalPrice:
            print("Expected to get total proce of 0 but got "+str(newTotalPrice)+" instead!")
            return False
        
        #then we will test if the non initial amount is correct
        displayedTotal = float(self.driver.find_element(*SearchResultsPageLocators.SUMMARY_TOTAL).text.split(" ")[1])
        if displayedTotal != 0:
            print("The amount shown in total is incorrect:\nExpected:",0," Displayed:",displayedTotal)
            #this assumes that the items' prices in summary is correct
            return False

        # check if summary items are BLANKS 
        for i in range(len(newSummaryEntries)):
            if newSummaryEntries[i][0].text != '':
                return False

        # if it reaches this point, no problems in normal flow. we do not need reverse in invalid flow
        return True

    def is_add_prompt(self):
        msg = ""
        # test for the existence of a pop up dialog
        try:
            WebDriverWait(self.driver, 5).until (EC.alert_is_present())
            # switch_to.alert for switching to alert and accept
            alert = self.driver.switch_to.alert
            msg = alert.text
            # print(msg)
            alert.accept()
        except TimeoutException:
            # print("alert does not Exist in page")
            msg = "alert does not Exist in page"
        return msg == "No domains selected / available!"
            
class LoginPageContinue(BasePage):
    password_text_element = ContinuePasswordLoginElement() 
    captcha_text_element = ContinueCaptchaLoginElement() 
    #============================Helper Functions================================
    def click_login(self):
        btn = self.driver.find_element(*ContinueLoginPageLocators.LOGIN_BTN)
        btn.click()

    def enter_name(self, name):
        field = self.driver.find_element(*ContinueLoginPageLocators.NAME_FIELD)
        field.send_keys(name)

    def click_create(self):
        btn = self.driver.find_element(*ContinueLoginPageLocators.CREATE_BTN)
        btn.click()

    #-----------------------------------------------------------------------------
    def is_login_prompt(self):
        #test for page change and existence of fields, buttons
        # captcha img
        img = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ContinueLoginPageLocators.CAPTCHA_IMG)
        )
        if not img:
            print("Captcha img NOT Visible")
            return False
        else:
            print("Captcha img Visible")
        checkInteractable = {
            "name": (ContinueLoginPageLocators.NAME_FIELD),
            "pw": (ContinueLoginPageLocators.PASSWORD_FIELD),
            "captcha": (ContinueLoginPageLocators.CAPTCHA_FIELD),
            "login": (ContinueLoginPageLocators.LOGIN_BTN),
            "create": (ContinueLoginPageLocators.CREATE_BTN),
            "forgot_pw": (ContinueLoginPageLocators.FORGOT_PASSWORD),
            "forgot_name": (ContinueLoginPageLocators.FORGOT_USERNAME)
        }
        for elementName, locator in checkInteractable.items():
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            if not element:
                print(elementName,"NOT Interactable")
                return False
            else:
                print(elementName,"Interactable")
        # if it can make it to this stage, all elements are visible/interactable
        return True
    
    def is_login_invalid(self):
        self.click_login()
        msg = self.driver.find_element(By.CLASS_NAME,"alert-danger").text
        return msg == "The login details entered are incorrect, please enter the correct login details."

    def is_captcha_invalid(self):
        self.click_login()
        msg = self.driver.find_element(By.CLASS_NAME,"alert-danger").text
        return msg == "The captcha details entered are incorrect, please enter the correct captcha details."
            
class LoginPage(BasePage):
    username_text_element = NameLoginElement() 
    password_text_element = PasswordLoginElement() 
    captcha_text_element = CaptchaLoginElement() 
    # helper functions
    def click_login(self):
        btn = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
        btn.click()
    # -------------tests--------------
    
    def is_login_invalid(self):
        self.click_login()
        msg = self.driver.find_element(By.CLASS_NAME,"alert-danger").text
        return msg == "The login details entered are incorrect, please enter the correct login details."

    def is_captcha_invalid(self):
        self.click_login()
        msg = self.driver.find_element(By.CLASS_NAME,"alert-danger").text
        return msg == "The captcha details entered are incorrect, please enter the correct captcha details."
            
class CreatePage(BasePage):
    # a lot of fields are available, defining all first
    company_org = OrgElement() 
    contactPIC = ContactPicElement() 
    addr1 = AddrElement1()  
    addr2 = AddrElement2() 
    city = cityElement() 
    state = StateElement() 
    zipPO = zipPoElement() 
    #country is a dropdown, we need a helper for that
    phonePre = phonePreElement()
    phonePost = phonePostElement()
    mobilePre = mobilePreElement()
    mobilePost = mobilePostElement()
    faxPre = faxPreElement()
    faxPost = faxPostElement()
    email = emailElement()
    tax = taxElement()
    userID = userIDElement()
    password = passwordElement()
    confirmPassword = confirmPasswordElement()

    # ===================== helper functions ===================== 
    def randomUserName(self):
        rid = uuid.uuid4()
        # uuid for UNIQUE NAME
        return "can_delete_"+str(rid)

    def countrySelect(self):
        # this selects a random country
        # get dropdown parent element
        dropdown = self.driver.find_element(*CreatePageLocators.DROPDOWN_BOX)
        select = Select(dropdown)
        all_options = select.options
        i = random.randint(0,len(all_options))
        select.select_by_visible_text(all_options[i].text)

    def checkCheckBox(self):
        checkbox = self.driver.find_element(*CreatePageLocators.CHECKBOX)
        checkbox.click()

    def click_back(self):
        btn = self.driver.find_element(*CreatePageLocators.BACK_BTN)
        btn.click()

    def click_submit(self):
        btn = self.driver.find_element(*CreatePageLocators.SUBMIT_BTN)
        btn.click()

    #--------------------- tests ---------------------
    def is_checkbox_dialogue(self):
        msg = ""
        # test for the existence of a pop up dialog
        try:
            WebDriverWait(self.driver, 5).until (EC.alert_is_present())
            # switch_to.alert for switching to alert and accept
            alert = self.driver.switch_to.alert
            msg = alert.text
            # print(msg)
            alert.accept()
        except TimeoutException:
            # print("alert does not Exist in page")
            return False
        return True

    def is_form_valid(self):
        errors = self.driver.find_elements(*CreatePageLocators.ERROR_MSGS)
        if len(errors) == 0:
            return True
        else:
            #here we can do more form checking as there are a few variants of each error, but I am lazy
            #eg: username error may be BLANK OR TAKEN etc etc
            for error in errors:
                print(error.text)
            return False

class Step2Page(BasePage):
    # =================== Helper functions =================
    def click_continue(self):
        btn = self.driver.find_element(*Step2PageLocators.CONTINUE_BTN)
        btn.click()

    def add_whois(self):
        btn = self.driver.find_element(*Step2PageLocators.ADD_WHOIS)
        btn.click()
        
    def add_dnssec(self):
        btn = self.driver.find_element(*Step2PageLocators.ADD_DNSSEC)
        btn.click()        
        
    def get_summary(self,section): 
        # section will be the domain OR services section
        summDomains = section.find_elements(*Step2PageLocators.DOMAIN_NAME)
        summPrice = section.find_elements(*Step2PageLocators.DOMAIN_PRICE)
        return list(zip(summDomains, summPrice))

    def total_summary(self,domainSection):
        # calculate some stats for further verification
        # we can increase quality of validation by ensuring 
        # more than OLD on add or less than OLD on cancel
        summaryEntries = self.get_summary(domainSection)
        total = 0
        for d,p in summaryEntries:
            price = p.text.split(" ")
            if price[0] != '':
                total += float(price[1])
        return total

    def check_services(self,servicesSection):
        # the positions will be 1 if a non null item is found (more services may be introduced)
        summaryEntries = self.get_summary(servicesSection)
        positions = [0]*len(summaryEntries)
        i = 0
        for d,p in summaryEntries:
            # print(d.text,p.text)
            #here the price is listed as free, but it might not be a constant so we check for null only
            if d.text != '' and p.text != '':
                positions[i] = 1
            i+=1
        return positions

    #-------------------- tests --------------------
    def is_summary_valid(self,mode=1):
        # precondition: the domain section must be visible and with a non 0 price
        try:
            domainSection= WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located(Step2PageLocators.DOMAIN_SECTION)
            )
            if self.total_summary(domainSection) <= 0:
                print("Total price for all domains is <=0")
                return False
        except:
            print("Missing elements from domains section")
            return False
        # regardless of choice, VAS MUST ALWAYS BE PRESENT
        try:
            serviceSection = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located(Step2PageLocators.VAS_SECTION)
            )
        except:
            print("Services section is missing")
            return False
        # get all position of services 1 = something inside, 0 = ''
        services_position = self.check_services(serviceSection)
        if mode == 0:
            # nothing selected, VAS should still appaer but no contents
            if 1 in services_position:
                print("No services were selected but something is in the Value Added Services section")
                return False
        elif mode == 1:
            # who is selected (DEFAULT)
            if services_position[0] != 1:
                print("WHOIS is selected but it is not in its section")
                return False
        elif mode == 2:
            # dns selected
            if services_position[1] != 1:
                print("DNSSEC is selected but it is not in its section")
                return False
        elif mode == 3:
            # all selected
            # print(services_position)
            if 0 in services_position:
                print("BOTH are selected but soemthing is missing in the Value Added Services section")
                return False
        return True

    def is_reverse_summary_valid(self):
        # precondition: the domain section must still be visible and with a non 0 price
        try:
            domainSection = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located(Step2PageLocators.DOMAIN_SECTION)
            )
            if self.total_summary(domainSection) <= 0:
                print("Total price for all domains is <=0")
                return False
        except:
            print("Missing elements from domains section")
            return False
        # regardless of choice, VAS MUST ALWAYS BE PRESENT
        try:
            serviceSection = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located(Step2PageLocators.VAS_SECTION)
            )
        except:
            print("Services section is missing")
            return False
        # get all position of services 1 = something inside, 0 = ''
        # regardless of choice, on removal of all services, it MUST BE 0 filled
        if 1 in self.check_services(serviceSection):
            print("There are items in the services section after removal")
            return False
        return True

class Step3Page(BasePage):
    # =================== Helper functions =================
    def click_back(self):
        return

    def set_dropdown(self,index):
        drops = self.driver.find_elements(*Step3PageLocators.DROPDOWN_CONTAINERS)
        # drops will be ALL the drop downs (1-10)
        drops[index].click()
        # we try to get the select object WITH custom function since it is SPAN so we can randomize
        select = self.driver.find_elements(*Step3PageLocators.SELECT_OPTIONS)
        # here, we will  just pick a random one available using index
        choice = random.randint(0,len(select)-1)
        # it must be random because there might be domains tht have different year options, 
        # despite 1-5 being the majority
        # select choice
        select[choice].click()

    def click_checkout(self):
        btn = self.driver.find_element(*Step3PageLocators.CONTINUE_BTN)
        btn.click()

    def checkout_clickable(self):
        try:
            WebDriverWait(self.driver,10).until(
                 EC.element_to_be_clickable(Step3PageLocators.CONTINUE_BTN)
            )
            return True
        except: #if time out, button is not clickable
            return False

    def click_modify(self,index):
        modify_btns = self.driver.find_elements(*Step3PageLocators.MODIFY_BUTTONS)
        modify_btns[index].click()

    def checkAllCheckBox(self):
        btn = self.driver.find_element(*Step3PageLocators.CHECK_ALL)
        btn.click()

    def checkCheckBox(self,index):
        # note that the first one is the CHECK ALL box
        checks = self.driver.find_elements(*Step3PageLocators.CHECK_MARKS)
        checks[index].click()
        
    def selectYear(self):
        return

    #-------------------- tests --------------------
    def is_checkbox_error(self):
        msg = ""
        # test for the existence of a pop up dialog
        try:
            WebDriverWait(self.driver, 5).until (EC.alert_is_present())
            # switch_to.alert for switching to alert and accept
            alert = self.driver.switch_to.alert
            msg = alert.text
            # print(msg)
            alert.accept()
        except TimeoutException:
            print("alert does not Exist in page")
            return False
        return True

class ModifyPage(BasePage):
    def checkTnC(self):
        box = self.driver.find_element(*ModifyPageLocators.CHECKBOX)
        box.click()

    def fillRegistrant(self):
        box = self.driver.find_element(*ModifyPageLocators.CHECKBOX)
        box.click()

class Step4Page(BasePage):
    # =================== Helper functions =================
    def click_proceed(self):        
        btn = self.driver.find_element(*Step4PageLocators.CONTINUE_BTN)
        btn.click()

    def proceed_complete(self):
        btn = None
        try:
            btn = WebDriverWait(self.driver,15).until(
                EC.element_to_be_clickable(Step4PageLocators.CONTINUE_BTN)
            )
        except TimeoutException:
            print("Failed to reach the 4th page in time")
            return False
        # in case no time out but for somereason btn is none
        if btn:
            return True
        else:
            return False

    def checkCheckbox(self):
        checkbox = self.driver.find_element(*Step4PageLocators.CHECKBOX)
        checkbox.click()
        
    def add_dnssec(self):
        return

    #-------------------- tests --------------------
    def is_summary_valid(self):
        return True

class PaymentGatewayPage(BasePage):
    card_num_field = cardNumElement()
    cvv_field = cvvElement()
    # =================== Helper functions =================
    def click_samsung_pay(self):        
        btn = self.driver.find_element(*PaymentGatewayLocators.SAMSUNG_PAY)
        btn.click()

    def setExpYear(self):
        checkbox = self.driver.find_element(*PaymentGatewayLocators.CHECKBOX)
        checkbox.click()

    def setExpMonth(self):
        checkbox = self.driver.find_element(*PaymentGatewayLocators.CHECKBOX)
        checkbox.click()

    def click_reset(self):        
        btn = self.driver.find_element(*PaymentGatewayLocators.RESET_BTN)
        btn.click()

    def click_pay(self):        
        btn = self.driver.find_element(*PaymentGatewayLocators.CONTINUE_BTN)
        btn.click()

    def wait_gateway_load(self):
        # we simply wait until we can click samsung pay
        btn = WebDriverWait(self.driver,60).until(
            EC.element_to_be_clickable(PaymentGatewayLocators.SAMSUNG_PAY)
        )
        return btn

    #-------------------- tests --------------------
    def is_summary_valid(self):
        return True
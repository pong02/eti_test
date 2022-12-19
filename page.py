from locator import *
from element import BasePageElement
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class SearchTextElement(BasePageElement):
    locator = "domains"

# Due to the repeat in loginVO.username, we have to enter this manually
# class UsernameLoginElement(BasePageElement):
#     locator = "loginVO.username"

class PasswordLoginElement(BasePageElement):
    locator = "loginVO.password"

class CaptchaLoginElement(BasePageElement):
    locator = "loginVO.answer"

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

    def add_to_cart(self,domain_entry):
        if self.domain_available(domain_entry):
            try:
                #scrolling is actuallt NOT NEEDED as the topbar WILL NEVER block on 
                # the way down, but we keep it for completeness and safety
                actions = ActionChains(self.driver)
                btn = domain_entry.find_element(*SearchResultsPageLocators.ADD_BTN)
                actions.move_to_element(btn).perform()
                btn.click()
            except Exception as e:
                raise e

    def remove_from_cart(self,domain_entry):
        if self.domain_available(domain_entry):
            try:
                actions = ActionChains(self.driver)
                btn = domain_entry.find_element(*SearchResultsPageLocators.CANCEL_BTN)
                actions.move_to_element(btn).perform()
                btn.click()
            except Exception as e:
                raise e
    
    def summaryItemsMatch(self,summaryEntries,domain_entries,singleMode = False):
        # first we want to check what items are checked, put them in an array
        checked = self.get_valid_domain_names(domain_entries)
        # for all cases, as long as it is available, we will add it
        displayed = []
        # then we will get the items in summary to compare

        for d,p in summaryEntries:
            if d.text != '':
                displayed.append(d.text)
        if singleMode:
            return displayed[0] in checked
        # compare using set in case ordering changes
        return set(checked) == set(displayed)

    def summaryIsBlank(self,summaryEntries):
        #this one can only be used for singleMode, as it is the only way to 
        #overcome the weakness of the 1 blank element by default design
        return summaryEntries[0][0] == ""

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

    def checkSummaryItems(self, oldItemCount, summaryEntries, revert= False):
        # special case, due to the element being summoned with "" rather than 
        # not summoned at all, there is this special case with length checking
        # when there is only 1 available and 1 is added, both sides will be 1
        if len(summaryEntries) == 1 and oldItemCount == 1:
            if summaryEntries[0][0] != "":
                return True
            else:
                return False
        elif revert:
            # whoever thought it was a good idea to keep blank elements as ""
            for entry in summaryEntries:
                if entry[0] != "":
                    return False
            return True
        else:
            return (oldItemCount!=len(summaryEntries))
    
    def clearedSummaryItems(self,summaryEntries):
    # def summaryItemsMatch(self,summaryEntries,domain_entries,singleMode = False):
        displayed = []
        for d,p in summaryEntries:
            if d.text != '':
                displayed.append(d.text)
        # compare using set in case ordering changes
        return [] == set(displayed)

    def click_continue(self):
        submit = self.driver.find_element(*SearchResultsPageLocators.CONTINUE)
        submit.click()

    def click_add_all(self,noLoad = False):
        self.wait_load(noLoad)
        add_all = self.driver.find_element(*SearchResultsPageLocators.ADD_ALL)
        add_all.click()
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

    def is_summary_added(self,addMode):
        results = self.wait_load()

        # initial state compute, before it gets detached
        oldSummaryEntries = self.get_summary()
        oldTotal = self.total_summary(oldSummaryEntries)
        oldItemCount = len(oldSummaryEntries)

        #addMode = 0 add only 1 via add
        #addMode = 1 add multiple via adds
        #addMode = 2 add everything using add all 
        if addMode == 0:
            # click only the first
            self.add_to_cart(results[0])
            # THIS IS ASSUMING THE FIRST ONE ALWAYS WORKS< DANGEROUD
            
        elif addMode == 1:
            # click all but one by one
            for result in results:
                self.add_to_cart(result)
            
        elif addMode == 2:
            self.click_add_all()
        
        # get the new summary items
        summaryEntries = self.get_summary()

        # check if item display is no longer empty and total no longer 0
        totalUpdated = (oldTotal != self.total_summary(summaryEntries))
        itemsUpdated = self.checkSummaryItems(oldItemCount,summaryEntries)

        totalDisplay = self.driver.find_element(*SearchResultsPageLocators.SUMMARY_TOTAL)
        #check if items and total displayed is correct
        displayedTotal = float(totalDisplay.text.split(" ")[1])
        totalAccurate = (displayedTotal == self.total_summary(summaryEntries))
        # this is an unavoidable loophole, the fact that there will always be 1
        # element on display restricts us from ever checking on cancel in singlemode
        # elif len(summaryEntries)==1 and singleMode and len(checked)==1:
            # return True 
        if addMode == 0:
            itemsAccurate = self.summaryItemsMatch(summaryEntries,results,singleMode=True)
        else:
            itemsAccurate = self.summaryItemsMatch(summaryEntries,results,singleMode=False)
        #now items accurate and items updated for revert is wrong
        print ([totalUpdated , itemsUpdated , totalAccurate , itemsAccurate])
        return totalUpdated and itemsUpdated and totalAccurate and itemsAccurate

    def is_summary_cleared(self,addMode):
        #TODO: THIS DOES NOT WORK YET BECAUSE OF THE "" ON REMOVE
        results = self.wait_load(noLoad=True)

        #addMode = 0 add only 1 via add
        #addMode = 1 add multiple via adds
        #addMode = 2 add everything using add all 
        if addMode == 0:
            # click only the first
            self.remove_from_cart(results[0])
        elif addMode == 1:
            # click all but one by one
            for result in results:
                self.remove_from_cart(result)
            
        elif addMode == 2:
            # when revert we dont need to wait load
            self.click_add_all(noLoad=True)
        
        # get the new summary items
        summaryEntries = self.get_summary()

        # check if item display is  0
        totalUpdated = (0 == self.total_summary(summaryEntries))
        # since the items remain present but as "", it will never be len 0
        # so we will start looping the entries to check if it is all blank
        for entry in summaryEntries:
            if entry[0] != "":
                itemsUpdated = False
        itemsUpdated = (len(summaryEntries) == 0)

        totalDisplay = self.driver.find_element(*SearchResultsPageLocators.SUMMARY_TOTAL)
        #check if items and total displayed is correct
        displayedTotal = float(totalDisplay.text.split(" ")[1])
        totalAccurate = (displayedTotal == 0)
        # this is an unavoidable loophole, the fact that there will always be 1
        # element on display restricts us from ever checking on cancel in singlemode
        # elif len(summaryEntries)==1 and singleMode and len(checked)==1:
            # return True 
        if addMode == 0:
            #on single revert, we just need to check if it is BLANK
            itemsAccurate = self.summaryIsBlank(summaryEntries)
        else:
            itemsAccurate = self.clearedSummaryItems(summaryEntries)
        #now items accurate and items updated for revert is wrong
        print ([totalUpdated , itemsUpdated , totalAccurate , itemsAccurate])
        return totalUpdated and itemsUpdated and totalAccurate and itemsAccurate

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
            
class LoginPage(BasePage):
    password_text_element = PasswordLoginElement() 
    captcha_text_element = CaptchaLoginElement() 
    #============================Helper Functions================================
    # def click_dropdown(self,domain_entry,target_index):
    #     #we just need to check if the text in drop changed
    #     #this is needed because the dropdowns are NOT select elements, but div
    #     #domain entry will be a SINGLE ROW in results page (result)
    #     drop = domain_entry.find_element(*SearchResultsPageLocators.DROPDOWN_PARENT)
    #     drop.click()
    #     dropdown = domain_entry.find_element(*SearchResultsPageLocators.DROPDOWN_BOX)
    #     options = dropdown.find_elements(*SearchResultsPageLocators.DROPDOWN_OPTIONS)
    #     options[target_index].click()
    def click_login(self):
        btn = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
        btn.click()

    def enter_name(self, name):
        field = self.driver.find_element(*LoginPageLocators.NAME_FIELD)
        field.send_keys(name)

    #-----------------------------------------------------------------------------
    def is_login_prompt(self):
        #test for page change and existence of fields, buttons
        # captcha img
        img = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.CAPTCHA_IMG)
        )
        if not img:
            print("Captcha img NOT Visible")
            return False
        else:
            print("Captcha img Visible")
        checkInteractable = {
            "name": (LoginPageLocators.NAME_FIELD),
            "pw": (LoginPageLocators.PASSWORD_FIELD),
            "captcha": (LoginPageLocators.CAPTCHA_FIELD),
            "login": (LoginPageLocators.LOGIN_BTN),
            "create": (LoginPageLocators.CREATE_BTN),
            "forgot_pw": (LoginPageLocators.FORGOT_PASSWORD),
            "forgot_name": (LoginPageLocators.FORGOT_USERNAME)
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
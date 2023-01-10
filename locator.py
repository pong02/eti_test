# any identifier for elements must be kept here to limit change areas, separated by pages
    # for use in find_element, unpack with *, otherwise, no need
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SEARCH_BUTTON = (By.ID, "singleRegSearchButton")
    SEARCH_TEXT = (By.ID, "domains")
    LOGIN_BUTTON = (By.ID, "myAccountDropdown")

class SearchResultsPageLocators(object):
    CONTINUE = (By.CLASS_NAME,"btn-lg")
    RESULTS = (By.CLASS_NAME,"domainListingSearch") #we can get an array from this
    RESULT_CONTAINER = (By.CLASS_NAME,"cart-container")
    DOMAIN_NAME = (By.ID,"displayDomain")
    SPINNER = (By.TAG_NAME,"i")
    DROPDOWN_PARENT = (By.CLASS_NAME,"select-styled")
    DROPDOWN_BOX = (By.CLASS_NAME,"select-options")
    DROPDOWN_OPTIONS = (By.TAG_NAME,"li")
    RESULT_MSG = (By.TAG_NAME,"p") #singular
    ADD_BTN = (By.CLASS_NAME,"btn-success")
    CANCEL_BTN = (By.CLASS_NAME,"label-on")
    ADD_ALL = (By.ID,"labelCheckUncheckAll")
    SUMMARY = (By.CLASS_NAME,"col-lg-5")
    SUMMARY_DOMAINS = (By.CLASS_NAME,"price-list")
    SUMMARY_PRICE = (By.CLASS_NAME,"order-list")
    SUMMARY_TOTAL = (By.TAG_NAME,"h3")
    POP_UP = (By.CSS_SELECTOR,"#overlay-abudhabi")
    POP_UP_ACCEPT = (By.CSS_SELECTOR, 'input')
    # summary initial state

class ContinueLoginPageLocators(object):
    NAME_FIELD = (By.XPATH,"//*[@id=\"verifyUserForm\"]/div/div[1]/div[3]/div/input")
    PASSWORD_FIELD = (By.XPATH,"//*[@id=\"verifyUserForm\"]/div/div[1]/div[4]/div/input")
    CAPTCHA_IMG = (By.XPATH,"//*[@id=\"captchaimg\"]")
    CAPTCHA_FIELD = (By.XPATH,"//*[@id=\"verifyUserForm\"]/div/div[1]/div[5]/div[2]/input")
    LOGIN_BTN = (By.XPATH,"//*[@id=\"verifyUserForm\"]/div/div[1]/button")
    CREATE_BTN = (By.XPATH,"//*[@id=\"verifyUserForm\"]/div/div[2]/button")
    FORGOT_USERNAME = (By.XPATH,"//*[@id=\"verifyUserForm\"]/div/div[1]/div[6]/div[1]/a")
    FORGOT_PASSWORD = (By.XPATH,"//*[@id=\"verifyUserForm\"]/div/div[1]/div[6]/div[2]/a")

class LoginPageLocators(object):
    LOGIN_BTN = (By.XPATH,'//*[@id="login"]/div/div/button')
    NAME_FIELD = (By.XPATH,'//*[@id="login"]/div/div/div[2]/div/input')
    PASSWORD_FIELD = (By.XPATH,'//*[@id="login"]/div/div/div[3]/div/input')
    CAPTCHA_IMG = (By.XPATH,'//*[@id="captchaimg"]')
    CAPTCHA_FIELD = (By.XPATH,'//*[@id="answer"]')
    FORGOT_USERNAME = (By.XPATH,'//*[@id="login"]/div/div/div[5]/div[1]/a')
    FORGOT_PASSWORD = (By.XPATH,'//*[@id="login"]/div/div/div[5]/div[2]/a')

class CreatePageLocators(object):
    # DROPDOWN_PARENT = (By.CLASS_NAME,"select-styled")
    DROPDOWN_BOX = (By.NAME,"userAccountVO.countryid")
    SUBMIT_BTN = (By.NAME,"_eventId_next")
    BACK_BTN = (By.XPATH,'/html/body/section/div/div/div/form/div[6]/div/div[14]/button[1]')
    CHECKBOX = (By.ID,"agreement")
    ERROR_MSGS = (By.CLASS_NAME,"alert-danger")

class Step2PageLocators(object):
    CONTINUE_BTN = (By.NAME,'_eventId_next')
    ADD_WHOIS = (By.XPATH,'//*[@id="label-3"]')
    ADD_DNSSEC = (By.ID,'label-6')
    DOMAIN_SECTION = (By.XPATH,'//*[@id="domainDetails-1030kasd"]')
    VAS_SECTION = (By.ID,"domainDetails-1030kvas")
    DOMAIN_NAME = (By.CLASS_NAME,"price-list")
    DOMAIN_PRICE = (By.CLASS_NAME,"order-list")

class Step3PageLocators(object):
    CONTINUE_BTN = (By.NAME,'_eventId_checkout')
    BACK_BTN = (By.NAME,'_eventId_editvas')
    CHECK_ALL = (By.NAME,'Check_ctr')
    CHECK_MARKS = (By.CLASS_NAME,'checkmark') 
    MODIFY_BUTTONS = (By.NAME, '_eventId_configure')
    DROPDOWN_CONTAINERS= (By.CLASS_NAME, 'selection')
    SELECT_OPTIONS = (By.CLASS_NAME, 'select2-results__option')

class ModifyPageLocators(object):
    # this section is for objects that are not constant throughout the page
    # CHECKBOX IS ACTUALLY NOT BOUND TO ANY TABS
    CHECKBOX = (By.XPATH,'//*[@id="agreement"]')
    # TABS
    REGISTRANT_TAB = (By.XPATH,'//*[@id="reg-tab"]')
    ADMIN_TAB = (By.XPATH,'//*[@id="myTab"]/li[2]')
    TECHNICAL_TAB = (By.XPATH,'//*[@id="myTab"]/li[3]')
    BILLING_TAB = (By.XPATH,'//*[@id="myTab"]/li[4]')
    COPY_SELECT_ADMIN = (By.XPATH,'//*[@id="selectSameAs_adm"]')
    COPY_SELECT_TECH = (By.XPATH,'//*[@id="selectSameAs_tec"]')
    COPY_SELECT_BILL = (By.XPATH,'//*[@id="selectSameAs_bil"]')
    # EVERYTHING ELSE IS BOUND TO TABS, AND HAVE EXACTLY THE SAME XPATH OTHER THAN ID
    # SINCE XPATH MANIPULATION IS WAY EASIER, WE WILL NOT USE BASIC LOCATORS
    '''//*[@id="regTab"]
    //*[@id="admTab"]
    //*[@id="tecTab"]
    //*[@id="bilTab"]'''
    # default will be regTab, so 
    tab = 'regTab'
    ORG_NAME = ("By.XPATH",'//*[@id="'+tab+'"]/div[3]/div/input')
    FNAME = ("By.XPATH",'//*[@id="'+tab+'"]/div[4]/div[1]/input')
    LNAME = ("By.XPATH",'//*[@id="'+tab+'"]/div[4]/div[2]/input')
    ADDR_1 = ("By.XPATH",'//*[@id="'+tab+'"]/div[5]/div/input')
    ADDR_2 = ("By.XPATH",'//*[@id="'+tab+'"]/div[6]/div/input')
    CITY = ("By.XPATH",'//*[@id="'+tab+'"]/div[7]/div[1]/input')
    STATE = ("By.XPATH",'//*[@id="'+tab+'"]/div[7]/div[2]/input')
    POSTCODE = ("By.XPATH",'//*[@id="'+tab+'"]/div[8]/div[1]/input')
    COUNTRY_SELECT = ("By.XPATH",'//*[@id="'+tab+'"]/div[8]/div[2]/select')
    PHONE_0 = ("By.XPATH",'//*[@id="'+tab+'"]/div[9]/div/div/input[1]')
    PHONE_1 = ("By.XPATH",'//*[@id="'+tab+'"]/div[9]/div/div/input[2]')
    FAX_0 = ("By.XPATH",'//*[@id="'+tab+'"]/div[10]/div/div/input[1]')
    FAX_1 = ("By.XPATH",'//*[@id="'+tab+'"]/div[10]/div/div/input[2]')
    EMAIL = ("By.XPATH",'//*[@id="'+tab+'"]/div[11]/div/input')
    ORG_NAME = ("By.XPATH",'//*[@id="'+tab+'"]/div[3]/div/input')
    FNAME = ("By.XPATH",'//*[@id="'+tab+'"]/div[4]/div[1]/input')
    LNAME = ("By.XPATH",'//*[@id="'+tab+'"]/div[4]/div[2]/input')
    ADDR_1 = ("By.XPATH",'//*[@id="'+tab+'"]/div[5]/div/input')
    ADDR_2 = ("By.XPATH",'//*[@id="'+tab+'"]/div[6]/div/input')
    CITY = ("By.XPATH",'//*[@id="'+tab+'"]/div[7]/div[1]/input')
    STATE = ("By.XPATH",'//*[@id="'+tab+'"]/div[7]/div[2]/input')
    POSTCODE = ("By.XPATH",'//*[@id="'+tab+'"]/div[8]/div[1]/input')
    COUNTRY_SELECT = ("By.XPATH",'//*[@id="'+tab+'"]/div[8]/div[2]/select')
    PHONE_0 = ("By.XPATH",'//*[@id="'+tab+'"]/div[9]/div/div/input[1]')
    PHONE_1 = ("By.XPATH",'//*[@id="'+tab+'"]/div[9]/div/div/input[2]')
    FAX_0 = ("By.XPATH",'//*[@id="'+tab+'"]/div[10]/div/div/input[1]')
    FAX_1 = ("By.XPATH",'//*[@id="'+tab+'"]/div[10]/div/div/input[2]')
    EMAIL = ("By.XPATH",'//*[@id="'+tab+'"]/div[11]/div/input')

# manually update all items
def setTab(instance,tabID):
    tab = tabID
    instance.ORG_NAME = ("By.XPATH",'//*[@id="'+tab+'"]/div[3]/div/input')
    instance.FNAME = ("By.XPATH",'//*[@id="'+tab+'"]/div[4]/div[1]/input')
    instance.LNAME = ("By.XPATH",'//*[@id="'+tab+'"]/div[4]/div[2]/input')
    instance.ADDR_1 = ("By.XPATH",'//*[@id="'+tab+'"]/div[5]/div/input')
    instance.ADDR_2 = ("By.XPATH",'//*[@id="'+tab+'"]/div[6]/div/input')
    instance.CITY = ("By.XPATH",'//*[@id="'+tab+'"]/div[7]/div[1]/input')
    instance.STATE = ("By.XPATH",'//*[@id="'+tab+'"]/div[7]/div[2]/input')
    instance.POSTCODE = ("By.XPATH",'//*[@id="'+tab+'"]/div[8]/div[1]/input')
    instance.COUNTRY_SELECT = ("By.XPATH",'//*[@id="'+tab+'"]/div[8]/div[2]/select')
    instance.PHONE_0 = ("By.XPATH",'//*[@id="'+tab+'"]/div[9]/div/div/input[1]')
    instance.PHONE_1 = ("By.XPATH",'//*[@id="'+tab+'"]/div[9]/div/div/input[2]')
    instance.FAX_0 = ("By.XPATH",'//*[@id="'+tab+'"]/div[10]/div/div/input[1]')
    instance.FAX_1 = ("By.XPATH",'//*[@id="'+tab+'"]/div[10]/div/div/input[2]')
    instance.EMAIL = ("By.XPATH",'//*[@id="'+tab+'"]/div[11]/div/input')
    instance.ORG_NAME = ("By.XPATH",'//*[@id="'+tab+'"]/div[3]/div/input')
    instance.FNAME = ("By.XPATH",'//*[@id="'+tab+'"]/div[4]/div[1]/input')
    instance.LNAME = ("By.XPATH",'//*[@id="'+tab+'"]/div[4]/div[2]/input')
    instance.ADDR_1 = ("By.XPATH",'//*[@id="'+tab+'"]/div[5]/div/input')
    instance.ADDR_2 = ("By.XPATH",'//*[@id="'+tab+'"]/div[6]/div/input')
    instance.CITY = ("By.XPATH",'//*[@id="'+tab+'"]/div[7]/div[1]/input')
    instance.STATE = ("By.XPATH",'//*[@id="'+tab+'"]/div[7]/div[2]/input')
    instance.POSTCODE = ("By.XPATH",'//*[@id="'+tab+'"]/div[8]/div[1]/input')
    instance.COUNTRY_SELECT = ("By.XPATH",'//*[@id="'+tab+'"]/div[8]/div[2]/select')
    instance.PHONE_0 = ("By.XPATH",'//*[@id="'+tab+'"]/div[9]/div/div/input[1]')
    instance.PHONE_1 = ("By.XPATH",'//*[@id="'+tab+'"]/div[9]/div/div/input[2]')
    instance.FAX_0 = ("By.XPATH",'//*[@id="'+tab+'"]/div[10]/div/div/input[1]')
    instance.FAX_1 = ("By.XPATH",'//*[@id="'+tab+'"]/div[10]/div/div/input[2]')
    instance.EMAIL = ("By.XPATH",'//*[@id="'+tab+'"]/div[11]/div/input')

class Step4PageLocators(object):
    CONTINUE_BTN = (By.NAME,'_eventId_submit')
    CHECKBOX = (By.ID, "agreement")

class PaymentGatewayLocators(object):
    CARD_NUM = (By.ID,"cardNumber")
    SAMSUNG_PAY = (By.XPATH,'//*[@id="PaymentData"]/div[2]/div[1]/div/div[3]/input')
    RESET_BTN = (By.XPATH,'//*[@id="SharedLayoutBody"]/div[1]/div/div[1]/div[6]/div[1]/button')
    CONTINUE_BTN = (By.XPATH,'//*[@id="SharedLayoutBody"]/div[1]/div/div[1]/div[6]/div[6]/input')
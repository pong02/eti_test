# any identifier for elements must be kept here to limit change areas, separated by pages
    # for use in find_element, unpack with *, otherwise, no need
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SEARCH_BUTTON = (By.ID, "singleRegSearchButton")
    SEARCH_TEXT = (By.ID, "domains")

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
    # summary initial state

class LoginPageLocators(object):
    NAME_FIELD = (By.XPATH,"//*[@id=\"verifyUserForm\"]/div/div[1]/div[3]/div/input")
    PASSWORD_FIELD = (By.XPATH,"//*[@id=\"verifyUserForm\"]/div/div[1]/div[4]/div/input")
    CAPTCHA_IMG = (By.XPATH,"//*[@id=\"captchaimg\"]")
    CAPTCHA_FIELD = (By.XPATH,"//*[@id=\"verifyUserForm\"]/div/div[1]/div[5]/div[2]/input")
    LOGIN_BTN = (By.XPATH,"//*[@id=\"verifyUserForm\"]/div/div[1]/button")
    CREATE_BTN = (By.XPATH,"//*[@id=\"verifyUserForm\"]/div/div[2]/button")
    FORGOT_USERNAME = (By.XPATH,"//*[@id=\"verifyUserForm\"]/div/div[1]/div[6]/div[1]/a")
    FORGOT_PASSWORD = (By.XPATH,"//*[@id=\"verifyUserForm\"]/div/div[1]/div[6]/div[2]/a")
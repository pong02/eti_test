# any identifier for elements must be kept here to limit change areas, separated by pages
    # for use in find_element, unpack with *, otherwise, no need
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SEARCH_BUTTON = (By.ID, "singleRegSearchButton")
    SEARCH_TEXT = (By.ID, "domains")

class SearchResultsPageLocators(object):
    CONTINUE = (By.LINK_TEXT,"Continue")
    RESULTS = (By.CLASS_NAME,"domainListingSearch") #we can get an array from this
    RESULT_CONTAINER = (By.CLASS_NAME,"cart-container")
    SPINNER = (By.TAG_NAME,"i")
    DROPDOWN_PARENT = (By.CLASS_NAME,"select-styled")
    DROPDOWN_BOX = (By.CLASS_NAME,"select-options")
    DROPDOWN_OPTIONS = (By.TAG_NAME,"li")
    RESULT_MSG = (By.TAG_NAME,"p") #singular
    ADD_BTN = (By.CLASS_NAME,"btn-success")

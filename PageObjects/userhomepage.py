from selenium.webdriver.common.by import By


class userhome:

    # constructor to get the driver
    def __init__(self, testdriver):
        self.localdriver = testdriver

    # locators
    Usrtitle = (By.CLASS_NAME, "account")
    Personal = (By.PARTIAL_LINK_TEXT, "personal")

    #methods to return locators
    def getusrtitle(self):
        return self.localdriver.find_element(*userhome.Usrtitle)

    def getpersonaldet(self):
        return self.localdriver.find_element(*userhome.Personal)

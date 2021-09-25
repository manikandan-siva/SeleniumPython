from selenium.webdriver.common.by import By


class userhome:

    def __init__(self, testdriver):
        self.localdriver = testdriver

    Usrtitle = (By.CLASS_NAME, "account")

    def getusrtitle(self):
        return self.localdriver.find_element(*userhome.Usrtitle)

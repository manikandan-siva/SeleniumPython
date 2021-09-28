from selenium.webdriver.common.by import By
from PageObjects.createaccountpage import createaccountpage


class sitehomepage:

    # constructor to assign the driver to local driver
    def __init__(self, testdriver):  # , email):
        self.localdriver = testdriver
        # self.localemail = email

    # now identify locators for each weblement and store it in variables
    Signin = (By.PARTIAL_LINK_TEXT, "Sign")

    # now methods via which these locators will be used
    def signinbutton(self):
        self.localdriver.find_element(*sitehomepage.Signin).click()
        Createaccount = createaccountpage(self.localdriver)  # , localemail)
        return Createaccount

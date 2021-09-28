from selenium.webdriver.common.by import By
from PageObjects.personalinfopage import personalinfo


class createaccountpage:

    # constructor to assign the driver locally
    def __init__(self, testdriver):
        self.localdriver = testdriver

    # webelements
    Email = (By.ID, "email_create")
    Submit = (By.ID, "SubmitCreate")

    # methods to return webelements
    def enteremail(self):
        return self.localdriver.find_element(*createaccountpage.Email)


    def createaccount(self):
        self.localdriver.find_element(*createaccountpage.Submit).click()
        Usrdet = personalinfo(self.localdriver)
        return Usrdet

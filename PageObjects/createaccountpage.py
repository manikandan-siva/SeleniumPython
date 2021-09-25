from selenium.webdriver.common.by import By
from PageObjects.personalinfopage import personalinfo


class createaccountpage:

    # constructor to assign the driver locally
    def __init__(self, testdriver):  # , email):
        self.localdriver = testdriver
        # self.email = ""
        # self.email = email

    Email = (By.ID, "email_create")
    Submit = (By.ID, "SubmitCreate")

    # def createaccount(self, email):
    def enteremail(self):
        # print(self.email)
        # self.localdriver.find_element(*createaccountpage.Email).send_keys(self.email)
        return self.localdriver.find_element(*createaccountpage.Email)

        # print("email entered", self.email)

    def createaccount(self):
        self.localdriver.find_element(*createaccountpage.Submit).click()
        print("submitted")
        Usrdet = personalinfo(self.localdriver)
        return Usrdet

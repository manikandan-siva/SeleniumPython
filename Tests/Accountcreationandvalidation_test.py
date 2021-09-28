#inbuilt packages
import time
import pytest

#selenium package
from selenium import webdriver

#Other python files
from Utilities.BaseClass import BaseClass
from PageObjects.sitehomepage import sitehomepage
from PageObjects.createaccountpage import createaccountpage
from PageObjects.personalinfopage import personalinfo
from TestData.readexcel import readexcel


# class with all test cases
class TestEcommercesiteoperations(BaseClass):

    #test case for new user account creation and validation
    def test_accountcreationandvalidation(self, getdata):
    #def test_accountcreationandvalidation(self):
        testlog = self.logconfig()
        testlog.info("Webdriver initiated and URL opened")
        testlog.info("Reading login page")
        Home = sitehomepage(self.testdriver)

        testlog.info("Ready to login")
        self.visibilitycheckbylink("Sign")
        Acc = Home.signinbutton()

        testlog.info("Ready to give email details " + getdata["Email"])
        self.visibilitycheckbyid("SubmitCreate")
        #testlog.info("Ready to give email details " + self.userdata["Email"])   #self.getdata["Email"])
        # Acc.enteremail().send_keys(self.testemail)
        Acc.enteremail().send_keys(getdata["Email"])
        #Acc.enteremail().send_keys(self.getdata["Email"])
        testlog.info("Email entered") # ,self.testemail)

        testlog.info("Registering Email and navigating to user details page")
        Usrdet = Acc.createaccount()

        testlog.info("Providing user details")
        self.visibilitycheckbyid("submitAccount")
        testlog.info("selecting title "+getdata["Title"])
        if getdata["Title"] == "Mr":
            Usrdet.titleselectmr().click()
        else:
            Usrdet.titleselectmrs().click()

        testlog.info("Entering first name "+getdata["Fname"])
        Usrdet.setfname().send_keys(getdata["Fname"])

        testlog.info("Entering last name "+getdata["Lname"])
        Usrdet.setlname().send_keys(getdata["Lname"])

        testlog.info("Entering password"+getdata["Pwd"])
        Usrdet.setpwd().send_keys(getdata["Pwd"])

        testlog.info("Entering address "+getdata["Addrs"])
        Usrdet.setaddrs().send_keys(getdata["Addrs"])

        testlog.info("Entering city "+getdata["City"])
        Usrdet.setcity().send_keys(getdata["City"])

        testlog.info("Entering state "+getdata["State"])
        self.dropdownselector(Usrdet.setstate(), getdata["State"])

        testlog.info("Entering postalcode "+str(getdata["PC"]))
        Usrdet.setpost().send_keys(getdata["PC"])

        testlog.info("Entering additional info "+getdata["AI"])
        Usrdet.setaddninfo().send_keys(getdata["AI"])

        testlog.info("Entering mobile no "+str(getdata["Mobile"]))
        Usrdet.setmobile().send_keys(getdata["Mobile"])

        testlog.info("Submitting")
        Usrhome = Usrdet.register()

        testlog.info("Valdiating user creation")
        self.visibilitycheckbylink("out")

        if getdata["Fname"] in Usrhome.getusrtitle().text:
            testlog.info(Usrhome.getusrtitle().text+" user creation successful")
            Usrhome.getpersonaldet().click()
        else:
            testlog.error("User creation failed")


# fixture to read excel
@pytest.fixture(params = [readexcel.getdatafromexcel("User1"), readexcel.getdatafromexcel("User2"), readexcel.getdatafromexcel("User3")])
#@pytest.fixture(params = [readexcel.getdatafromexcel("User1")])
def getdata(request):
    return request.param
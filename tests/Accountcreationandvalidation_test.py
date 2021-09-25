import time

from selenium import webdriver
from Utilities.BaseClass import BaseClass
from PageObjects.sitehomepage import sitehomepage
from PageObjects.createaccountpage import createaccountpage
from PageObjects.personalinfopage import personalinfo


class Testaccountcreationandvalidation(BaseClass):
    def test_accountcreationandvalidation(self):
        # Home = sitehomepage(self.testdriver)
        print("Reading login page")
        Home = sitehomepage(self.testdriver)

        print("ready to login")
        Acc = Home.signinbutton()
        print("ready to give email")
        time.sleep(2)

        print(self.testemail)
        Acc.enteremail().send_keys(self.testemail)
        print("Email entered")
        # Acc.createaccount()
        print("providing user details")
        Usrdet = Acc.createaccount()

        print("selecting title")
        time.sleep(3)
        Usrdet.titleselect().click()
        print("entering first name")
        Usrdet.setfname().send_keys("mani")
        print("entering last name")
        Usrdet.setlname().send_keys("kandan")
        print("entering password")
        Usrdet.setpwd().send_keys("pwd12")
        print("entering address")
        Usrdet.setaddrs().send_keys("addrs")
        print("entering city")
        Usrdet.setcity().send_keys("city")
        print("entering state")
        self.dropdownselector(Usrdet.setstate(), "California")
        print("entering postalcode")
        Usrdet.setpost().send_keys("00000")
        print("entering addn info")
        Usrdet.setaddninfo().send_keys("info")
        print("entering mobile no")
        Usrdet.setmobile().send_keys("1234567890")
        print("submitting")
        # Usrdet.register().click()
        Usrhome = Usrdet.register()
        print("validating")
        print(Usrhome.getusrtitle().text)
        if "mani kandan" == Usrhome.getusrtitle().text:
            print("user creation successfull")

        # Acc.createaccount(self, email)
        # print(Home.text)
        # print("I am here")
        # Home.signinbutton().click()

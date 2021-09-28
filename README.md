# Selenium_Pytest_framework_ecommerce
Selenium pytest framework to automate testing of e-commerce webpage operations

My framework will read user details from excel and then create account for each user in an e-commerce webpage.

Steps Automated:
1. Open  url  
2. Click on sign in link.
3. Enter email address in 'Create and account' section.
4. Click on Create an Account button.
5. Enter personal details
6. Click on Register button.
7. Validate that user is created.


Folder structure and class details
1)PageObjects - Each file contains webelement details about each page in e-commerce site(Sitehomepage -> createaccountpage -> personalinfopage -> userhomepage).
I have written constructor to get the driver first, then webelement locator, methods to return that locator to test cases, hybrid methods to call other page objects classes, 
which will be redirected from first pageobjects operations like login button in home screen to login screen and return corresponding object 
2)Reports - Storing logfile, screenshots and reports generated
3)Testdata - File to read excel(readexcel) and the source excel file
4)Tests - conftest file with fixture function to define driver and call url, assign that driver to our testcase class driver, code flexibility to decide the browser is added here. 
SS capture and integrate with the report code is added here. Added test cases file (make sure class and method name starts with test) and inherit base class from utility and 
call page objects methods to execute desired actions in our webpage.
5)Utilities - Baseclass file which will call conftest fixtures,then added select generic method to select values from any drop down, logging configuration and explicit wait config


ecommerce.py - selenium python file to exercise the code before using it in framework

import inspect
import logging
import pytest

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as EW

@pytest.mark.usefixtures("OpenUrl")
class BaseClass:

    # explicit wait using link property
    def visibilitycheckbylink(self, linkname):
        wait = EW(self.testdriver, 20)
        wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, linkname)))

    # explicit wait using id property
    def visibilitycheckbyid(self, id):
        wait=EW(self.testdriver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, id)))

    # drop down utility
    def dropdownselector(self, dropdownlocator, name):
        dd = Select(dropdownlocator)
        dd.select_by_visible_text(name)


    #logger configuration
    def logconfig(self):
        # to get the test case name where we call this log method
        Testcasename = inspect.stack()[1][3]
        logger = logging.getLogger(Testcasename)

        #log format and file info
        # 2021-09-12 12:53:32,434 :INFO : test_homepage :Name received is
        logformat = logging.Formatter("%(asctime)s: %(levelname)s : %(name)s: %(message)s")
        logfile = logging.FileHandler('C:\DEV\PYTHON\PycharmProjects\Ecommerceframework\Reports\Testrunlogfile.log')
        logfile.setFormatter(logformat)

        #to avoid duplicate log infos
        if logger.hasHandlers():
            logger.handlers.clear()

        #integrating log file with the logger object
        logger.addHandler(logfile)

        #adding the level of logs we need in our file
        logger.setLevel(logging.INFO)
        return logger




import pytest
from selenium import webdriver
#from TestData.readexcel import readexcel

# Declaring it global to use it in screenshot function
Basedriver = None

# to read value from cmd
def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="chrome", help="browser option - chrome:firefox:IE"
    )

# Initialising driver, properties and URL
#@pytest.fixture(params = [readexcel.getdatafromexcel("tc1")])
@pytest.fixture()
def OpenUrl(request):
    global Basedriver #declaring it global to preserve the driver value assigned here for screenshot function

    browser = request.config.getoption("browsername") #getting browser detail

    if browser == "chrome": # assigning exe path
        Basedriver = webdriver.Chrome(executable_path="C:\\DEV\\chromedriver.exe")
    elif browser == "firefox":
        Basedriver = webdriver.Firefox(executable_path="C:\\DEV\\geckodriver.exe")

    Basedriver.get("http://automationpractice.com/index.php") #opening URL
    Basedriver.maximize_window()

    request.cls.testdriver = Basedriver #assigning the driver to the class driver which invoked this fixture

    #B aseemail = "aaaazdss s2dsss@mail.com"
    # request.cls.testemail = Baseemail
    yield #despite test case status, closing the browser
    Basedriver.close()

# @pytest.fixture(params = [readexcel.getdatafromexcel("tc1")])
# def getdata(request):
    #return request.param
#   request.cls.userdata = param

# code to embed ss in reports
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' : # or report.when == "setup":
        # xfail = hasattr(report, 'wasxfail')
        # if (report.skipped and xfail) or (report.failed and not xfail):
        file_name = report.nodeid.replace("::", "_") + ".png"
        _capture_screenshot(file_name)
        if file_name:
             html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
             extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    Basedriver.get_screenshot_as_file("C:\\DEV\\PYTHON\\PycharmProjects\\Ecommerceframework\\Reports\\" + name)



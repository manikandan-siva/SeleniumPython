import pytest
from selenium import webdriver

# to read value from cmd
def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="chrome", help="browser option - chrome:firefox:IE"
    )

@pytest.fixture()
def OpenUrl(request):
    print("webdriver initiation started")
    browser = request.config.getoption("browsername")
    if browser == "chrome":
        Basedriver = webdriver.Chrome(executable_path="C:\\DEV\\chromedriver.exe")
    elif browser == "firefox":
        Basedriver = webdriver.Firefox(executable_path="C:\\DEV\\geckodriver.exe")
    Basedriver.get("http://automationpractice.com/index.php")
    Basedriver.maximize_window()
    request.cls.testdriver = Basedriver
    print("webdriver initiation completed")
    Baseemail = "aaaaz2sss@mail.com"
    request.cls.testemail = Baseemail

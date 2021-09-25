import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\DEV\\chromedriver.exe")
driver.get("http://automationpractice.com/index.php")
# time.sleep(3)
wait =WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located(driver.find_element_by_class_name("login")))
driver.find_element_by_partial_link_text("Sign").click()
# time.sleep(3)
driver.find_element_by_id("email_create").send_keys("ssssa@gmail.com")
driver.find_element_by_id("SubmitCreate").click()
time.sleep(3)
driver.find_element_by_id("uniform-id_gender1").click()
# driver.find_element_by_xpath("//*[@class='radio-inline'][1]").click()
# driver.find_element_by_id("uniform-id_state").send_keys("a")
city = Select(driver.find_element_by_id("id_state"))
city.select_by_value("1")
# city.select_by_visible_text("California")

# This is a simple flow test (independent)
from selenium import webdriver
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path="C:/Users/PC/PycharmProjects/Selenium/Driver/chromedriver.exe")
driver.implicity_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
driver.find_element_by_id("welcome").click()
driver.find_element_by_id("Logout").click()
time.sleep(2)
driver.close()
driver.quit()
print("Test Completed")



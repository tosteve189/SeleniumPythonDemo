from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")

path = "..\Driver\geckodriver.exe"
driver = webdriver.Firefox(executable_path=path, firefox_options=firefox_options)

driver.get("https://google.com")
time.sleep(2)
print(driver.title)

driver.find_element_by_name("q").send_keys("Automation Step by Step")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

driver.close()
driver.quit()

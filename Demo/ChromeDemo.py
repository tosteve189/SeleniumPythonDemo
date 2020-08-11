from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_arguement("--headless")
chrome_options.add_arguement("--disable-extensions")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="..\Driver\chromedriver.exe")
driver.get("https://google.com")
print(driver.title)

driver.find_element_by_name("q").send_keys("Automation Step by Step")
driver.find_element_by_name("btnK").click()
time.sleep(2)
driver.close()
driver.quit()

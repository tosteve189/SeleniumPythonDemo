# This is a unit test (independent)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
import HtmlTestRunner

driver = webdriver.Chrome(ChromeDriverManager().install())


# Implicit waits
# driver.implicitly_wait(10)
# driver = webdriver.Chrome(executable_path="C:/Users/PC/PycharmProjects/Selenium/Driver/chromedriver.exe")

class LoginTests(unittest.TestCase):

    @classmethod
    def setupClass(cls):
        # cls.driver = webdriver.Chrome(executable_path="C:/Users/PC/PycharmProjects/Selenium/Driver/chromedriver.exe")
        driver.implicity_wait(10)

    def test_login_valid(self):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_id("welcome").click()
        driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        driver.close()
        driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/PC/PycharmProjects/Selenium/Report'),
                  verbosity=2)


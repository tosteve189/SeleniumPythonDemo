# This is an OOP unittest#
# Difference between LoginTest and LoginTest1 and LoginTest2
# Single flow test >>> LoginTest1 (independent)
# Unit test >>> LoginTest2 (independent)
# OOP Unit test >>> LoginTest (Dpendency) - And Logout has been using xpath

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
from POMDemo.Pages.LoginPage import LoginPage
from POMDemo.Pages.HomePage import HomePage
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
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        driver.close()
        driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/PC/PycharmProjects/Selenium/Report'),
                  verbosity=2)

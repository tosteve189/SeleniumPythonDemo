# This is an OOP unittest with Locator implementation (LCT)
# Difference between LoginTest and LoginTest1 and LoginTest2
# Single flow test >>> LoginTest1 (independent)
# Unit test >>> LoginTest2 (independent)
# OOP Unit test >>> LoginTest (Dependency) - And Logout has been using xpath
# OOP Unit test >>> LoginTestLCT (with corresponding LCT Dependency)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
from POMDemo.Pages.LoginPageLCT import LoginPageLCT
from POMDemo.Pages.HomePageLCT import HomePageLCT
import HtmlTestRunner

driver = webdriver.Chrome(ChromeDriverManager().install())


class LoginTestsLCT(unittest.TestCase):

    @classmethod
    def setupClass(cls):
        # cls.driver = webdriver.Chrome(executable_path="C:/Users/PC/PycharmProjects/Selenium/Driver/chromedriver.exe")
        driver.implicity_wait(10)

    def test_login_valid(self):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPageLCT(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePageLCT(driver)
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

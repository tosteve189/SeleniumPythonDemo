from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import HtmlTestRunner

driver = webdriver.Chrome(ChromeDriverManager().install())
# Implicit waits
driver.implicitly_wait(10)

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass executed")
        cls.driver = webdriver.Chrome(executable_path="..\Driver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def setUp(self):
        print("setUp executed before each method")

    def test_search_1(self):
        self.driver.get("http://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Automation Step by Step - Google Search")

    def test_search_2(self):
        self.driver.get("http://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Raghav Pal")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Raghav Pal - Google Search")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """This test should be skipped."""

    def tearDown(self):
        print("tearDown executed after each method")

    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.implicitly_wait(10)
        finally:
            print("Test Completed")
            cls.driver.close()
            cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/PC/PycharmProjects/Selenium/Report'), verbosity=2)

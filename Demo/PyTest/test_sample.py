# This is a simple pytest flow test (independent)
# pytest must be run from command line "pytest test_sample.py"
# To run all test cases with name convention ".py" under pytest directory, "python -m pytest"
# pytest must work with with localized driver (driver manager does not work)
# pytest has the fixture feature
# pytest - "test_*.py" or "*_test.py" is required as file name (have to be lower case, no capital letters)
# pytest - class name has to start with Test "class Test*()"

from selenium import webdriver
import pytest
import time

# driver = webdriver.Chrome(executable_path="C:/Users/PC/PycharmProjects/Selenium/Driver/chromedriver.exe")
# driver = webdriver.Chrome(ChromeDriverManager().install())


def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/PC/PycharmProjects/Selenium/Driver/chromedriver.exe")
    time.sleep(10)
    driver.maximize_window()


def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()


def test_title():
    x = driver.title
    assert x == "OrangeHRM"


def test_logout():
    driver.find_element_by_id("welcome").click()
    driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[9]/ul[1]/li[2]/a[1]").click()
    time.sleep(5)


def test_teardown():
    driver.close()
    driver.quit()
    print("Test Completed")

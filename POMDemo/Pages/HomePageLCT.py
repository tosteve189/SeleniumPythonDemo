from POMDemo.Locators.Locators import Locators


class HomePageLCT:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = Locators.welcome_link_id
        self.logout_xpath = Locators.logout_xpath

    def click_welcome(self):
        self.driver.find_element_by_id(Locators.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(Locators.logout_xpath).click()

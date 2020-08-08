class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        # self.logout_link_linkText = "Logout"
        self.logout_xpath = "/html[1]/body[1]/div[1]/div[1]/div[9]/ul[1]/li[2]/a[1]"

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        # self.driver.find_element_by_link_text(self.logout_link_linkText).click()
        self.driver.find_element_by_xpath(self.logout_xpath).click()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import locators

class TrainingPlaygroundPage:
    def __init__(self, driver=None):
        if driver == None:
            options = Options()
            options.headless = False
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        self.driver = driver

    def setup(self):
        self.driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/training-ground.html")

    def tier_down(self):
        self.driver.close()
        self.driver.quit()

    # def get_input_1(self):
    #     return self.driver.find_element_by_xpath(locators.input_1_xpath)
    #
    # def type_into_input_1(self, text):
    #     self.get_input_1().send_keys(text)

    def get_input(self, input_id):
        return self.driver.find_element_by_xpath(locators.inputs[input_id])

    def type_into_input(self, input_id, text):
        self.get_input(input_id).send_keys(text)

    def __del__(self):
        self.driver.close()
        self.driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import locators
options = Options()
options.headless = False

driver = None

def setup():
    global driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/training-ground.html")

def tier_down():
    driver.close()
    driver.quit()

def get_input_1():
    return driver.find_elements_by_xpath(locators.input_1_xpath)

def type_into_input_1(text):
    get_input_1().send_keys(text)

# finally:

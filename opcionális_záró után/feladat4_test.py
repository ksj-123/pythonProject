from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)
URL = "https://wonderful-pond-0d96a8503.azurestaticapps.net/f4.html"

driver.get(URL)
time.sleep(2)


def find_loc(id):
    return driver.find_element_by_id(id)


submit_button = driver.find_element_by_xpath('/html/body/div[1]/form/input[3]')

test_data_1 = ["teszt@elek.hu", "Kiscica1234"]
test_data_2 = ["teszt@elek.hu", "a1"]


# TC1-helyes kitöltés
def test_tc1():
    find_loc("usrname").send_keys(test_data_1[0])
    find_loc("psw").send_keys(test_data_1[1])
    submit_button.click()
    time.sleep(2)
    assert find_loc("titleText").text == "404: Not Found"


# TC2-helytelen kitöltés
def test_tc2():
    driver.get(URL)
    find_loc("usrname").send_keys(test_data_2[0])
    find_loc("psw").send_keys(test_data_2[1])

    assert find_loc("message").is_displayed()
    assert find_loc("number").get_attribute("class") and find_loc("letter").get_attribute("class") == "valid"
    assert find_loc("capital").get_attribute("class") and find_loc("length").get_attribute("class") == "invalid"

    driver.quit()

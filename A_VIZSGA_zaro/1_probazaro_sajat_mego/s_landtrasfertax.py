import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.set_window_size(1000, 500, 500)

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html')


# TC01: üres kitöltés helyessége
def empty():
    goBtn = driver.find_element_by_xpath('/html/body/main/div/div/p[1]/button')
    goBtn.click()


empty()

assert driver.find_element_by_xpath(
    '//*[@id="disclaimer"]/strong').text == 'Enter the property value before clicking Go button.'


# TC02: helyes kitöltés helyes kitöltése
def transfer():
    price = driver.find_element_by_id('price')
    price.send_keys(33333)
    goBtn = driver.find_element_by_xpath('/html/body/main/div/div/p[1]/button')
    goBtn.click()


transfer()

try:
    assert driver.find_element_by_id('tax').text == '166.665'

finally:
    driver.close()

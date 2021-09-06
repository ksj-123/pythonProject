from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select

options = Options()
options.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html')
    time.sleep(2)

# TC01: üres kitöltés helyessége

    est_of_prop_field = driver.find_element_by_id('price')
    price = est_of_prop_field.get_attribute('value')
    assert price == ''

    tax_field = driver.find_element_by_id('tax')
    tax_dollar = tax_field.get_attribute('value')
    button_go = driver.find_element_by_xpath('/html/body/main/div/div/p[1]/button')
    button_go.click()

    time.sleep(1)
    warning_message = driver.find_element_by_id('disclaimer').text
    print(warning_message)

    assert warning_message == 'Enter the property value before clicking Go button.'
    assert tax_dollar == ''

# TC02: helyes kitöltés helyes kitöltése

    est_of_prop_field.send_keys('3333')

    button_go.click()
    tax_field = driver.find_element_by_id('tax')
    tax_dollar = tax_field.get_attribute('value')
    #print(tax_field)
    assert tax_dollar == '16.665'

finally:
    driver.close()
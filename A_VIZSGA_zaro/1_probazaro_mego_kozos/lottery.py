from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html"

driver.get(URL)


def get_all_numbers():
    return driver.find_elements_by_class_name("balls")

draw_number = driver.find_element_by_id("draw-number")
reset_numbers = driver.find_element_by_id("reset-numbers")
#TC01 ures
lotto_nubers = get_all_numbers()

assert len(lotto_nubers) == 0

# TC02 6 szam huzas eredmenye

for _ in range(6):
    draw_number.click()
    time.sleep(1)

lotto_nubers = get_all_numbers()

assert len(lotto_nubers) == 6

for number in lotto_nubers:
    assert int(number.text) in range(1, 60)

# TC03
draw_number.click()
lotto_nubers = get_all_numbers()
assert len(lotto_nubers) == 6
reset_numbers.click()
lotto_nubers = get_all_numbers()
assert len(lotto_nubers) == 0
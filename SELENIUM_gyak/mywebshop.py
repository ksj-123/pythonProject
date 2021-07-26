from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("https://react-card-2a6c5.web.app/")
time.sleep(2)

# buttons = driver.find_elements_by_xpath('//*[@class="shelf-item__buy-btn"]')
buttons = driver.find_elements_by_class_name("shelf-item__buy-btn")

for button in buttons:
    button.click()
    driver.find_element_by_class_name("float-cart__close-btn").click()
    time.sleep(0.35)

driver.find_element_by_class_name("bag").click()
time.sleep(0.5)
result_text = driver.find_element_by_class_name("sub-price__val").text
assert result_text == "$ 440.00"
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

import time


def test_webshop():
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


# Adott ez a React Cart alkalmazás.
#
# Tedd be a kosárba az összes terméket és ellenőrizd, hogy a végösszeg "$ 440.00" lett-e. (vigyázat, trükkös)
#
# https://react-card-2a6c5.web.app/


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
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

except Exception as e:
    print('Exception: ', e)
finally:
    driver.close()

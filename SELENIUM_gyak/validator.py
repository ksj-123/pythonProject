# validátor - űrlapkitöltő

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/another_form.html")

    # várakozás
    msg = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='fullname' and @name='fullname]"))).get_attribute("validationMessage")

    # ellenőrizzük, hogy van message
    assert msg is not None
    assert msg == 'Please fill out this field.'

    time.sleep(2)


finally:
    # pass
    driver.close()

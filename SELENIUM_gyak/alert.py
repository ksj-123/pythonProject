# felugró párbeszédpanel

import time

from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/kitchensink.html")
    name = driver.find_element_by_id("name")
    name.send_keys("Juc")
    button = driver.find_element_by_id("alertbtn")
    button.click()
    ref_text = "Hello Juc, share this practice page and share your knowledge"
    alert = driver.switch_to.alert    # de még rá kell kapcsolódni
    assert(alert.text == ref_text)  # összehasonlítjuk a szövegeket
    print(alert.text)
    time.sleep(2)
    alert.accept()          # mintha megnyomnánk a gombot 2 mp múlva eltűnik a felugró ablak
    time.sleep(1)

finally:
    # pass
    driver.close()

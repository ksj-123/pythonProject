# felugró ablak (másik weboldal másik ablakban) és felugró tab (másik weboldal új fülön)

import time

from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/kitchensink.html")
    driver.find_element_by_id("openwindow").click()
    time.sleep(1)

    main_window = driver.window_handles[0]
    other_window = driver.switch_to.window('myWin')        # átállítjuk a másik ablakra

    assert(driver.title == "met.hu - Országos Meteorológiai Szolgálat")      # a vizsgált ablak címe megegyezik e
    print(driver.title)
    time.sleep(5)
    driver.close()
    driver.switch_to.window(main_window)
    driver.close()
finally:
    pass
     # driver.quit()      # minden ablakot a származtatottakat is bezár


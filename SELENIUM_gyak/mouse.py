# Egér műveletek kezelése

import time

from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/kitchensink.html")

    from selenium.webdriver.common.action_chains import ActionChains

    mousehover = driver.find_element_by_id("mousehover")
    top_submenu = driver.find_element_by_xpath("//div[@class='mouse-hover-content']/a[1]")

    # actions.move_to_element(mousehover) -ből
    ActionChains(driver).move_to_element(mousehover).perform()
    time.sleep(3)

    actions = ActionChains(driver)
    actions.click(top_submenu)
    actions.perform()

finally:
    pass
    # driver.close()

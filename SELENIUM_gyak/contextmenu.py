# context menü tesztelése

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/contextmenu.html")
    ActionChains(driver).context_click().perform()
    driver.find_element_by_xpath("//div[@data-rc-launch='first']").click()
    time.sleep(2)
    alert = driver.switch_to.alert()
    assert (alert.text == "first")
    time.sleep(2)
    alert.accept()

finally:
    pass
    # driver.close()

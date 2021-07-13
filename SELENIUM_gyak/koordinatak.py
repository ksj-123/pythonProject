# koordináták kezelése

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/dragdrop3.html")
    draggableElement = driver.find_element_by_id("dragThis")
    ActionChains(driver).drag_and_drop_by_offset(draggableElement,
                                                 draggableElement.location["x"] + 350,
                                                 draggableElement.location["y"] + 100).perform()
    time.sleep(5)

finally:
    pass
    # driver.close()
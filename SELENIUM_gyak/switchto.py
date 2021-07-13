from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

# In order for ChromeDriverManager to work you must pip install it in your own environment.
# driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome()
try:
    driver.get("http://gentle-bay-0e4e13803.azurestaticapps.net/embeds.html")
    # elmentjuk az eredeti ablak azonosítóját
    general_frame = driver.find_element_by_id("general-frame")
    forms_frame = driver.find_element_by_id("forms-frame")
    print(driver.window_handles)

    default_window = driver.window_handles[0]
    driver.switch_to.frame(general_frame)
    h4text = driver.find_element_by_tag_name("h4").text
    driver.switch_to.parent_frame()
    driver.switch_to.frame(forms_frame)
    driver.find_element_by_id("example-input-text").send_keys(h4text)

    # vissza az eredeti ablakba / driver contextushoz
    driver.switch_to.window(default_window)
finally:
    pass
    # driver.close()
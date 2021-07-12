from selenium import webdriver

driver = webdriver.Chrome()


try:
    driver.get("http://localhost:9999/kitchensink.html")

    input_text = driver.find_element_by_id("displayed-text")
    hidebutton = driver.find_element_by_id("hide-textbox")
    showbutton = driver.find_element_by_id("show-textbox")
    print(input_text.is_displayed())
    hidebutton.click()
    print(input_text.is_displayed())
    input_text.is_selected()
finally:
    driver.close()
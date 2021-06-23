from selenium import webdriver

driver = webdriver.Chrome()
try:
    driver.get("https://localhost:9999/trickybuttons.html")

    button2 = driver.find_element_by_xpath('//button[text() = "button2"]')
    button2.click()

    result = driver.find_element_by_xpath('//label[@id="result"]')
    print(result.text)

    assert (result.text == "button2 was clicked")
finally:
    driver.close()

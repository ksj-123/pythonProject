from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()

try:
    driver.get("https://proud-cliff-00bebe803.azurestaticapps.net/masodik.html")

    number_input = driver.find_element_by_id("number")
    unit_input = driver.find_element_by_id("unit")

    # scenario TC_001 : '112' 'meter' == `367.45406824146977 FOOT`
    number_input.send_keys("112")
    unit_input.send_keys("meter")
    strong_text = driver.find_element_by_xpath('/html/body/main/div/p').text
    assert strong_text == "367.45406824146977 FOOT"

    # need to clear input fields before typing new data
    number_input.clear()
    unit_input.clear()

    # scenario TC_002 : '8' 'oz' == `236.56 MILLILITER`
    number_input.send_keys("8")
    unit_input.send_keys("oz")
    strong_text = driver.find_element_by_xpath('/html/body/main/div/p').text
    assert strong_text == "236.56 MILLILITER"

    # need to clear input fields before typing new data
    number_input.clear()
    unit_input.clear()

    # scenario TC_003 : '1' 'gallon' == `3.785 LITER`
    number_input.send_keys("1")
    unit_input.send_keys("gallon")
    strong_text = driver.find_element_by_xpath('/html/body/main/div/p').text
    assert strong_text == "3.785 LITER"

finally:
    driver.close()

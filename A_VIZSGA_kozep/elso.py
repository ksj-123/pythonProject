from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()

try:
    driver.get("https://proud-cliff-00bebe803.azurestaticapps.net/elso.html")

    age_input = driver.find_element_by_id("age")
    submit_button = driver.find_element_by_id("submit")

    # scenario 1 age = 39; secons = 1227376800
    age_input.send_keys("39")
    submit_button.click()
    comment_text = driver.find_element_by_id("seconds").text
    assert comment_text == "1227376800"

    # need to clear input fields before typing new data
    age_input.clear()

    # scenario 2 age = "empty" ; secons = 0
    age_input.send_keys()
    submit_button.click()
    comment_text = driver.find_element_by_id("seconds").text
    assert comment_text == 0

    # scenario 3 age = -122 ; secons = -3524774400
    age_input.send_keys("-122")
    submit_button.click()
    comment_text = driver.find_element_by_id("seconds").text
    assert comment_text == "-3524774400"

finally:
    driver.close()
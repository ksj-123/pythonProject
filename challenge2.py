from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://brave-desert-0a706e303.azurestaticapps.net/")

q = driver.find_element_by_id("user-message")
q.send_keys("input")

q.click()

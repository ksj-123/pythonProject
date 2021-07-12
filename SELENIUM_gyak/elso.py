from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://python.org")

q = driver.find_element_by_name("q")
q.send_keys("input")

submit = driver.find_element_by_name("submit")
submit.click()

driver.close()

driver.find_by_id
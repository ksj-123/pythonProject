from selenium import webdriver

def navigate_to_general_page():
    link = driver.find_element_by_xpath('//a[text()=General text and other elements"]')
    link.click()


driver = webdriver.Chrome()
try:
    driver.get("http://localhost:9999/")
    navigate_to_general_page()
    time.sleep(1.0)
    driver.back()
    time.sleep(1.0)
    navigate_to_general_page()

    anchors = driver.find_elements_by_xpath('//header//small//a')

    for a in anchors:
        a.click()
        time.sleep(1.0)

finally:
    driver.close()

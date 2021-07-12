from selenium import webdriver

def navigate_to_general_page():
    link = driver.find_element_by_xpath('//a[text()="General text and other elements"]')
    link.click()


driver = webdriver.Chrome()
try:
    driver.get("http://localhost:9999/")
    print(driver.current_url)
    navigate_to_general_page()
    print(driver.current_url)
    driver.back()
    print(driver.current_url)
    navigate_to_general_page()

    anchors = driver.find_elements_by_xpath('//header//small//a')

    for a in anchors:
        a.click()
        print(driver.current_url)
    print("*" * 50)
    while driver.current_url != "http://localhost:9999/":
        print(driver.current_url)
        driver.back()

finally:
    driver.close()
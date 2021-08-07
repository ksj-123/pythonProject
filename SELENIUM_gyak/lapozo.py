# lapozó kezelőfelület tesztelése

from selenium import webdriver
import pprint
import time

driver = webdriver.Chrome()
extracted_date = []

try:
    driver.get("http://localhost:9999/pagination.html")
    while True:
        time.sleep(2)
        table = driver.find_element_by_xpath("//table[@id='contacts-table']/tbody")
        rows = table.find_elements_by_tag_name("tr")
        c
    pprint.pprint(extracted_date)
    print(len(extracted_date))
finally:
    pass
    # driver.close()

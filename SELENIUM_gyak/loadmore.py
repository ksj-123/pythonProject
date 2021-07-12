# töltsön még be több képet - Load More funckió tesztelése

from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/loadmore.html")
    load_more = driver.find_element_by_xpath("/html/body/div[2]/button")
    for i in range(5):
        time.sleep(3)
        images = driver.find_elements_by_xpath("//div[@class='image']")
        # az utolsó 5 elem lekérdekézése
        for j in images[-5:]:
            print(j.find_element_by_tag_name("img").get_attribute("src"))
            print(j.find_element_by_tag_name("p").text)
        load_more.click()
finally:
    driver.close()

# scroll bar és scroll to használata, tesztelése

from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/general.html")

    ## html tag használata
    # from selenium.webdriver.common.keys import Keys
    #
    # html = driver.find_element_by_tag_name("html")
    # html.send_keys(Keys.END)

    ## JavaScript végrehajtás
    js = "window.scrollTo(0, document.body.scrollHeight);"
    driver.execute_script(js)

finally:
    pass
    # driver.close()


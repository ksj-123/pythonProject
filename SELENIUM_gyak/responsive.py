# átméretezés tesztelése, responzive design
import time

from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/responsive-table.html")
    # méretezés
    driver.set_window_size(800, 1080)
    size = driver.get_window_size()
    # irassuk ki, a tényleges méreteket
    print("Window size: width = {}px, height = {}px.".format(size["width"], size["height"]))
    time.sleep(2)
    # átméretezés
    driver.set_window_size(240, 1080)
    size = driver.get_window_size()
    print("Window size: width = {}px, height = {}px.".format(size["width"], size["height"]))
    time.sleep(2)

finally:
    pass
    # driver.close()

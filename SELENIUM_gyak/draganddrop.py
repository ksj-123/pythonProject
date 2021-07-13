# drag and drop tesztelése (fogd és vidd)
from selenium import webdriver
import time
from os import getcwd

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://localhost:9999/dragndrop1.html")

time.sleep(2)

cwd = getcwd()
JS_DRAG_DROP = open(cwd + '\\drag-drop.js', 'r').read()
print(JS_DRAG_DROP)
# drag and drop an element on another one
source = driver.find_element_by_id("drag1")
target = driver.find_element_by_id("div2")

driver.execute_script(JS_DRAG_DROP, source, target)

driver.implicitly_wait(5)

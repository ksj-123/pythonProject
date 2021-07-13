# fájlfeltöltés

from selenium import webdriver
from os import getcwd
import time

driver = webdriver.Chrome()

def drag_and_drop_file(drop_target, path):
    driver = drop_target.parent
    file_input = driver.execute_script(JS_DRAG_DROP, drop_target, 0, 0)
    file_input.sent_keys(path)

driver.get("http://localhost:9999/filedragndropupload.html")

filedrag = driver.find_element_by_id('filedrag')
cwd = getcwd()
JS_DRAG_DROP = open(cwd + '\\filedrag.js', 'r').read()
print(JS_DRAG_DROP)
time.sleep(2)
drag_and_drop_file(filedrag, path="C:\Users\User\PycharmProjects\pythonProject\SELENIUM_gyak\data.csv")
time.sleep(5)
# driver.close()

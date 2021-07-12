from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.rpachallenge.com/")

import csv

with open("challenge.csv") as file:
    reader = csv.reader(file)
    next(reader)
for data in reader:
    print(data)

    lines = file.readlines()
    for line in lines[1:]:
        print(line.replace("\n", "").split(';'))

q = driver.find_element_by_("q")
q.send_keys("input")

submit = driver.find_element_by_name("submit")
submit.click()

driver.close()

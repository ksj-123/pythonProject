import csv
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:9999/filltablewithsum.html")

#-------

with open('data1.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        print(row)
        product = driver.find_element_by_id("product")
        product.clear()
        product.send_keys(row[0])
        quantity = driver.find_element_by_id("quantity")
        quantity.clear()
        quantity.send_keys(row[1])
        price = driver.find_element_by_id("price")
        price.clear()
        price.send_keys(row[2])
        driver.find_element_by_id('add').click()


#-------

def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element

add_button = driver.find_element_by_id('add')

with open('data1.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        print(row)
        find_and_clear_by_id("product").send_keys(row[0])
        find_and_clear_by_id("quantity").send_keys(row[1])
        find_and_clear_by_id("price").send_keys(row[2])
        add_button.click()

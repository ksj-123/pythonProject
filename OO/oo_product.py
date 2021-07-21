import csv
import time
# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
driver = webdriver.Chrome()
import pprint
# In order for ChromeDriverManager to work you must pip install it in your own environment.
# driver = webdriver.Chrome(ChromeDriverManager().install())

def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element

class Product:
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
    def __repr__(self):
        return f"Product({self.product_name, self.quantity, self.price})"

def load_products_from_csv():
    product_list = []
    with open('data.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # skip header
        for row in csvreader:
            product_list.append(Product(row[0], row[1], row[2]))
    return product_list
try:
    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/filltablewithsum.html")
    products = load_products_from_csv()
    pprint.pprint(products)
    for product in products:
        find_and_clear_by_id("product").send_keys(product.product_name)
        find_and_clear_by_id("quantity").send_keys(product.quantity)
        find_and_clear_by_id("price").send_keys(product.price)
        driver.find_element_by_id("add").click()
finally:
    driver.close()
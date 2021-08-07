from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html"

driver.get(URL)

sales_tax_expected_values = ["", "0.00"]
gtotal_expected_values = ["", "9.90"]

# TC01: ures

select = Select(driver.find_element_by_id("Proditem"))
select.select_by_visible_text('')

driver.find_element_by_id("subtotalBtn").click()

assert sales_tax_expected_values[0] == driver.find_element_by_id("salestax").text

# TC02: kitoltve

select = Select(driver.find_element_by_id("Proditem"))
select.select_by_visible_text('6" x 6" Volkanik Ice')
driver.find_element_by_id("quantity").send_keys("1")

driver.find_element_by_id("subtotalBtn").click()
driver.find_element_by_id("gtotalBtn").click()
assert sales_tax_expected_values[1] == driver.find_element_by_id("salestax").get_attribute("value")
assert gtotal_expected_values[1] == driver.find_element_by_id("gtotal").get_attribute("value")

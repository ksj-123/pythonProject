from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html"

driver.get(URL)

# elemek kutatasa
price_element = driver.find_element_by_id("price")
go_button = driver.find_element_by_tag_name("button")
tax_element = driver.find_element_by_id("tax")

# TC01 ures
assert "" == price_element.get_attribute("value")
go_button.click()
error_element = driver.find_element_by_xpath('//*[@id="disclaimer"]/strong')
assert "" == tax_element.get_attribute("value")
assert "Enter the property value before clicking Go button." == error_element.text

tax_test_data = ["33333", "3333"]

# TC02 teszadatos
price_element.send_keys(tax_test_data[0])
go_button.click()
assert "16.665" == tax_element.get_attribute("value")

# TC03 teszadatos
price_element.send_keys(tax_test_data[1])
go_button.click()
assert "16.665" == tax_element.get_attribute("value")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://happy-sea-0a5ffef03.azurestaticapps.net/elso.html")

.....



except Exception as e:
    print('Exception occured: ', e)
finally:
    driver.close()
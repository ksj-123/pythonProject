from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html"

driver.get(URL)

passenger_test_value = "Tamas Jozsa"
date_test_value = "12251999"
date_test_value_out = "1999-12-25"
time_test_value = "1235a"
time_test_value_out = "12:35AM"

passenger = driver.find_element_by_id("passenger")
passenger.send_keys(passenger_test_value)
date = driver.find_element_by_id("departure-date")
date.send_keys(date_test_value)
departure_time = driver.find_element_by_id("departure-time")
departure_time.send_keys(time_test_value)

driver.find_element_by_id("issue-ticket").click()

passenger_name = driver.find_element_by_id("passenger-name")
departure_date_text = driver.find_element_by_id("departure-date-text")
departure_time_text = driver.find_element_by_id("departure-time-text")
side_departure_date = driver.find_element_by_id("side-detparture-date")
side_departure_time = driver.find_element_by_id("side-departure-time")

assert passenger_test_value.upper() == passenger_name.text
assert date_test_value_out == departure_date_text.text
assert time_test_value_out == departure_time_text.text

assert date_test_value_out == side_departure_date.text
assert time_test_value_out == side_departure_time.text
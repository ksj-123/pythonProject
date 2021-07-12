from datetime import datetime, date, time, timezone
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost:9999/forms.html")

nowutc = datetime.now(timezone.utc)
print(nowutc)
# hh/nn/eeee
driver.find_element_by_id("example-input-date").send_keys(nowutc.strftime("%m/%d/%Y"))

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html"

driver.get(URL)

# TC01 user
assert not driver.find_element_by_xpath('//*[@id="buttons"]/input').is_enabled()

# TC02 adatokkal
#
# test@bela.hu
# 2 hours and 0 minutes
# working hard
# types of work: Time working on visual effects for movie

email = "test@bela.hu"
hours = "2"
minutes = "0"
driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[1]').send_keys(email)
driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[2]').send_keys(hours)
driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[3]').send_keys(minutes)
driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/textarea').send_keys("working hard")

select = Select(driver.find_element_by_id("dropDown"))
select.select_by_visible_text("Time working on visual effects for movie")

submit = driver.find_element_by_xpath('//*[@id="buttons"]/input')

assert submit.is_enabled()

submit.click()
time.sleep(3)

assert email == driver.find_element_by_xpath('//*[@id="section-thankyou"]/div/p[1]/span').text
assert hours == driver.find_element_by_xpath('//*[@id="section-thankyou"]/div/p[2]/span[1]').text
assert minutes == driver.find_element_by_xpath('//*[@id="section-thankyou"]/div/p[2]/span[2]').text

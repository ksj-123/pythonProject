from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html")


def find_and_clear(id):
    find = driver.find_element_by_id(id)
    find.clear()
    return find


def issue_ticket():
    passenger = find_and_clear("passenger")
    passenger.send_keys("Proba Pista")
    depdate = find_and_clear("departure-date")
    date_to_set = datetime(2022, 12, 20)
    depdate.send_keys(date_to_set.strftime('%Y'))
    depdate.send_keys(date_to_set.strftime('%m'))
    depdate.send_keys(date_to_set.strftime('%d'))
    deptime = find_and_clear("departure-time")
    date_to_set = datetime(2022, 12, 20, 16, 10)
    deptime.send_keys(date_to_set.strftime('%I:%M'))
    deptime.send_keys(date_to_set.strftime('%p'))


issue_ticket()

issue = driver.find_element_by_id("issue-ticket")
issue.click()

try:
    assert driver.find_element_by_id("passenger-name").text == "Proba Pista"


finally:
    driver.close()

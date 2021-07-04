import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "http://www.rpachallenge.com/"

driver.get(URL)

start_button = driver.find_element_by_xpath('//button[text()="Start"]')

start_button.click()


def get_element_by_xpath(xpath_text):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//label[text()="{xpath_text}"]/../input'))
    )


def get_element_by_css(css_text):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f'input[value="{css_text}"]'))
    )


with open('challenge.csv', 'r') as csvfile:
    table_reader = csv.reader(csvfile)
    next(table_reader)

    for row in table_reader:
        first_name = get_element_by_xpath("First Name")
        last_name = get_element_by_xpath("Last Name")
        role = get_element_by_xpath("Role in Company")
        address = get_element_by_xpath("Address")
        company = get_element_by_xpath("Company Name")
        email_address = get_element_by_xpath("Email")
        phone_number = get_element_by_xpath("Phone Number")
        submit_button = get_element_by_css("Submit")
        first_name.send_keys(row[0])
        last_name.send_keys(row[1])
        company.send_keys(row[2])
        role.send_keys(row[3])
        address.send_keys(row[4])
        email_address.send_keys(row[5])
        phone_number.send_keys(row[6])
        submit_button.click()

result = driver.find_element_by_xpath('/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[1]')

assert result == "Congratulations!"

driver.close()

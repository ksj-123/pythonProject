# TC001 - User Registration - random generátorral
import time
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://react-layr-realworld-example-app.layrjs.com/all")

    def register(username, email, password):
        driver.get("http://localhost:1667/#/")
        driver.find_element_by_xpath('//*[@id="root"]/div/nav/div/ul/li[3]/a').click()
        username = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/form/fieldset/fieldset[1]/input').send_keys("user000" + string((random().int(3)) + 1))
        email = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/form/fieldset/fieldset[2]/input').send_keys("user000" + string((random().int(3)) + 1)) + "example.com")
        password = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/form/fieldset/fieldset[3]/input').ssend_keys("User000" + string((random().int(3)) + 1))
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/form/fieldset/button').click()

    # leellenőrizni, hogy a regisztrált username megjelenik a jobb felső sarokban
    # assert

finally:
    driver.close()

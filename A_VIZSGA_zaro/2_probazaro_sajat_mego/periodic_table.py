# Periodic table test
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import csv

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 500, 500)


def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


try:
    # Oldal betöltése
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html/")
    time.sleep(2)


    # periodic table
    # def table():
    #     find('//*[@id="app"]/nav/div/ul/li[3]/a').click()
    #     with open('../data.txt', 'r') as csvfile:
    #         csvreader = csv.reader(csvfile, delimiter=',')
    #         next(csvreader)
    #         for row in csvreader:
    #             print(row)
    #             find('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(row[0])
    #             find('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys(row[1])
    #             find('//*[@id="app"]/div/div/div/div/form/fieldset[3]/input').send_keys(row[2])
    #     sign_up = find('//form/button')
    #     sign_up.click()
    #
    # table()
    # ki kell egészíteni még for ciklussal

finally:
    driver.close()
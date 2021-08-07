# Guess the number test
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 600, 600)

# buttons
number = '//*[@id="step1"]/ul/li[1]/select'
next1_btn = '//*[@id="step1"]/ul/li[2]/button'
date = '//*[@id="step2"]/ul/li[1]/input'
time_of_day = '//*[@id="step2"]/ul/li[2]/select'
hours = '//*[@id="step2"]/ul/li[3]/select'
next2_btn = '//*[@id="step2"]/ul/li[4]/button'
name = '//*[@id="step3"]/ul/li[1]/input'
email = '//*[@id="step3"]/ul/li[2]/input'
message = '//*[@id="step3"]/ul/li[3]/textarea'
submit = '//*[@id="step3"]/ul/li[4]/button'
successfully = '//*[@id="booking-form"]/h2'


def findx(xpath):
    findx = driver.find_element_by_xpath(xpath)
    return findx


try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html')
    time.sleep(3)


    # test helyes adatokkal
    def kitoltes():
        findx(number).click()
        findx(number).send_keys('2')
        findx(next1_btn).click()
        findx(date).send_keys('2021.08.20.')
        findx(time_of_day).click()
        findx(time_of_day).send_keys('Morning')
        findx(hours).click()
        findx(hours).send_keys('3')
        findx(next2_btn).click()
        findx(name).send_keys('Proba Pista')
        findx(email).send_keys('proba@email.com')
        findx(message).send_keys('message proba')
        findx(submit).click()


    kitoltes()

    # assert findx(
    #     successfully).text == "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."
    # print(findx(successfully).text)

    # test rossz email címmel
    def email_h():
        findx(number).click()
        findx(number).send_keys('2')
        findx(next1_btn).click()
        findx(date).send_keys('2021.08.20.')
        findx(time_of_day).click()
        findx(time_of_day).send_keys('Morning')
        findx(hours).click()
        findx(hours).send_keys('3')
        findx(next2_btn).click()
        findx(name).send_keys('Proba Pista')
        findx(email).send_keys('proba@')
        findx(message).send_keys('message proba')
        findx(submit).click()


    email_h()

    # assert findx(
    #     successfully).text == "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."
    # print(findx(successfully).text)

finally:
    driver.close()

# Guess the number test
import random

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import pprint

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 600, 600)

# xpath
higher_btn = '/html/body/div[1]/div[2]/input'
lower_btn = '/html/body/div[1]/div[2]/input'

# <p ng-show="deviation < 0" class="alert alert-warning ng-hide">Guess lower.</p>
# <p ng-show="deviation > 0" class="alert alert-warning ng-hide">Guess higher.</p>
# <p ng-show="deviation === 0" class="alert alert-success">Yes! That is it.</p>

number_of_guesses = '/html/body/div[1]/div[3]/p/span'


def find(id):
    find = driver.find_element_by_id(id)
    return find


def findx(xpath):
    findx = driver.find_element_by_xpath(xpath)
    return findx


def number():
    number = findx('/html/body/div[1]/div[2]/input').send_keys(random.randint(0, 100))
    return number


try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html')
    time.sleep(3)


    # Helyes számokkal
    # number()
    # print(number)
    # g_btn = findx('/html/body/div[1]/div[2]/span/button')
    # g_btn.click()
    # for row in rows:
    #
    #
    #
    #     findx(higher_btn)
    #     findx(lower_btn)
    #     g_btn = findx('/html/body/div[1]/div[2]/span/button')
    #     g_btn.click()
    #
    # next_button = driver.find_element_by_id("next")
    # if next_button.is_enabled():
    #     break
    # else:
    #     next_button.click()
    #
    # if guess():
    #     print(number)
    #     g_btn = findx('/html/body/div[1]/div[2]/span/button')
    #     g_btn.click()
    # else

    # Proba helytelen számokkal (-19, 255)

    def proba():
        findx('/html/body/div[1]/div[2]/input').send_keys(-19)
        g_btn = findx('/html/body/div[1]/div[2]/span/button')
        g_btn.click()
        assert findx('/html/body/div[1]/p[4]').text == "Guess higher."
        findx('/html/body/div[1]/div[2]/input').send_keys(255)
        g_btn = findx('/html/body/div[1]/div[2]/span/button')
        g_btn.click()
        assert findx('/html/body/div[1]/p[5]').text == "Guess lower."


    proba()

finally:
    driver.close()

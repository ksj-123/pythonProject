import csv

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/imdb_guessmovie.html"

driver.get(URL)


# Helyes jelenik meg az applikáció:
#
# minden strike gomb zöld
# egy gomb sincs lenyomva
# 144,238,144,1 lightgreen

def test_initial_state():
    strike_divs = driver.find_elements_by_xpath('//*[contains(@id,"strike")]')[1:]
    for strike in strike_divs:
        assert 'rgba(144, 238, 144, 1)' == strike.value_of_css_property('background-color')
    keys_on = driver.find_elements_by_xpath('//button[contains(@class, "keyOn")]')
    assert len(keys_on) == 0


# Helyesen működik us filem-re az applikáció
# Tallágassunk és végig ellenőrizzük, hogy a megfelelő karakterek jelennek-e
# Ha kitaláljuk 4 találgatásból, akkor jó üzenet jelenik-e meg.
# Helytelenül találgatunk akkor működik-e az applikáció:

def click_button(bid):
    driver.find_element_by_id(bid).click()


def guess_buttons(button_str):
    for char in button_str:
        click_button(char)


def test_app_works_guessed_correct():
    driver.find_element_by_xpath('//input[@value="us"]').click()
    time.sleep(1)
    guess_buttons("MENTO")
    time.sleep(1)
    ex_confirm_text = "Well Done!"
    confirm_next_element = driver.find_element_by_id("confirmNext")
    assert ex_confirm_text in confirm_next_element.text


# Tallágassunk és végig ellenőrizzük, hogy a megfelelő karakterek jelennek-e
# Most ne találjuk el 4 találgatásból, akkor jó üzenet jelenik-e meg.

def test_app_works_guessed_wrong():
    driver.find_element_by_xpath('//input[@value="us"]').click()
    time.sleep(1)
    guess_buttons("1234")
    time.sleep(1)
    ex_confirm_text = "Well Done!"
    confirm_next_element = driver.find_element_by_id("confirmNext")
    assert ex_confirm_text not in confirm_next_element.text


test_initial_state()
test_app_works_guessed_correct()
driver.refresh()
test_app_works_guessed_wrong()
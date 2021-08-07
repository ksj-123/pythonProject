import csv

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html"

driver.get(URL)
character_elements = driver.find_elements_by_xpath('//ul[@class="characters"]/li')

with open("characters.txt", "w") as chfile:
    for character in character_elements:
        chfile.write(character.get_attribute("id"))
        chfile.write(",")
        chfile.write(character.get_attribute("data-teams").replace(" ", ","))
        chfile.write("\n")

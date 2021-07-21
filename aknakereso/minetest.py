from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from mines import mines_funsolver
from webdriver_manager.chrome import ChromeDriverManager
import random
# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://gentle-bay-0e4e13803.azurestaticapps.net/minesweeper-game.html"
driver.get(URL)

minefield_elements = driver.find_elements_by_xpath('//div[@id="minefield"]//div')


def minefield_element_to_type(element):
    elementclass = element.get_attribute("class")
    if elementclass == "covered":
        return "-"
    elif elementclass == "flag":
        return "m"
    elif elementclass == "question":
        return "m"
    elif elementclass == "mine-hit":
        return "m"
    elif elementclass == "mine":
        return "m"
    else:
        return elementclass[-1]


def print_minefield():
    i = 0
    for minefield_element in minefield_elements:
        print(minefield_element_to_type(minefield_element), end='')
        if i == 8:
            print()
            i = 0
            continue
        i += 1


def calc_minefiled():
    m = []
    for minefield_element in minefield_elements:
        m.append(minefield_element_to_type(minefield_element))
    return "".join(m)


def is_dead():
    return True if driver.find_element_by_id("minesweeper-reset-button").get_attribute("class") == "face-sad" else False


def seq_player():
    while True:
        if is_dead():
            break
        for minefield_element in minefield_elements:
            if is_dead():
                break
            if minefield_element_to_type(minefield_element) == "-":
                minefield_element.click()
                print_minefield()


def random_player():
    """ TODO: don't click open fields (m12345678) """
    while True:
        if is_dead():
            break

        filtered_minefield = list(filter(lambda e: minefield_element_to_type(e) == '-', minefield_elements))

        next_field = random.randint(0, len(filtered_minefield)-1)

        filtered_minefield[next_field].click()
        print_minefield()


def algoritmic_player():
    minefield_elements[0].click()
    possible_minefield = mines_funsolver(9, 9, 10, calc_minefiled())
    print("possible: ")
    print(possible_minefield)

    while True:
        if is_dead():
            break

        for index, minefield_element in enumerate(minefield_elements):
            minefield_element_to_type(minefield_element) == possible_minefield[index]


        next_possible = possible_minefield[0].click()
        possible_minefield = possible_minefield[1:]
        next_possible.click()

algoritmic_player()
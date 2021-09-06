import csv

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/bowling-scorecard.html"

driver.get(URL)

# osszes gombot kiszedem es majd a lista elemeit kattintgatom
buttons = driver.find_elements_by_tag_name("button")


def hit_pins(pin_hits_data):
    for hit in pin_hits_data:
        buttons[hit].click()
        # time.sleep(0.5)


def tuple_to_str(t):
    if len(t) == 2:
        return f'{t[0]},{t[1]}'  # "0,7"
    else:
        return f'{t[0]}'  # X


def check_frames(frames_data):
    frames = driver.find_elements_by_xpath('//td[contains(@id, "frame")]')
    for idx, frame in enumerate(frames_data):
        assert frames[idx].text == tuple_to_str(frame)


def check_markers(markers_data):
    markers = driver.find_elements_by_xpath('//td[contains(@id, "marker")]')
    for idx, marker in enumerate(markers_data):
        assert markers[idx].text == str(marker)


pin_hits = [[0, 1, 2, 3, 4, 5, 6, 0, 7, 0, 8, 0, 9, 0, 10, 10, 0, 0],
            [('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',)],
            [6, 5]]
exp_frames = [[(0, 1), (2, 3), (4, 5), (6, 0), (7, 0), (8, 0), (9, 0), ('X',), ('X',), (0, 0)],
              ['', '', '', '', '', '', '', '', '', '']]
exp_markers = [[1, 6, 15, 21, 28, 36, 45, 55, 65, 75]]


def test_pin_hit():
    """ Helyes grurítások adminisztrációja jól működik
            gurítsunk sorrendben: 0,1,2,3,4,5,6,0,7,0,8,0,9,0,10,10,0,0
            ellenőrizzük, hogy ezek a gruítások szerepelnek: [(0,1),(2,3),(4,5),(6,0),(7,0),(8,0),(9,0),(X,),(X,),(0,0)]
            ellenőrizzük, hogy ezek az összegek szerepelnek: [1,6,15,21,28,36,45,55,65,75] """

    hit_pins(pin_hits[0])
    time.sleep(0.5)
    check_frames(exp_frames[0])
    time.sleep(0.5)
    check_markers(exp_markers[0])
    time.sleep(0.5)


def test_initial():
    """ Helyes jelenik meg az üres eredmény kártya:
            mind a 10 guritási mező üres
            mind a 10 összegző mező üres """

    check_frames(exp_frames[1])
    time.sleep(0.5)
    check_markers(exp_markers[1])
    time.sleep(0.5)


def test_error():
    """ Nem lehet egyszerre 11 bábút gurítani:
        gurítsunk: 6, majd 5 bábút
        ellezőrizzük, hogy a hibaüzenet ezt írja-e: Invalid Roll - there are only ten pins! """
    exp_error = "Invalid Roll - there are only ten pins!"

    hit_pins(pin_hits[2])
    time.sleep(0.5)
    assert driver.find_element_by_id("comments").text == exp_error


# test_pin_hit()
# test_initial()
test_error()

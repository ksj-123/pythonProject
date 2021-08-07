from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


def find_and_clear(id):
    find = driver.find_element_by_id(id)
    find.clear()
    return find


try:
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html')

    # TC01: lotto huzas elott nem ismertek a szamok
    ball = driver.find_element_by_id('container')
    ball_numb = driver.find_element_by_class_name('balls')
    while True:


    # if: ball nem tartalmaz ball_numb
    # else: False

    # TC02: lotto huzas mukodik
    def generate():
        generateBtn = driver.find_element_by_id('draw-number')
        generateBtn.click()
        generateBtn.click()
        generateBtn.click()
        generateBtn.click()
        generateBtn.click()
        generateBtn.click()


    generate()


    # ball = driver.find_element_by_id('container')
    # # tartalmaz 6 ball
    # ball_numb = driver.find_element_by_class_name('balls')
    # # print(ball_numb, ",")
    # 1 és 59 között

    # TC03: lottohuzas befejezodott
    def generate():
        generateBtn = driver.find_element_by_id('draw-number')
        generateBtn.click()
        generateBtn.click()
        generateBtn.click()
        generateBtn.click()
        generateBtn.click()
        generateBtn.click()
        generateBtn.click()


    generate()


    # ball = driver.find_element_by_id('container')
    # # csak 6 ball tartalmaz

    def reset():
        resetBtn = driver.find_element_by_id('reset-numbers')
        resetBtn.click()


    reset()

    while True:
# if: ball nem tartalmaz ball_numb
# else: False


finally:
    driver.close()

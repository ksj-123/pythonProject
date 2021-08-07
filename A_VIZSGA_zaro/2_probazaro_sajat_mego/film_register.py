# Film register test
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

# regisztrációs adatok
title = 'Black widow'
year = '2021'
cron = '2020'
trailer = 'https://www.youtube.com/watch?v=Fp9pNPdNwjI'
image = 'https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg'
summary = 'https://www.imdb.com/title/tt3480822/'


def find(id):
    find = driver.find_element_by_id(id)
    return find


def findx(xpath):
    findx = driver.find_element_by_xpath(xpath)
    return findx


try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html')
    time.sleep(3)


    # "betöltés után megjelennek filmek az alkalmazásban, méghozzá 24 db"
    # count = driver.find_element_by_class_name('center')
    # assert print(len(count)) == '24'

    # adatfeltöltés
    def register():
        reg_button = findx('/html/body/div[2]/div[1]/button')
        reg_button.click()
        time.sleep(2)
        find('nomeFilme').send_keys(title)
        find('anoLancamentoFilme').send_keys(year)
        find('anoCronologiaFilme').send_keys(cron)
        find('linkTrailerFilme').send_keys(trailer)
        find('linkImagemFilme').send_keys(image)
        find('linkImdbFilme').send_keys(summary)
        time.sleep(2)
        save_button = findx('/html/body/div[2]/div[2]/fieldset/button[1]')
        save_button.click()


    register()

    # assert title == findx('/html/body/div[2]/div[3]')
    # print(title)

finally:
    driver.close()

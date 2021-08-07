# Marvel Mutant Teams test
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 600, 600)

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html')
    time.sleep(3)

    # Teams Xpath
    original = '/html/body/div/label[1]'
    force = '/html/body/div/label[2]'
    factor = '/html/body/div/label[3]'
    hellfire = '/html/body/div/label[4]'


    # Driver find xpath
    def find_x(xpath):
        find_x = driver.find_element_by_xpath(xpath)
        return find_x


    # Driver find id
    def find_id(id):
        find_id = driver.find_element_by_id(id)
        return find_id

    # Angel
    # def angel():
    #     find_id('angel')
    #     if angel():
    #         data_teams = driver.find_element_by_class_name('data-teams')
    #         assert find_id(data_teams) == 'original force factor hellfire'
    #         print(True)
    #     else:
    #         print(False)
    #
    #
    # angel()
    # hibás a lekérdezés, de

    # a többi csapattagnál is hasonlóan






finally:
    driver.close()

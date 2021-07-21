# # hacker chet
#
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
#
# driver = webdriver.Chrome()
#
# try:
#     driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/hackernews/index.html#/")
#     hacker_sor = driver.find_element_by_xpath('//div[@class="story"]')
#     with open("hacker.txt", "w") as file:
#         file.write(hacker_sor)
# #         print(anchor.text()
#
# finally:
#     pass
# driver.close()


#####

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

opt = Options()

opt.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/hackernews/index.html")
try:
    links = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="story"]/div/a')))
except TimeoutException:
    print('Időtúllépés')

link_file = open('linkek.txt', 'w')
for link in links:
    link_file.write(f'{link.text}\n')
link_file.close()

driver.close()


#####

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
opt = Options()
opt.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/hackernews/index.html")
try:
    links = WebDriverWait(driver, 30).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="story"]/div/a')))
except TimeoutException:
    print('Időtúllépés')
link_file = open('linkek.txt', 'w')
words_stat = dict()
for link in links:
    link_file.write(f'{link.text}\n')
    for word in link.text.split():
        if word in words_stat:
            words_stat[word] = words_stat[word] + link.text.count(word)
        else:
            words_stat[word] = link.text.count(word)
link_file.close()
words_stat = dict(sorted(words_stat.items(), key=lambda item: item[1], reverse=True))
print(words_stat)
driver.close()
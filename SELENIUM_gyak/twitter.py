from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver = webdriver.Chrome()

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/twitter.html")

    # sign out (TC15 - kijelentkezés)
    sign_out = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/div[2]/a[3]")
    sign_out.click()
    time.sleep(2)

    # nem aktív, nem vizsgálható jelenleg a sign_in (TC16 - bejelentkezés)
    # sign_in = driver.find_element_by_text("Sign In")
    # sign_in.click()
    # time.sleep(2)

    # new tweet (TC4 - új Tweet megjelenése Tweet gomb megnyomsa után)
    new_tweet = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/textarea")
    with open('tweet.txt') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
    tweet_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/button")
    tweet_button.click()
    time.sleep(2)
    # még kiegészíteném a kép feltöltésével, illetőleg a szöveget lehetne nem fájlból, hanem egyből
    # egy szöveget beleíratni, csak hogy működkik e a dolog


    #
    # hány ember van követve előtte
    # followed_before =
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul[2]/li[2]/div/div[2]/div[2]/button").click()
    # hány ember van követve utána
    # followed_after =
    # assert
    time.sleep(2)

    # szerkesztés gomb elérése (TC13 saját profil szerkesztese)
    driver.find_element_by_xpath("//a[text='Edit Profile']").click()
    time.sleep(2)




finally:
    pass
# driver.close()

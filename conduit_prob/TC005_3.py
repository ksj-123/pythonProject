# TC005 - New blog post
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import csv
import string
import random

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 600, 600)

try:
    # Oldal betöltése
    driver.get("http://localhost:1667/")
    time.sleep(3)

    # Feltöltendő adatok megadása
    email = 'username5005@gmail.com'
    pwd = 'Username5005'
    title = random.sample(string.ascii_letters, 10)
    about = random.sample(string.ascii_letters, 15)
    write = random.sample(string.ascii_letters, 50)
    tags = random.sample(string.ascii_letters, 8)

    # Post mezők xpath
    title_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
    about_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
    write_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
    tags_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'


    # Driver find
    def find(xpath):
        find = driver.find_element_by_xpath(xpath)
        return find


    # Sign in
    def sign_in(email, pwd):
        sign_button = find('//*[@id="app"]/nav/div/ul/li[2]/a')
        sign_button.click()
        find('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(email)
        find('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys(pwd)
        sign_in_btn = find('//*[@id="app"]/div/div/div/div/form/button')
        sign_in_btn.click()
        time.sleep(2)


    sign_in(email, pwd)
    time.sleep(3)

    # Write post
    with open('../text/post_out.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(title)
        for i in range(3):
            def write_post():
                find('//*[@id="app"]/nav/div/ul/li[2]/a').click()
                time.sleep(2)
                titlew = find(title_x).send_keys(title)
                print(titlew)
                aboutw = find(about_x).send_keys(about)
                print(aboutw)
                writew = find(write_x).send_keys(write)
                print(writew)
                tagsw = find(tags_x).send_keys(tags)
                print(tagsw)
                write_btn = find('//*[@id="app"]/div/div/div/div/form/button')
                write_btn.click()

            write_post()
        time.sleep(2)

# Controll
# print(find('//*[@id="app"]/div/div[1]/div/h1').text)
# assert (title in find('//*[@id="app"]/div/div[1]/div/h1').text)


finally:
    pass
# driver.close()

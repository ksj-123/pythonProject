# TC005 - New blog post
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import csv

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 600, 600)


# Driver find
def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


try:
    # Load page
    URL = driver.get("http://localhost:1667/")
    time.sleep(3)

    # Enter the data to be uploaded
    email = 'testuser1@example.com'
    username = 'testuser1'
    pwd = 'Abcd123$'

    # Xpath field
    email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
    username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
    pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
    title_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
    about_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
    write_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
    tags_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'
    sign_btn = '//*[@id="app"]/nav/div/ul/li[2]/a'
    sign_inbtn = '//*[@id="app"]/div/div/div/div/form/button'
    new_artbtn = '//*[@id="app"]/nav/div/ul/li[2]/a'
    publish = '//*[@id="app"]/div/div/div/div/form/button'


    # Sign in
    def sign_in(email, pwd):
        sign_button = find(sign_btn)
        sign_button.click()
        find(email_x).send_keys(email)
        find(pwd_x).send_keys(pwd)
        sign_in_btn = find(sign_inbtn)
        sign_in_btn.click()
        time.sleep(2)


    sign_in(email, pwd)
    time.sleep(3)

    assert username == find(username_x).text
    print(username)
    time.sleep(2)


    def creat_post(row):
        find(new_artbtn).click()
        print(row)
        find(title_x).send_keys(row[0])
        find(about_x).send_keys(row[1])
        find(write_x).send_keys(row[2])
        find(tags_x).send_keys(row[3])
        find(publish).click()
        


    # Write new post
    def new_post():
        with open('post.csv') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                creat_post(row)


    new_post()

    # Controll
    # assert # az új poszt címét, stb.-t kellene összehasonlítani a felület és a post.csv tartalma között???

finally:
    driver.close()

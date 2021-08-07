from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import string
import random

# def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))
#
#
# id_generator()
# print(id_generator())

#-------------------------------
# -random letter generator-

# var1 = string.ascii_letters
# print(var1)
#
# var2 = random.choice(string.ascii_letters)
# print(var2)

#-------------------------------
for i in range(3):
    # get random string of length 6 without repeating letters
    result_str = ''.join(random.sample(string.ascii_letters, 8))
    print(result_str)

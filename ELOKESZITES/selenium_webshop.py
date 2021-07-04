# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://react-card-2a6c5.web.app/")
#
# t_shirt = driver.find_elements_by_class_name("<div class="shelf-item__buy-btn">Add to cart</div>")
# print(t_shirt)
#
# for x in t_shirt:
#     x.click()

#-----

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# opt = Options()
# opt.headless = True
# driver = webdriver.Chrome()
# driver.get('https://react-card-2a6c5.web.app/')
# time.sleep(2)
# add_to_cart = driver.find_elements_by_xpath('//div[@class="shelf-item__buy-btn"]')
# driver.set_window_size(1920,1080)
# print(len(add_to_cart))
# for element in add_to_cart:
#     element.click()
# price = driver.find_element_by_class_name("sub-price__val")
# print(price)
# assert price == "$ 440.00"
# driver.close()
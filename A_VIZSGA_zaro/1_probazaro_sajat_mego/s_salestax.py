from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.set_window_size(1000, 500, 500)


def find_and_clear(id):
    find = driver.find_element_by_id(id)
    find.clear()
    return find


try:
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html')

    # TC01: üres kitöltés helyessége
    subtotalBtn = driver.find_element_by_id('subtotalBtn')
    subtotalBtn.click()
    sub = driver.find_element_by_id('subtotal').text
    assert (sub == '0.00')

    gtotalBtn = driver.find_element_by_id('gtotalBtn')
    gtotalBtn.click()
    grand = driver.find_element_by_id('gtotal').text
    assert (grand == "4.95")


    # TC02: 6" x 6" Volkanik Ice kitöltés helyessége
    def sales():
        item = find_and_clear('Proditem')
        item.send_keys(driver.find_element_by_xpath('//*[@id="Proditem"]/option[2]'))
        quan = find_and_clear('quantity')
        quan.send_keys('1')


    sales()

    subtotalBtn = driver.find_element_by_id('subtotalBtn')
    subtotalBtn.click()

    sub = driver.find_element_by_id("subtotal").text
    sub.click()
    assert (sub == "4.95")

    gtotalBtn = driver.find_element_by_id("gtotalBtn")
    gtotalBtn.click()

    grand = driver.find_element_by_id("gtotal").text
    assert (grand == "9.90")


finally:
    driver.close()

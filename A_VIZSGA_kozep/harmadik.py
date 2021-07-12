from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()

try:
    driver.get("https://proud-cliff-00bebe803.azurestaticapps.net/harmadik.html")

    cash_input = driver.find_element_by_id("cash")
    bet_input = driver.find_element_by_id("bet")
    tails_button = driver.find_element_by_id('tails')
    heads_button = driver.find_element_by_id('heads')

    # scenario TC_000: kezdeti értékek
    # need to clear input fields before typing new data (money = '100'; bet = ' '; result = '-')
    cash_text = driver.find_element_by_id("cash").text
    assert cash_text == "100"
    bet_text = driver.find_element_by_id("bet").text
    assert cash_text == ""
    result_text = driver.find_element_by_id("result").text
    assert cash_text == "-"

    # scenario TC_001
    bet_input.send_keys("100")
    tails_button.click()
    if result_text == 'heads' or 'tails':
        cash_text == '110'
    else:
        cash_text == '90'

finally:
    driver.close()

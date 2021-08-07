from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver import Chrome
import time

@pytest.fixture
def browser():
    # Initialize ChromeDriver
    driver = Chrome()
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    return driver

def test_basic_duckduckgo_search(browser):
    URL = 'https://duckduckgo.com/'
    PHRASE = "panda"

    browser.get(URL)
    time.sleep(3)

    search_input = browser.find_element_by_id("search_form_input_homepage")
    search_input.send_keys(PHRASE + Keys.RETURN)

    time.sleep(3)

    link_divs = browser.find_elements_by_css_selector('#links > div')
    assert len(link_divs) > 0

    xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
    phrase_results = browser.find_elements_by_xpath(xpath)
    assert len(phrase_results) > 0

    search_input = browser.find_element_by_id("search_form_input")
    assert search_input.get_attribute("value") == PHRASE
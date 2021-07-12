from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# driver = webdriver.Edge(EdgeChromiumDriverManager().install())
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://python.org")
search_field = driver.find_element_by_name('q')
search_field.send_keys("hello")

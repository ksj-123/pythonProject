from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://react-card-2a6c5.web.app/")

t_shirt = driver.find_elements_by_class_name("<div class="shelf-item__buy-btn">Add to cart</div>")
print(t_shirt)

for x in t_shirt:
    x.click()

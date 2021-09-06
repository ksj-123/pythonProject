## 1 Feladat: Keressük a kör területét
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
# A program töltse be a kör területe app-ot az [https://wonderful-pond-0d96a8503.azurestaticapps.net/f1.html](https://wonderful-pond-0d96a8503.azurestaticapps.net/f1.html) oldalról.
# Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a kör területe appban:
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!
# * Helyes kitöltés esete:
#     * r: 10
#     * Eredmény: 314
# * Nem számokkal történő kitöltés:
#     * r: kiscica
#     * Eredmény: NaN
# * Üres kitöltés:
#     * r: <üres>
#     * Eredmény: NaN

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://wonderful-pond-0d96a8503.azurestaticapps.net/f1.html"

driver.get(URL)
r_input = driver.find_element_by_id("r")
submit_button = driver.find_element_by_id("submit")
result_text = driver.find_element_by_id("result")

# tesztadatok
test_data = ["10", "kiscica", ""]
reference_data = ["314", "NaN", "NaN"]

# teszt függvények - végül nem használtuk
test_data2 = [
    {"input": "10",
     "result": "314",
     "id_selector": "r"},
    {"input": "kiscica",
     "result": "NaN",
     "id_selector": "r"},
    {"input": "",
     "result": "NaN",
     "id_selector": "r"},
]

# ismétlés helyett kiemelés
def clear_and_fill_input(element, text):
    element.clear()
    element.send_keys(text)


# * Helyes kitöltés esete:
# * r: 10
# * Eredmény: 314
def test_positive():
    clear_and_fill_input(r_input, test_data[0])
    submit_button.click()
    assert result_text.text == reference_data[0]


# * Nem számokkal történő kitöltés:
#     * r: kiscica
#     * Eredmény: NaN
def test_neg_chars():
    clear_and_fill_input(r_input, test_data[1])
    submit_button.click()
    assert result_text.text == reference_data[1]


# * Üres kitöltés:
#     * r: <üres>
#     * Eredmény: NaN
def test_neg_chars2():
    clear_and_fill_input(r_input, test_data[2])
    submit_button.click()
    assert result_text.text == reference_data[2]


def do_something(rin, exp):
    clear_and_fill_input(r_input, rin)
    submit_button.click()
    assert result_text.text == exp


# test_positive()
# test_neg_chars()
# test_neg_chars2()

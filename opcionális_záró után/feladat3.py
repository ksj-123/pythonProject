## 3 Feladat: Véletlen kalkulátor
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
# A program töltse be a véletlen kalkulátor app-ot az [https://wonderful-pond-0d96a8503.azurestaticapps.net/f3.html](https://wonderful-pond-0d96a8503.azurestaticapps.net/f3.html) oldalról.
# Feladatod, hogy automatizáld selenium webdriverrel a  véletlen kalkulátor app tesztelését.
# Az applikáció minden frissítésnél véletlenszerűen változik!
# A feladatod, hogy a random számokkal működő matematikai applikációt ellenőrizd. A teszted ki kell, hogy olvassa a két operandust (számot) és az operátort (műveleti jelet).
# Ennek megfelelően kell elvégezned a kalkulációt Pythonban.
# A kalkulátor gombra kattintva mutatja meg az applikáció, hogy mi a művelet eredménye szerinte.
# Hasonlítsd össze az applikáció által kínált megoldást és a Python által kalkulált eredményt. Ennek a kettőnek egyeznie kell.
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://wonderful-pond-0d96a8503.azurestaticapps.net/f3.html"

driver.get(URL)

op1 = driver.find_element_by_id("op1")
op2 = driver.find_element_by_id("op2")
num1 = driver.find_element_by_id("num1")
num2 = driver.find_element_by_id("num2")
num3 = driver.find_element_by_id("num3")
submit_button = driver.find_element_by_id("submit")


def assemble_expression(*args):
    return "{}{}{}{}{}".format(*args)

# eval függvény
def test_evaluate_expression():
    submit_button.click()
    result_text = driver.find_element_by_id("result")
    ex = assemble_expression(num1.text, op1.text, num2.text, op2.text, num3.text)
    assert eval(ex) == int(result_text.text)

# assert eval(f"{num1.text}{op1.text}{num2.text}{op2.text}{num3.text}") == int(result_text.text)

test_evaluate_expression()

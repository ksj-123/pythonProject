from selenium import webdriver

driver = webdriver.Chrome()
import time

try:
    driver.get("https://happy-sea-0a5ffef03.azurestaticapps.net/harmadik.html")

# be akartam hivatkozni az alapállapot stílusában lévő színeket
WebElement
el = driver.findElement(By.xpath("//a[text()='LEARN HTML']"));
String
contents = (String)((JavascriptExecutor)
drive)
.executeScript("return window.getComputedStyle(arguments[0]).getPropertyValue('background-color');", el);
System.out.println(contents);

# ha meg lett volna a stíulban a színeknek a hivatkozása, akkor assert-tel, a gomb megnyomása után a változást lehetne ellenőrizni

color_button = driver.find_element_by_xpath('//*[@id="banner-message"]/button')
color_button.click()

driver.close();

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.color import Color
import time

opt = Options()

opt.headless = True

driver = webdriver.Chrome(options=opt)

driver.get('https://happy-sea-0a5ffef03.azurestaticapps.net/harmadik.html')

bgcolor = '#0084ff'
fgcolor = '#ffffff'

btn = driver.find_element_by_tag_name('button')

dialog_color = driver.find_element_by_id('banner-message').value_of_css_property('background-color')
btn_color = btn.value_of_css_property('background-color')

assert Color.from_string(dialog_color).hex == fgcolor
assert Color.from_string(btn_color).hex == bgcolor

btn.click()

time.sleep(1)

btn = driver.find_element_by_tag_name('button')

dialog_color = driver.find_element_by_id('banner-message').value_of_css_property('background-color')
btn_color = btn.value_of_css_property('background-color')

assert Color.from_string(dialog_color).hex == bgcolor
assert Color.from_string(btn_color).hex == fgcolor

driver.close()
# video lejátszás tesztelése

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/videos.html")
    html5video = driver.find_element_by_id("html5video")
    html5video.click()
    html5video.send_keys(Keys.SPACE)
    time.sleep(4)
    # képernyőkép használatával ellenőrizzük le, hogy a videolejátszás elindult
    html5video.screenshot('video_screenshot.png') 

    time.sleep(5)

finally:
    driver.close()


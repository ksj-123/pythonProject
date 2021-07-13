# HF-hez segítség - kattintgatás

driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/windowgame.html")
button_list = driver.find_elements_by_tag_name("button")
for _ in range(10):
    button_list[random.randint(0, len(button_list)-1)].click()
    driver.switch_to.window(driver.window_handles[-1])
    print(driver.find_element_by_tag_name("h1").text)
    driver.switch_to.window(driver.window_handles[0])

# HF-hez segítség - videó betöltés 1. ver.

driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/videos.html")
frame = driver.find_element_by_id("youtubeframe")
driver.switch_to.frame(frame)
time.sleep(2)
driver.find_element_by_id("player").click()

# HF-hez segítség - videó betöltés 2. ver.

frameElement = driver.find_element_by_xpath("//iframe[@src='https://www.youtube.com/embed/tgbNymZ7vqY']")
driver.switch_to.frame(frameElement)
driver.find_element_by_xpath("//button[@aria-label='Lejátszás']").click()
time.sleep(5)
WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='movie_player']"))).send_keys(Keys.SPACE)




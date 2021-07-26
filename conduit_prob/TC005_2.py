def register(username, email, password):
    driver.get("http://localhost:1667/#/")
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys('First')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys('first@gmail.com')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[3]/input').send_keys('First12345')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()


register('First', 'first@gmail.com', 'First12345')
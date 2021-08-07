from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html')


    # TC01: üres kitöltés helyessége
    # def email:
    #     driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[1]')
    # while True:
    #     emailBtn():
    #     driver.find_element_by_xpath('//*[@id="buttons"]/input')
    #
    #     (ng - disabled = "formTimesheet.$invalid")
    #
    #     if email cím nem tartalmaz @ és .
    #     if email cím csak @ tartalmaz .-ot nem
    #     if email cím csak .-ot tartalmaz @ nem
    #     elif email = ('')
    # else: (ng - click = "saveForm()")
    #         break

    # TC02: helyes kitöltés helyes köszönet képernyő
    def timesheet():
        email = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[1]')
        email.send_keys('test@bela.hu')
        hours = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[2]')
        hours.send_keys('2')
        minut = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[3]')
        minut.send_keys('0')
        message = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/textarea')
        message.send_keys('working hard')
        type = driver.find_element_by_xpath('//*[@id="dropDown"]/option')
        type.click()


    timesheet()

    next = driver.find_element_by_xpath('//*[@id="buttons"]/input')
    next.click()

    email_control = driver.find_element_by_xpath('//*[@id="section-thankyou"]/div/p[1]/span').text
    assert (email_control == 'test@bela.hu')

    hour_control = driver.find_element_by_xpath('//*[@id="section-thankyou"]/div/p[2]/span[1]')
    assert (hour_control == '2')

    minu_control = driver.find_element_by_xpath('//*[@id="section-thankyou"]/div/p[2]/span[2]')
    assert (minu_control == '0')

finally:
    driver.close()

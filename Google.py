import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(options=webdriver.ChromeOptions())
driver.get('http://www.kurs-selenium.pl/demo/')
driver.maximize_window()

driver.find_element('xpath','//*[@id="s2id_autogen8"]/a/span[1]').click()
driver.find_element('xpath','//*[@id="select2-drop"]/div/input').send_keys('Dubai')
time.sleep(1) #let's the list load
driver.find_element('xpath','//*[@id="select2-drop"]/ul/li/ul/li/div/span').click()
#driver.find_element('xpath', '//*[@id="select2-drop"]/ul/li/ul/li/div/span[text()[contains(.,"Dubai")]]').click() #safer version - it also "checks" if the value on list is correct

driver.find_element('name', 'checkin').click()
time.sleep(1)
driver.find_element('xpath', '/html/body/div[9]/div[1]/table/tbody/tr[2]/td[5]').click()
driver.find_element('name', 'checkout').clear()
driver.find_element('name', 'checkout').send_keys("20/02/2023")

driver.find_element('name', 'travellers').click()
time.sleep(1) #slow computer :')
driver.find_element('name', 'child').clear()
time.sleep(1) #slowboy here strikes again, let's give him some time to process 
driver.find_element('name', 'child').send_keys('2')

driver.find_element('xpath', '//*[@id="hotels"]/form/div[5]/button').click()

hotels = driver.find_elements('xpath', '//h4[contains(@class,"list_title")]//b')
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_names:
    print(name)

prices = driver.find_elements('xpath', '//div[contains(@class,"price_tab")]//b')
price_value = [price.get_attribute('textContent') for price in prices]
for value in price_value:
    print(value)



time.sleep(3) #leaves the window open for 3 sec


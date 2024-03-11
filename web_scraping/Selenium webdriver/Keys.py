from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://bednyakov.ru')

content = browser.find_element(By.NAME, 'html')
content.send_keys(Keys.END)
content.send_keys(Keys.HOME)

browser.back()
browser.forward()
browser.refresh()
browser.quit()
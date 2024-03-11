from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://bednyakov.ru')

try:
    content = browser.find_element(By.CLASS_NAME, 'entry-title')
    print(f'Контент класса {content.tag_name} найден.')
except:
    print('Искомый элемент не обнаружен.')

content.click()

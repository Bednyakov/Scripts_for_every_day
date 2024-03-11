from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://bednyakov.ru/contacts/')

try:
    user_name = browser.find_element(By.CSS_SELECTOR, '#wpcf7-f134-p9-o1 > form > p:nth-child(2) > label > span > input')
    password = browser.find_element(By.CSS_SELECTOR, '#wpcf7-f134-p9-o1 > form > p:nth-child(4) > label > span > input')
    user_name.send_keys('Тёма')
    password.send_keys('12345')

    password.submit()
    print(f'Поля заполнены')
except:
    print('Искомые элементы не обнаружены.')
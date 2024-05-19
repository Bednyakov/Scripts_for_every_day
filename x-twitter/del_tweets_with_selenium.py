from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Замените на путь к драйверу вашего браузера (пример для Chrome)
driver_path = "путь_к_драйверу_браузера/chromedriver"

# Создаем экземпляр веб-драйвера
driver = webdriver.Chrome(executable_path=driver_path)

# Замените на ваше имя пользователя и пароль от Twitter
username = "your_username"
password = "your_password"

# Открываем Twitter
driver.get("https://twitter.com")

# Ждем загрузки страницы
time.sleep(2)

# Входим в аккаунт
login_link = driver.find_element_by_link_text("Log in")
login_link.click()

time.sleep(2)

username_input = driver.find_element_by_name("session[username_or_email]")
password_input = driver.find_element_by_name("session[password]")
username_input.send_keys(username)
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

# Ждем загрузки страницы
time.sleep(2)

# Получаем ссылку на профиль
profile_link = driver.find_element_by_id("profile_tab")
profile_link.click()

# Ждем загрузки страницы
time.sleep(2)

# Находим и удаляем все твиты
while True:
    delete_buttons = driver.find_elements_by_xpath("//div[@data-testid='tweet']//div[contains(@aria-label, 'Delete Tweet')]")
    if len(delete_buttons) == 0:
        print("All tweets deleted.")
        break
    else:
        delete_buttons[0].click()
        time.sleep(1)
        confirm_delete_button = driver.find_element_by_xpath('//div[@role="button" and text()="Delete"]')
        confirm_delete_button.click()
        time.sleep(2)

# Закрываем браузер
driver.quit()

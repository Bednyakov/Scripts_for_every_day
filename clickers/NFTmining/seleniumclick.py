from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Путь к профилю пользователя Chrome
user_profile = "C:/Users/Артем/AppData/Local/Google/Chrome/User Data"

# Настройка параметров Chrome
options = Options()
options.add_argument(f"user-data-dir={user_profile}")

# Указание пути к chromedriver
service = Service('/chromedriver')  # Укажите путь к chromedriver

# Инициализация WebDriver с профилем пользователя
driver = webdriver.Chrome(options=options)

try:
    # Загрузка веб-страницы
    driver.get("https://nftmining.com/skale-mint")

    # Пример взаимодействия с веб-страницей
    # Ожидание загрузки кнопки
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'font-montserrat') and contains(@class, 'bg-main-pink1') and contains(text(), 'Mine Crystal')]")))

    # Проверка, активирована ли кнопка
    if button.is_enabled():
        print("Кнопка уже активирована")
    else:
        # Активируем кнопку
        button.click()
        print("Кнопка активирована")
    
except Exception as e:
    print(e)

finally:
    # Закрытие браузера
    driver.quit()

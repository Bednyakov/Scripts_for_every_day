import requests
from time import time, sleep
from random import randint

# URL для отправки POST-запроса синхронизации
url = "https://api.hamsterkombat.io/clicker/sync"

# Заголовки запроса
headers = {
    "Connection":	"keep-alive",
    "sec-ch-ua":	'"Chromium";v="122", "Not(A:Brand";v="24", "Android WebView";v="122"',
    "sec-ch-ua-mobile":	'?1',
    "User-Agent":	"Mozilla/5.0 (Linux; Android 11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.64 Mobile Safari/537.36",
    "sec-ch-ua-platform":	'"Android"',
    "Accept":	"*/*",
    "Origin":	"https://hamsterkombat.io",
    "X-Requested-With":	"org.telegram.messenger",
    "Sec-Fetch-Site":	"same-site",
    "Sec-Fetch-Mode":	"cors",
    "Sec-Fetch-Dest":	"empty",
    "Referer":	"https://hamsterkombat.io/",
    "Accept-Encoding":	"gzip, deflate, br",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",  # Замените YOUR_ACCESS_TOKEN на ваш токен авторизации
}

def sync_request():
    """
    Функция для отправки POST-запроса синхронизации и клейма монет.
    """
    with requests.Session() as session:
        response = session.post(url, headers=headers)

        if response.status_code == 200:
            result = response.json()
            print(result)

        else:
            print("Ошибка при отправке POST-запроса:", response.status_code, response.text)


def main():
    """
    Функция каждые три часа вызывает функцию синхронизации.
    """
    while True:
        sync_request()
        sleep(randint(10801, 11131))


if __name__ == "__main__":
    main()
